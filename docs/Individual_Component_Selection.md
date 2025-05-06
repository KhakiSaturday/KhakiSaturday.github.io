---
Component Selection: HMI System

---

## Summary Table of Components

| Component Image    | Link and Cost    | Function    |
| ------------------ | ---------------- | ----------- |
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ESP32-S3-WROOM-1-N4.jpg?raw=true" width="200">|[ESP32-S3-WROOM-1-N4](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4/16162639) Cost:$2.95 USD| Micro Controller|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/4133screenadafruit.jpg?raw=true" width="200">|[2.0" 320x240 Color IPS TFT Display with microSD Card Breakout - ST7789 EYESPI](https://www.adafruit.com/product/4311) Cost:$19.95 USD| OLED Screen|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/LM2576-5.0WU-TR.jpg?raw=true" width="200">|[LM2576WU-TR](https://www.digikey.com/en/products/detail/microchip-technology/LM2576WU-TR/1121875)Cost:$1.79 USD| 3 Amp Switching Voltage Regulator|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ButtonADAFruitBlue.jpg?raw=true" width="200">|[Arcade Button with LED - 30mm Translucent Blue](https://www.adafruit.com/product/3490) Cost:$2.50 USD| Buttons for user input|

## Component Selection HMI System

### Role within Group
My role on the team is the HMI system. It is required that I have a screen and a control system on it for the end user to control. This will be done using an ESP32 to communicate with the board and my teammates' boards. The display will show data taken from teammates' systems and present them in graphical form (i.e. graph of average speed of ball over 10 second span).

### Micro Controller Selection
| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ESP32-S3-WROOM-1-N4.jpg?raw=true" width="200">[ESP32-S3-WROOM-1-N4](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4/16162639) Cost:$2.95 USD|Recommended by class/Has all of the pins I need/Affordable/Optimal processing power|Small form factor|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ESP32-S3-MINI-1U-N8.jpg?raw=true" width="200">[ESP32-S3-MINI-1U-N8](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-MINI-1U-N8/17728863) Cost:$3.10 USD|Has all of the pins I need and some more|Needs an additional antenna for wifi/Not worth the added hassle|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ESP32-S3-WROOM-1-N4R2.jpg?raw=true" width="200">[ESP32-S3-WROOM-1-N4R2](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4R2/16162643)Cost:$3.10 USD|ESP32-S3-WROOM-1-N4 with PS-RAM/has all the pins I need|It costs more than #1/I probably won’t end up using the PS-Ram|

Choice: ESP32-S3-WROOM-1-N4

Justification
When comparing the three options above I decided to go with option ESP32-S3-WROOM-1-N4. This is due to it being similar to the one we will be using in class. Thus it will be easier to troubleshoot since everyone in the class will have had some experience with it and makes getting it up and running easier. It is also the cheapest option out of the three, keeping it cheap is very important and means that I can splurge more on the buttons and the housing for the control system.

### Screen Selection

| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/4133screenadafruit.jpg?raw=true" width="200">[2.0" 320x240 Color IPS TFT Display with microSD Card Breakout - ST7789 EYESPI](https://www.adafruit.com/product/4311) Cost:$19.95 USD|BIG screen/premade libraries and examples for both I2C and SPI/good documentation on how it should be wired/has videos on how to code it|Cost is 1/3 of my budget/Data sheet is unconventional but still able to be comprehended/slow refresh rate|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/613516_005975_01_front_zoom.jpg?raw=true" width="200">[Adafruit 1.44" Color TFT LCD Display with MicroSD Card breakout - ST7735R](https://www.adafruit.com/product/2088)Cost:$14.95 USD| Can be seen from multiple different viewing angles without lose in image quality/ Has premade libraries and example code for I2C and SPI| Its an LCD screen/ Less value than the 2” version/ Slow refresh rate|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/MFG_NHD-1.8-160128UBC3_web(640x640).jpg?raw=true" width="200">[NHD-1.8-160128UBC3](https://www.digikey.com/en/products/detail/newhaven-display-intl/NHD-1-8-160128UBC3/23334148) Cost:$25.91 USD|It's an OLED/ Fulfills assignment criteria| No premade libraries with examples/ more expensive than the other two by at minimum five dollars/ Small screen size/ Slow refresh rate|

Choice: GRAPHIC DISPLAY TFT RGB 2"

Justification
I selected the GRAPHIC DISPLAY TFT RGB 2" due to its included libraries as they were a big reason for my choice. Having example code of how to get it up and running in the language we are using is a huge help, in combination with it having examples of communication through I2C and SPI is a massive bonus. In case one is harder than the other I can always swap over to the other. It also has a leg up on the competition as I already have approval on the screen, which makes it a guaranteed best choice.

### Voltage Regulator Selection

| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/LM2674MX33NOPB.jpg?raw=true" width="200">[LM2674MX-3.3/NOPB](https://www.digikey.com/en/products/detail/texas-instruments/LM2674MX-3-3-NOPB/366902) Cost:$3.37 USD|Few pins that need to be soldered/ Small Footprint| Decently expensive/ only provides 500mA/ 3 Volt Output/ Min Voltage range input of 6.5V|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/LM2576-5.0WU-TR.jpg?raw=true" width="200">[LM2576WU-TR](https://www.digikey.com/en/products/detail/microchip-technology/LM2576WU-TR/1121875)Cost:$1.79 USD| Cheap/ 3 amps which would be nice if I needed to add a component to my board/ Only 5 pins to solder/ Min Voltage range input of 4 Volts| Large Footprint|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/SC189ZSKTRT.jpg?raw=true" width="200">[SC189ZSKTRT](https://www.digikey.com/en/products/detail/semtech-corporation/SC189ZSKTRT/2182360) Cost:$1.89 USD| Only 6 pins/ space efficient|Incredibly small/Easy to lose/ Will be a headache|

Choice: LM2576WU-TR

Justification
I chose the LM2576WU-TR since it was the best “bang for your buck” option that I was able to find. The wide range it has for the input voltage and the extra 3 amps it's able to provide will be a huge help if I need to swap components last second. Its footprint also allows for it to be mounted partially off the side of the board for added space.

### Barrel Jack Selection

| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/PJ-102B.jpg?raw=true" width="200">[PJ-102B](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/PJ-102B/281307)Cost:$0.65 USD| 5 amp max current rating/Fulfills power requirements| One cent more than PJ-002BH|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/PJ-102A.jpg?raw=true" width="200">[PJ-102A](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/PJ-102A/275425)Cost:$0.65 USD| Fulfills power requirements| 2.5 amp max current rating|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/PJ-002BH.jpg?raw=true" width="200">[PJ-002BH](https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices/PJ-002BH/408447) Cost:$0.64 USD| 5 amp max current rating/ Fulfills power requirements/ Cheaper by 1 cent| It’s facing to the right|

Choice: PJ-002BH

Justification
I chose the PJ-002BH due to the price point being a cent less, as they say a penny saved is a penny earned. It also fullfills the power needs of my system.

### USB Micro B Connector
| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/MFG_USB3131-30-0230-A.jpg?raw=true" width="200">[USB3131-30-0230-A](https://www.digikey.com/en/products/detail/gct/USB3131-30-0230-A/9859642) Cost:$0.77 USD|Good size/ conforms to what other group member using esp32 is using/looks nice/ cheap| uses usb micro b|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/MUSB.jpg?raw=true" width="200">[MUSB-B5-S-VT-TSMT-T/R](https://www.digikey.com/en/products/detail/adam-tech/MUSB-B5-S-VT-TSMT-T-R/9832395?s=N4IgjCBcpgLFoDGUBmBDANgZwKYBoQB7KAbRACZYBOMAdggF0CAHAFyhAGVWAnASwB2AcxABfAgDYqCEMkjps%2BIqRCwADFQDMWkExBsO3fsLHiKKgK5YARrtFA) Cost:$1.27 USD|miniusb/cheap programming cables|expensive|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/1051330001.jpg?raw=true" width="200">[1051330001](https://www.digikey.com/en/products/detail/molex/1051330001/3313407) Cost:$1.05 USD|fits the needs of the project/ 5 contacts| uses usb micro b|

Choice:USB3131-30-0230-A

Justification
 The USB3131-30-0230-A was chosen for conformity with the other teammate using the esp32, this way if problems arise we are able to help eachother with getting USB Micro B port to work. It is also cheap and an effective USB Micro B port with only a bare minimum amount of pins required. The other two won't have the same in person support system taht the usb3131-30-0230-A will have.

### Buttons
| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ButtonADAFruitBlue.jpg?raw=true" width="200">[Arcade Button with LED - 30mm Translucent Blue](https://www.adafruit.com/product/3490) Cost:$2.50 USD|Good value per button/has option to light up/ cheap/ large size| will need large housing and said housing will need to be deep|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/adafruitwhitebutton.jpg?raw=true" width="200">[1187](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1187/6817192) Cost:$9.95 USD|Very large button size/ Can be seen from a mile away|Price|
|<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/MX2A-G1NB_web(640x640).jpg?raw=true" width="200">[MX2A-G1NB](https://www.digikey.com/en/products/detail/cherry-americas-llc/MX2A-G1NB/21738375) Cost:$1.75 USD|Cheapest of the 3/ gets the job done| WAY to small for the application this needs to be geared towards|

Choice:Arcade Button with LED - 30mm Translucent Blue

Justification
The button was chosen due to its large size and the five different color ways it had. Due to needing 5 different buttons for my system to control menuing, this is not only the best option to have board wise but also for readability and navigabiity of the device with each color being used for a different purpose. While the other buttons would work they are either to expensive or to small for the application these will be used for.

### Micro Controller Fact Sheet

| ESP32 Info           | Answer             |
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
| GPIO           |  45         | 12     | GPIO 2, GPIO9-13, GPIO 35-37, GPIO 41              |
| USB Programmer |  1          | 1      | GPIO19-GPIO20                                      |

### Power Budget
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/power%20budget%20HMI%20Hunter.JPG?raw=true">

The power budget was used to estimate how many amps would be needed to run my system both at max load and average load. I chose to go with a 3 amp switching regulator since I wanted to make sure that no matter what happened I wouldn't have to redesign my voltage regulator.
