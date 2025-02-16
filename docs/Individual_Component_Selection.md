---
title: Individual Component Selection

---
## Component Selection HMI System

### Role within Group
My role on the team is the HMI system. It is required that I have a screen and a control system on it for the end user to control. This will be done using an ESP32 to communicate with the board and my teammates' boards.The display will show data taken from teammates' boards and will present it in a “good on the eyes” fashion while still keeping it strictly to what is neccesary. 
### Micro Controller Selection
| Components         |  Pros       |  Cons       |
| ------------------ | ----------- | ----------- |
|![](https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/ESP32-S3-WROOM-1-N4.jpg)[ESP32-S3-WROOM-1-N4](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4/16162639)| / Recommended by class/has all of the pins I need/affordable/just the right amount of processing power|small form factor|
|![](https://github.com/NBrentASU/NBrent/blob/main/PIC2.png?raw=true)[PIC18F27Q10 (SOIC/28)](https://www.microchip.com/en-us/product/pic18f27q10#Documentation)| 7.5x17.9mm / Most pins will be used, minimizing excess soldering / Easier soldering / 128K Bytes (Flash) / 1k EEPROM | More pins per side / If a requirement is overlooked now, little to no extra pins to fix it / 31 Deep Hardware Stack / 3.6K SRAM / Confusing documentation regarding pins |
|![](https://github.com/NBrentASU/NBrent/blob/main/PIC3.png?raw=true)[PIC18F24Q24 (SOIC/28)](https://www.microchip.com/en-us/product/pic18f24q24#Documentation)| 7.5x17.9mm / Most pins will be used, minimizing excess soldering / Easier soldering / 128 Deep Hardware Stack / 4K SRAM / Better information for my use case | More pins per side / If a requirement is overlooked now, little to no extra pins to fix it / 64K Bytes (Flash) / 500 EEPROM |



### Micro Controller Fact Sheet


### Micro Controller Pin Usage Table