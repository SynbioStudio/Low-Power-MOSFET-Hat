# Product Description:
The low-power MOSFET Hat is designed as an IO expander for actuating small DC devices (e.g. DC motors, pumps and valves). It uses I2C as the communication protocol enabling up to 8 boars to be used at once (i.e. 64 devices can be controlled simultaneously)!

# Warning:
Do not use devices that draw over 8 W per MOSFET. At 12 V this would 0.667 A per device. We have built a high-power version of this board, which can handle up to 150 W; for higher power device we would recommend using this alternate board. 

# Connecting the MOSFET Hat:
To connect the device, simply align the female inputs on the hat with the male outputs from the Raspberry Pi board or other hats which have been previously stacked on top of the board. Connect the board to a voltage source of your choosing. Maximum voltage is 24 V. Make sure to connect the power pins correctly; while there is reverse polarity protection, it is only reliably effective up to 12 V.

# Enabling I2C Devices:
On the desktop screen, click on the Raspberry Pi icon in the top left corner. Click on preferences and select Raspberry Pi Configuration. At the top of the screen, click on Interfaces. Make sure I2C is enabled by selecting the appropriate radio button. Click OK.

# Installing the Relevant Libraries:
Make sure you are connected to the internet. From your command line run the following command:
sudo pip3 install adafruit-circuitpython-mcp230xx

# Setting the I2C Address for the Driver Board:
Setting distinct I2C addresses will enable you to use multiple driver boards by simply stacking them. The default address in 0x20. Dip switches built into the board allow you to set the I2C address to 0x20 + binary number set by toggling the switches. From your command line run the following command:
	i2cdetect -y 1
Make sure you see the address which you have set appears on the output.
