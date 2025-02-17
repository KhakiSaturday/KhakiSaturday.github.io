---
title: Individual Component Selection

---
## Component Selection HMI System

### Role within Group
My role on the team is the HMI system. It is required that I have a screen and a control system on it for the end user to control. This will be done using an ESP32 to communicate with the board and my teammates' boards. The display will show data taken from teammates' systems and present them in graphical form (i.e. graph of average speed of ball over 10 second span).

### Micro Controller Selection
| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ESP32-S3-WROOM-1-N4.jpg)[ESP32-S3-WROOM-1-N4](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4/16162639) Cost:$2.95 USD|Recommended by class/Has all of the pins I need/Affordable/Optimal processing power|Small form factor|
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ESP32-S3-MINI-1U-N8.jpg)[ESP32-S3-MINI-1U-N8](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-MINI-1U-N8/17728863) Cost:$3.10 USD|Has all of the pins I need and some more|Needs an additional antenna for wifi/Not worth the added hassle|
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ESP32-S3-WROOM-1-N4R2.jpg)[ESP32-S3-WROOM-1-N4R2](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4R2/16162643)Cost:$3.10 USD|ESP32-S3-WROOM-1-N4 with PS-RAM/has all the pins I need|It costs more than #1/I probably won’t end up using the PS-Ram|

### Selected Micro Controller ESP32-S3-WROOM-1-N4
### Justification
When comparing the Three options above I decided to go with option ESP32-S3-WROOM-1-N4. This is due to it being similar to the one we will be using in class. Thus it will be easier to troubleshoot since everyone in the class will have had some experience with it and makes getting it up and running easier. It is also the cheapest option out of the three, keeping it cheap is very important and means that I can splurge more on the buttons and the housing for the control system.

### Micro Controller Fact Sheet

| PIC18F24Q24 Info     |  Answer            |
| -------------------- | ------------------ |
| Model                | ESP32-S3-WROOM-1-N4|
| Product Page         | [Product Page](https://www.espressif.com/en/module/esp32-s3-wroom-1-en)        |
| Datasheet            | [Data Sheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf)        |
| Technical Reference| [Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf)        |
| Vendor               | [Vendor](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4/16162639)              |
| Code Examples        | [Code Examples](https://github.com/espressif/esp-idf/tree/master/examples)         |
| External Resources   | [External Resources](https://esp32io.com/tutorials/esp32-code-structure)    |
| Unit Cost            |  $2.95             |
| Max Current Entire IC| 500 mA             |
| Supply Voltage Range | 3.0-3.6 V          |
| Max GPIO Current(pin)| 40mA               |
| Support External Interupts| Yes                |
| Required Programming,Hardware cost,url| Can be programmed over USB               |


### Micro Controller Pin Usage Table
| Module         | # Available | Needed | Associated Pins                                    |
| -------------- | ----------- | ------ | -------------------------------------------------- |
| Power          |  2          | 2      | EN, 3V3                                            |
| Ground         |  2          | 2      | GND, GND                                           |
| UART           |  3          | 2      | GPIO17-GPIO18, GPIO43-GPIO44                       |
| External SPI   |  4          | 4      | GPIO26-GPIO32, GPIO33-GPIO37, GPIO9-GPIO14, GPIO38 |
| I2C            |  2          | 0      | Can Be Choosen Via Pin Matrix                      |
| GPIO           |  45         | 5      | *                                                  |
| Motor PWM      |  0          | 0      | N/A                                                |
| USB Programmer |  1          | 1      | GPIO19-GPIO20                                      |



| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/4133screenadafruit.jpg)[2.0" 320x240 Color IPS TFT Display with microSD Card Breakout - ST7789 EYESPI](https://www.adafruit.com/product/4311) Cost:$19.95 USD|BIG screen/premade libraries and examples for both I2C and SPI/good documentation on how it should be wired/has videos on how to code it|Cost is 1/3 of my budget/Data sheet is unconventional but still able to be comprehended/slow refresh rate|
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/613516_005975_01_front_zoom.jpg)[Adafruit 1.44" Color TFT LCD Display with MicroSD Card breakout - ST7735R](https://www.adafruit.com/product/2088)Cost:$14.95 USD| Can be seen from multiple different viewing angles without lose in image quality/ Has premade libraries and example code for I2C and SPI| Its an LCD screen/ Less value than the 2” version/ Slow refresh rate|
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/MFG_NHD-1.8-160128UBC3_web(640x640).jpg)[NHD-1.8-160128UBC3](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-MINI-1U-N8/17728863) Cost:$25.91 USD|It's an OLED/ Fulfills assignment criteria| No premade libraries with examples/ <ore expensive than the other two by at minimum five dollars/ Small screen size/ Slow refresh rate|

### Component Selected: GRAPHIC DISPLAY TFT RGB 2"

### Justification
I selected the GRAPHIC DISPLAY TFT RGB 2" due to its included libraries as they were a big reason for my choice. Having example code of how to get it up and running in the language we are using is a huge help, in combination with it having examples of communication through I2C and SPI is a massive bonus. In case one is harder than the other I can always swap over to the other. It also has a leg up on the competition as I already have approval on the screen, which makes it a guaranteed best choice.


| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/4133screenadafruit.jpg)[2.0" 320x240 Color IPS TFT Display with microSD Card Breakout - ST7789 EYESPI](https://www.adafruit.com/product/4311) Cost:$19.95 USD|BIG screen/premade libraries and examples for both I2C and SPI/good documentation on how it should be wired/has videos on how to code it|Cost is 1/3 of my budget/Data sheet is unconventional but still able to be comprehended/slow refresh rate|
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/613516_005975_01_front_zoom.jpg)[Adafruit 1.44" Color TFT LCD Display with MicroSD Card breakout - ST7735R](https://www.digikey.com/en/products/detail/microchip-technology/LM2576-5-0WU-TR/1027688)Cost:$14.95 USD| Can be seen from multiple different viewing angles without lose in image quality/ Has premade libraries and example code for I2C and SPI| Its an LCD screen/ Less value than the 2” version/ Slow refresh rate|
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/SC189ZSKTRT.jpg)[SC189ZSKTRT](https://www.digikey.com/en/products/detail/semtech-corporation/SC189ZSKTRT/2182360) Cost:$1.89 USD| Only 6 pins/ Space efficient
| Incredibly small/Easy to lose/ Will be a headache|




