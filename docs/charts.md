---
title: Diagrams and Charts
---
# Block Diagram
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/Hunter_Hassebroek_Block%20Diagram-314_Team_310%20(1).jpg?raw=true">

# Electrical Schematic V1
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/pcbschematic.png?raw=true">

# PCB Design

## Front of PCB
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/front_of_design.png?raw=true">

## Back of PCB
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/pcbback.png?raw=true">

# Why the design is the goat
The system fullfills the HMI requirement through the use of 5 buttons with one increasing the speed setting and one decreasing it. There are four speeds that can be set 0,1,2,3 and when the value is changed it sends a speed setting message to the actuator subsystem to change the strength of the magnet. Another one of the buttons displays all messages sent, recieved and passed through the system with the newest being at the top and those that don't fit on the screen being removed. The other two buttons are used to directly swap between a screen that displays the current speed, average speed(past 6), highest speed recorded, lowest speed recorded, and the speed setting. The current speed is sent from the sensors subsystem and transcribed when I receive it. I then calculate the values above in my code and update the display. The last and final button is used to reset the display. The requirements to display messages processed through the system is fullfilled alongside the user controlled input which sends out a message. I also fullfill the switching regulator by using a switching regulator (crazy, I know). The system is coded in micropython and uses an esp32-wroom-S3-N4 as the microcontroller, it also had a usb programmer and correctly connected header placing. As a result the system not only fullfills the requirements of the class, it also exceeds them.