#Development Notes:
#Trying a library at https://github.com/amaork/libi2c
#   Adds I2C support in Python, hopefully for the Jetson TX1
#   Avoiding using C++ due to harder GUI.

#GUI for control of the 3D printed arm
#Jetson TX1 must be connected via I2C to the arduino uno, address 8, to
#control the hardware PWMs. 

from tkinter import *

#Servo Specs and Operation
#Servos for Joints 0, 1, 2, and 3 are mapped to GPIO pins 29, 31, 33, 35

def setDutyPWM0(newDuty):
    print("SetDutyPWM0 called")

def toHome():
    print("ToHome called")

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

sliders[0] = createSlider(master, "J0 Angle", 0, 180, 90, setDutyPWM0)
sliders[0].pack()
sliders[1] = createSlider(master, "J1 Angle", 0, 180, 90, setDutyPWM0)
sliders[1].pack()
sliders[2] = createSlider(master, "J2 Angle", 0, 180, 90, setDutyPWM0)
sliders[2].pack()
sliders[3] = createSlider(master, "J3 Angle", 0, 180, 90, setDutyPWM0)
sliders[3].pack()
sliders[4] = createSlider(master, "J4 Angle", 0, 180, 90, setDutyPWM0)
sliders[4].pack()
sliders[5] = createSlider(master, "J5 Angle", 0, 180, 90, setDutyPWM0)
sliders[5].pack()

##j1Scale = Scale(master,
##    label      = 'J1 servo pulse width (ms)',
##    from_      = ServoSpecs.pwmDutyMin,
##    to         = ServoSpecs.pwmDutyMax,
##    command    = setDutyPWM1,
##    digits     = 3,
##    resolution = 0.01,
##    length     = 500,
##    orient     = HORIZONTAL)
##j1Scale.set(ArmSpecs.homeDuties[1])
##j1Scale.pack()
##
##j2Scale = Scale(master,
##    label      = 'J2 servo pulse width (ms)',
##    from_      = ServoSpecs.pwmDutyMin,
##    to         = ServoSpecs.pwmDutyMax,
##    command    = setDutyPWM2,
##    digits     = 3,
##    resolution = 0.01,
##    length     = 500,
##    orient     = HORIZONTAL)
##j2Scale.set(ArmSpecs.homeDuties[2])
##j2Scale.pack()
##
##j3Scale = Scale(master,
##    label      = 'J3 (wrist) servo pulse width (ms)',
##    from_      = ServoSpecs.pwmDutyMin,
##    to         = ServoSpecs.pwmDutyMax,
##    command    = setDutyPWM3,
##    digits     = 3,
##    resolution = 0.01,
##    length     = 500,
##    orient     = HORIZONTAL)
##j3Scale.set(ArmSpecs.homeDuties[3])
##j3Scale.pack()

Button(master, text='To Home Position', command=toHome).pack()

mainloop()
#insert cleanup code here

