#import the necessary modules for the I2C connection
import board
import busio
from digitalio import Direction
from adafruit_mcp230xx.mcp23008 import MCP23008

#enable time.sleep() function
import time

# Initialize the I2C bus:
i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23008(i2c, address=0x21)  # create an instance of MCP23008 and select the I2C address
pin0 = mcp.get_pin(0) #create an instance of the pin you wish to address. You can set the number within parentheses from 0 to 7 to select a MOSFET on the hat.

# Set up pin0 as an output pin
pin0.direction = Direction.OUTPUT

# Blink pin 0 on and then off forever
while True:
    pin0.value = True
    time.sleep(1)
    pin0.value = False
    time.sleep(1)
