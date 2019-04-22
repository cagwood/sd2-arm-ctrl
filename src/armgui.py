#Development Notes:
#Found a simple python library for general I2C on linux.
#https://github.com/vitiral/i2cdev
#to install, use the following command on linux:
##  pip install i2cdev

#GUI for control of the 3D printed arm
#Jetson TX1 must be connected via I2C to the arduino uno, address 8, to
#control the hardware PWMs. 

from tkinter import *
from i2cdev  import I2C

#I2C Setup
ardAddr = 0x08
ardBus  = 1
#I2C parts commented out due to permissions denied
i2c = I2C(ardAddr, ardBus)

#Servo Specs and Operation
#Servos for Joints 0, 1, 2, and 3 are mapped to GPIO pins 29, 31, 33, 35
class Arm:
    home = [90, 150, 20, 0, 0, 0]

#Functions 
def setAngle(jointNum, newAngle):
    data = bytes([jointNum, int(newAngle)])
    i2c.write(data)

def toHome():
    data = bytes([0, Arm.home[0],
                  1, Arm.home[1],
                  2, Arm.home[2],
                  3, Arm.home[3],
                  4, Arm.home[4],
                  5, Arm.home[5]])
    i2c.write(data)
 

#Slider callbacks
def j0slide(val):
    setAngle(0, val)
def j1slide(val):
    setAngle(1, val)
def j2slide(val):
    setAngle(2, val)
def j3slide(val):
    setAngle(3, val)
def j4slide(val):
    setAngle(4, val)
def j5slide(val):
    setAngle(5, val)

#UI
master = Tk()
master.title("Arm Controller")
def createSlider(master, label, mini, maxi, init, onChange):
    slider = Scale(master,
                   label      = label,
                   from_      = mini,
                   to         = maxi,
                   command    = onChange,
                   digits     = 3,
                   resolution = 0.01,
                   length     = 500,
                   orient     = HORIZONTAL)
    slider.set(init)
    return slider

sliders = []
for num in range(6):
    sliders.append(Scale)

sliders[0] = createSlider(master, "J0 Angle", 0, 180, Arm.home[0], j0slide)
sliders[0].pack()
sliders[1] = createSlider(master, "J1 Angle", 0, 180, Arm.home[1], j1slide)
sliders[1].pack()
sliders[2] = createSlider(master, "J2 Angle", 0, 180, Arm.home[2], j2slide)
sliders[2].pack()
sliders[3] = createSlider(master, "J3 Angle", 0, 180, Arm.home[3], j3slide)
sliders[3].pack()
sliders[4] = createSlider(master, "J4 Angle", 0, 180, Arm.home[4], j4slide)
sliders[4].pack()
sliders[5] = createSlider(master, "J5 Angle", 0, 180, Arm.home[5], j5slide)
sliders[5].pack()

Button(master, text='To Home Position', command=toHome).pack()

mainloop()
#insert cleanup code here

