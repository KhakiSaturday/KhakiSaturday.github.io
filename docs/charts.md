---
title: Diagrams and Charts
---
# Block Diagram
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/FinalizedBlockDiagramsmilever.jpg?raw=true">

## Block Diagram Conclusion
The philosphy I followed while making the block diagram was "what would get me all the points for the assignment". This unique visionary,bleeding edge,robust and culturally relevant philosophy allowed me to come up with the design above. The design implements a 5 buttons to for the user to control the device, alongside an esp32 to interpret said inputs. These inputs navigate the oled screen and will send messages to other subsystems. The system also features a switching 3 amp regulator, a boot button and a reset button. It also connects to a female usb B programmer so it is able to be coded. There are also rx tx lines to the 2 2x4 headers for daisy chain communication. With all of these features combiend it conforms to all requirements.

# Electrical Schematic V2
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/pcbschematic.png?raw=true">

# PCB Design

## Front of PCB
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/front_of_design.png?raw=true">

## Back of PCB
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/pcbback.png?raw=true">

## Manufactured/Assembled Front of PCB
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/FabricatedPCBFront.jpg?raw=true">

## Manufactured/Assembled Back of PCB
<img src="https://github.com/KhakiSaturday/KhakiSaturday.github.io/blob/main/Images/FabricatedPCBBack.jpg?raw=true">

### Design Requirement Fullfillment/Justification
The system fullfills the HMI requirement through the use of 5 buttons with one increasing the speed setting and one decreasing it. There are four speeds that can be set 0,1,2,3 and when the value is changed it sends a speed setting message to the actuator subsystem to change the strength of the magnet. Another one of the buttons displays all messages sent, recieved and passed through the system with the newest being at the top and those that don't fit on the screen being removed. The other two buttons are used to directly swap between a screen that displays the current speed, average speed(past 6), highest speed recorded, lowest speed recorded, and the speed setting. The current speed is sent from the sensors subsystem and transcribed when I receive it. I then calculate the values above in my code and update the display. The last and final button is used to reset the display. The requirements to display messages processed through the system is fullfilled alongside the user controlled input which sends out a message. I also fullfill the switching regulator by using a switching regulator (crazy, I know). The system is coded in micropython and uses an esp32-wroom-S3-N4 as the microcontroller, it also has a usb programmer and correctly connected header placing. As a result the system not only fullfills the requirements of the class, it also exceeds them.


### What Would I change on a theoretical 2.0 version
The first thing I would change would be a different, larger touch screen display. One of the biggest issues I ran into was coding my screen and getting it to work with the esp32 and micropython, it rsulted in a two week long battle with the hydra that is depricated libraries. A touchscreen with good documentation and proper libaries would result in an overall greater product/device for the end user. I would also make sure that all of the pins for the screen that needed an SPI line had an SPI line as the refresh rate of my screen is greatly hindered by software SPI. As a result it takes close to a full second for the screen to refresh leading to a curtain draw effect everytime it updates. I would also completely remove the buttons in favor of the touchscreen since it would allow for greater interactivity with the system as a whole. If I did keep the buttons, I would fully remake that section of the board as I had wired them incorrectly and as a result it was leaving the pins floating when the buttons hadn't been pressed. I would also choose to order my screen from a different site as I tried to order everything off of digikey and digikey doesn't have the greatest selection of screens available. Ordering off of sites a different site would have resulted in a larger screen at a cheaper price that would have also been touchscreen as well. Since the design is fully functional, for a 2.0 I would also greatly condense the board, the main reason I had the board so big was becuase I wanted to have the ability to completely remove a section of the board if I had to, since the system works there isn't a real need for it to be as large as it is. I would also change the 330uF capacitors, after repeatedly getting made fun of for how large they were I saw the error in my ways and would have chosen a smaller size if I had known of the ridicule I would face. A part of the device that I would change that would have a huge impact in its engagement would be the overall presentation of it. I would change it so that it is more inviting for children to use and engage with by makeing the design more colorful and make the speed change a lever or some other type of play element, having worked at an elementary school for a semester helping teach robotics and CAD to 5th and 6th graders, the most important thing you can have is play features and something that is bright and colorful. Making the application as interesting as possible is incredibly important. No kid wants to sit and listen to someone talk about how the electromagnet works. The solution is to present it in such a way that they have to engage with that knowledge to do something fun such as having a lever to turn the amperage up or a timing activity where they try to get the ball to go as fast around the track as possible by activating the electromagnets with push buttons. While such features would cause the project to massively exceed its budget, it would lead to an overall better design.