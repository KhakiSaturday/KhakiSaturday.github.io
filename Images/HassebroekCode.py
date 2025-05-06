# Hunter Hassebroek
# EGR314 Team 310
# HMI Subsystem
import uasyncio as asyncio
from machine import Pin, SPI, UART
import st7789  # ST7789 driver 
import vga1_16x16 as font  

# ---------- Configuration Constants ----------

# UART communication parameters
BAUD_RATE = 115200
START_BYTE = 0x02  # Protocol start-of-message byte
STOP_BYTE  = 0x03  # Protocol end-of-message byte

UART0_TX_PIN = 19  
UART0_RX_PIN = 20   
UART1_TX_PIN = 17  
UART1_RX_PIN = 16  

TFT_MOSI  = 35   
TFT_SCK   = 41   
TFT_CS    = 15    
TFT_DC    = 36
TFT_BL    = 2  

# Display dimensions (in pixels)
TFT_WIDTH  = 240
TFT_HEIGHT = 240

# Button pins (GPIO 9 through 13) with internal pull-ups
BUTTON_PINS = [9, 10, 11, 12, 13]
DEBOUNCE_MS = 20   # Debounce check interval (ms)
STABLE_COUNT = 3   # Number of consecutive stable reads (each ~10ms apart) to confirm state

# ---------- Global Variables for State ----------

# Speed and statistics
speed = 0  # current speed value
speed_history = [speed]  # list to keep last up to 20 speed values
min_speed = speed        # minimum recorded speed
max_speed = speed        # maximum recorded speed
avg_speed = speed        # average speed (integer)

# Message log (store last up to 6 messages as bytes or strings)
message_history = []  # will store the content of messages received (excluding framing)

# UART interfaces
# (Using UART0 and UART1. Note: UART0 is typically the REPL interface on ESP32.)
uart0 = UART(0, BAUD_RATE, tx=Pin(UART0_TX_PIN), rx=Pin(UART0_RX_PIN))
uart1 = UART(1, BAUD_RATE, tx=Pin(UART1_TX_PIN), rx=Pin(UART1_RX_PIN))
# Warning: Using UART0 for custom data will interfere with the USB REPL if it's active.
# You may disable REPL on UART0 or use UART(2) instead of UART0 if needed.

# Initialize display (SPI and ST7789 driver)
spi = SPI(2, baudrate=40000000, polarity=1, phase=1,
          sck=Pin(TFT_SCK), mosi=Pin(TFT_MOSI))
display = st7789.ST7789(spi, TFT_WIDTH, TFT_HEIGHT,
                        cs=Pin(TFT_CS, Pin.OUT),
                        dc=Pin(TFT_DC, Pin.OUT),
                        rotation=0)  # rotation=0 (adjust as needed for your display orientation)
display.init()  # initialize the display controller
# Turn on backlight if pin is defined
if TFT_BL is not None:
    bl = Pin(TFT_BL, Pin.OUT)
    bl.value(1)

# Clear display initially
display.fill(st7789.BLACK)

# Configure button pins as inputs with pull-ups
buttons = []
for gp in BUTTON_PINS:
    pin = Pin(gp, Pin.IN, Pin.PULL_UP)
    buttons.append({
        "pin": pin,
        "stable_state": 1,    # current debounced stable state (1 = not pressed, since pull-up)
        "count": 0           # counter for debounce state changes
    })
# Button functions: define actions for each button (by index or pin)
# Here we map:
#  GPIO9 -> decrease speed, GPIO10 -> increase speed,
#  GPIO11 -> send current speed message, GPIO12 -> reset min/max/avg, GPIO13 -> clear messages
btn_decrease = BUTTON_PINS[0]
btn_increase = BUTTON_PINS[1]
btn_send     = BUTTON_PINS[2]
btn_reset    = BUTTON_PINS[3]
btn_clear    = BUTTON_PINS[4]

def send_message(payload: bytes, uart: UART):
    """Send a message with protocol framing (start/stop bytes) over the given UART."""
    frame = bytes([START_BYTE]) + payload + bytes([STOP_BYTE])
    uart.write(frame)
    # (Optionally, also log the sent message or print to console for debugging)

# ---------- Asynchronous Tasks ----------

async def uart_rx_task(uart: UART, name: str):
    """Task to read incoming data from a UART and assemble messages based on start/stop bytes."""
    buffer = bytearray()
    in_message = False  # tracking if we are inside a message frame
    while True:
        # Read all available data from UART (non-blocking)
        if uart.any():
            data = uart.read()  # read all bytes available
            if data:
                for b in data:
                    byte = b if isinstance(b, int) else ord(b)  # ensure we have an int byte value
                    if not in_message:
                        # Not currently in a message, look for start byte
                        if byte == START_BYTE:
                            in_message = True
                            buffer = bytearray()  # start a new message buffer (content only)
                    else:
                        # Already in a message, accumulate bytes until stop
                        if byte == START_BYTE:
                            # Unexpected start byte while already in a message:
                            # reset buffer and start new message frame
                            buffer = bytearray()
                            in_message = True
                            # (We stay in_message since a new frame started)
                        elif byte == STOP_BYTE:
                            # End-of-message reached, finalize message
                            in_message = False
                            # Convert buffer to bytes and store in history
                            msg_bytes = bytes(buffer)
                            # Log the message content (save last 6 messages)
                            message_history.append(msg_bytes)
                            if len(message_history) > 6:
                                # Remove oldest message if exceeding history size
                                message_history.pop(0)
                            # (Here you could also parse or react to specific message content if needed)
                            buffer = bytearray()  # reset buffer for next message
                        else:
                            # Regular byte of message content
                            buffer.append(byte)
        # Small delay to yield control (adjust polling rate as needed)
        await asyncio.sleep_ms(10)

async def button_task():
    """Task to poll button inputs, debounce them, and handle state changes (presses)."""
    global speed, min_speed, max_speed, avg_speed  # we will modify these globals
    while True:
        for btn, btn_info in zip(BUTTON_PINS, buttons):
            pin_obj = btn_info["pin"]
            reading = pin_obj.value()  # current raw pin state (0 = pressed, 1 = released if pull-up)
            # Debounce logic: check if reading is stable and different from current stable_state
            if reading != btn_info["stable_state"]:
                # State is different from last known stable state; increment counter
                btn_info["count"] += 1
                if btn_info["count"] >= STABLE_COUNT:
                    # State has been different for enough consecutive checks -> accept new state
                    btn_info["stable_state"] = reading
                    btn_info["count"] = 0
                    if reading == 0:
                        # Button is pressed (went from released->pressed)
                        if btn == btn_decrease:
                            # Decrease speed
                            speed -= 1
                            if speed < 0:
                                speed = 0  # prevent negative speed
                        elif btn == btn_increase:
                            # Increase speed
                            speed += 1
                        elif btn == btn_send:
                            # Send current speed over one of the UARTs (e.g., UART0)
                            msg_str = f"SPEED:{speed}"
                            send_message(msg_str.encode('ascii'), uart0)
                        elif btn == btn_reset:
                            # Reset statistics (clear history except current speed)
                            speed_history.clear()
                            speed_history.append(speed)
                            min_speed = speed
                            max_speed = speed
                            avg_speed = speed
                        elif btn == btn_clear:
                            # Clear message log
                            message_history.clear()
                        # Update speed history and stats for speed changes
                        if btn == btn_decrease or btn == btn_increase:
                            # Record new speed in history buffer
                            speed_history.append(speed)
                            if len(speed_history) > 20:
                                speed_history.pop(0)
                            # Recalculate min, max, avg
                            min_speed = min(speed_history)
                            max_speed = max(speed_history)
                            avg_speed = sum(speed_history) // len(speed_history)
                        # (No action on button release events in this implementation)
            else:
                # Reading matches the stable state; reset the counter
                btn_info["count"] = 0
        await asyncio.sleep_ms(DEBOUNCE_MS)  # check buttons every 20ms

async def display_task():
    """Task to update the TFT display with current speed stats and message history."""
    # Pre-calculate text line positions and heights
    line_height = font.HEIGHT  # font height in pixels (16 for vga1_16x16 font)
    # Determine base Y positions for each line of text on the display
    # We'll use lines 0-2 for speed stats, and lines 3-8 for message history (6 lines).
    while True:
        # Prepare the text lines for speed statistics
        speed_line = f"Speed: {speed}"
        stats_line = f"Min: {min_speed}   Max: {max_speed}"
        avg_line   = f"Avg: {avg_speed}"
        # Copy message history to avoid concurrency issues during iteration
        msgs = list(message_history)
        # Convert message bytes to string representation for display
        msg_lines = []
        for msg in msgs:
            # If messages were stored as bytes, decode for display
            try:
                text = msg.decode('ascii')  # decode as ASCII text
            except:
                # If not ASCII, show bytes in hex
                text = ' '.join(f'{b:02X}' for b in msg)
            msg_lines.append(text)
        # Limit to last 6 messages and pad with blanks if fewer than 6
        if len(msg_lines) > 6:
            msg_lines = msg_lines[-6:]
        while len(msg_lines) < 6:
            msg_lines.insert(0, "")  # insert blank at start so messages shift to bottom

        # Clear the relevant display area and draw each line of text
        # (We clear line by line to avoid flicker)
        # Draw speed stats (lines 0,1,2)
        display.fill_rect(0, 0, TFT_WIDTH, line_height, st7789.BLACK)
        display.text(font, speed_line, 0, 0, st7789.WHITE, st7789.BLACK)
        display.fill_rect(0, line_height, TFT_WIDTH, line_height, st7789.BLACK)
        display.text(font, stats_line, 0, line_height, st7789.WHITE, st7789.BLACK)
        display.fill_rect(0, 2*line_height, TFT_WIDTH, line_height, st7789.BLACK)
        display.text(font, avg_line, 0, 2*line_height, st7789.WHITE, st7789.BLACK)
        # Draw message history (lines 3 through 8)
        for i, msg_text in enumerate(msg_lines):
            y = (3 + i) * line_height
            display.fill_rect(0, y, TFT_WIDTH, line_height, st7789.BLACK)
            # If message line is empty, skip drawing text (it stays cleared)
            if msg_text:
                display.text(font, msg_text, 0, y, st7789.WHITE, st7789.BLACK)

        await asyncio.sleep_ms(200)  # update display ~5 times per second
        # (Adjust the sleep for faster or slower refresh as needed)

# ---------- Main Execution (setup tasks) ----------

async def main():
    """Main coroutine to start all tasks."""
    # Create tasks for UART receiving, button handling, and display update
    asyncio.create_task(uart_rx_task(uart0, "UART0"))
    asyncio.create_task(uart_rx_task(uart1, "UART1"))
    asyncio.create_task(button_task())
    asyncio.create_task(display_task())
    # Keep main alive indefinitely (since tasks are running forever)
    while True:
        await asyncio.sleep(1)

# Run the main coroutine, starting the event loop
asyncio.run(main())