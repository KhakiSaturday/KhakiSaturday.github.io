---
title: HMI API
---
## Message Structure

Start Byte (2 uint8_t)

Sender Address (uint8_t)

Receiver Address (uint8_t)

Message Type (uint8_t)

Message (1-56 uint8_t)

Stop Byte (2 uint8_t)

## Team Definitions

### Team Bytes

| Type |  Byte  |
| -----------| ----------- |
| Start | AZ  |
| Stop | YB |

### Team Addresses

| Name |  Address  |
| -----------| ----------- |
| Noah Brent | N  |
|Evan Skinner| E |
|Kirk Volin| K |
|Hunter Hassebroek| H |
| Broadcast | X |

### Recieved Messages
All are (uint8_t).

| Message Type | Message Byte 1-2 <br> Message Prefix | Byte 3 <br> Sender ID | Byte 4 <br> Receiver ID | Byte 5 <br> Data Type | Byte 6 <br> Data Value| Byte 7-8 |
|----------|---------------|--------|-----------|--------|--| --|
| 5 | Prefix (AZ)| MQTT ID (K)| HMI ID (H)| Master Reset(R) | Reset(1) | Suffix (YB) |
| 6 | Prefix (AZ)| MQTT ID (K)| HMI ID (H)| MQTT Connection(W) | MQTT Connection(0-1)) | Suffix (YB) |
| 1 | Prefix (AZ)| Sensor ID (E)| HMI ID (H)| Ball Speed (V) | Ball Speed (0-100) | Suffix (YB) |

## Sent Messages

All are (uint8_t).

| Message Type | Message Byte 1-2 <br> Message Prefix | Byte 3 <br> Sender ID | Byte 4 <br> Receiver ID | Byte 5 <br> Data Type | Byte 6 <br> Data Value| Byte 7-8 |
|----------|---------------|--------|-----------|--------|--| --|
| 7 | Prefix (AZ)| HMI ID (H)| Actuator ID (N)| Speed (S) | Speed Setting (0-3) | Suffix (YB) |
| 8 | Prefix (AZ)| HMI ID (H)| Broadcast ID (X)| Error (F) | Error Message (0-5) | Suffix (YB) |

Error Types:

0: Incorrect / No Start Bit

1: Incorrect / No Address Bit

2: Incorrect / No Message Type

3: Incorrect / No Stop Bit

4: Incorrect Data Value in Valid Message

5: Bytes per Message Overflow

## Message handling 
### HMI message handling protocol
1.  Identify the start of a message and begin copying it to an array for retransmission.
2.  When receiver identified either
  
    2a. If not mine, finish copying to retransmission array then retransmit

    2b. If mine, continue to step 3

    2c. If broadcast byte, copy to retransmit array, retransmit, and continue to step 3
    
 3. Identify message type
 4. Interpret message data and apply as specified
 5. Trash message
 6. Transmit relevant data
 7. When new message is received go back to step 1

Each step has an error check to make sure that things are proceeding smoothly, if it fails, the error code and the address it was transmitted from will be transmitted.

To elaborate on step 6 and error handling

## Error handling and Transmission
1. Whenever an interruptive event occurs (ie switching info every second, error, or reset) begin construction of message in array
2. To a temporary array, begin by adding start bytes and my address byte
3. Then add receiving address which in most cases will be MQTT, HMI, or broadcast
4. Add message type byte based on messaging protocols above
5. Complete message by adding data then capping with stop bytes
6. Check if already transmitting, if so wait for transmission to end and delay then send
7. Otherwise send
8. Trash temporary sending array



