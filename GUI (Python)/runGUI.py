import tkinter as tk
from PIL import Image, ImageTk
import random
# this is a test  nbhbh
# PIXEL FORMATTING
# Used to adjust pixel coordinates of frames and labels.
HEIGHT=750
WIDTH=1200
OFFSET=35
VALUE_OFFSET = 80
UNIT_OFFSET = 90
LABEL_BEGIN_X = 190
LABEL_BEGIN_Y = 70
COL1 = 0
COL2 = 450
COL3 = 820

# IMAGE PIXEL SIZE REFERENCE
LOGO_HEIGHT=166
LOGO_WIDTH=373
ICON_HEIGHT=40
ICON_WIDTH=40

# UPDATE RANDOM NUMBER TEST
# Tests to see if label values can change without issues.
REFRESH_RATE = 50   # Measured in milliseconds
MIN_FLOAT = 0.0
MAX_FLOAT = 300.0
DIGITS = 2
normalUnitArray = []
for i in range(19):
    normalUnitArray.append(12.34)
    # Initialize / populate the array.
    # If label value shows 12.34, then update / refresh failed.


# INITIALIZATION
# Creation of the program(root) and its workspace(main_canv).
root = tk.Tk()
root.resizable(False, False)
main_canv = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black',highlightthickness=0)
main_canv.pack()


# IMAGE / ICON FILE PATHS
# Hyperloop Logo courtesy of Cal Poly Pomona Hyperloop Club.
# Icons courtesy of FreePik.com.
hyperloop_logo = tk.PhotoImage(file='images\\hyperloop\\hyperloop_logo_scale25.png')
battery_icon = tk.PhotoImage(file='images\\icons\\battery.png')
com_icon = tk.PhotoImage(file='images\\icons\\com.png')
kin_icon = tk.PhotoImage(file='images\\icons\\kin.png')
pod_icon = tk.PhotoImage(file='images\\icons\\pod.png')
time_icon = tk.PhotoImage(file='images\\icons\\time.png')
motor_icon = tk.PhotoImage(file='images\\icons\\motor.png')
progress_icon = ImageTk.PhotoImage(file='images\\icons\\progress.png')

# HYPERLOOP LOGO
# Creates and adds Hyperloop Logo to the workspace.
title_logo_canv = tk.Canvas(main_canv, width=LOGO_WIDTH, height=LOGO_HEIGHT, highlightthickness=0)
title_logo_canv.place(relx=0, rely=0, anchor='nw')
title_logo_canv.create_image(0,0,anchor='nw',image=hyperloop_logo)

# TITLES WITH ICON
# Simplifies positioning of title and icon.
class tkTitle:
    def __init__(self, master=root, title='Text', iconpos=0.2, titlepos=0.6, icon=battery_icon):
        self.title = tk.Label(master, text=title, bg="black", fg='white', font=('Helvetica',20,'bold'), pady=5)
        self.title.place(relx=titlepos, rely=0, anchor='n')

        self.icon = tk.Canvas(master, width=ICON_WIDTH, height=ICON_HEIGHT, highlightthickness=0)
        self.icon.place(relx=iconpos, rely=0, anchor='n')
        self.icon.create_image(0,0,anchor='nw', image=icon)

# LABELS WITH UNITS
# Simplifies positioning of labels, values, and units.
class tkLabelUnit:
    def __init__(self, master=root, str='text', val=0.01, unit='m', list=0, offsetX=0):
        self.label = tk.Label(master, text=str, bg='black', fg='white', font=('Courier',12,'bold'), justify='right')
        self.label.place(x=LABEL_BEGIN_X+offsetX, y=LABEL_BEGIN_Y+list*OFFSET, anchor='ne')

        self.value = tk.Label(master, text=val, bg='black', fg='white', font=('Courier',12,), justify='right')
        self.value.place(x=LABEL_BEGIN_X+VALUE_OFFSET+offsetX,y=LABEL_BEGIN_Y+list*OFFSET, anchor='ne')

        self.unit = tk.Label(master, text=unit, bg='black', fg='white', font=('Courier',12,'bold'),justify='left')
        self.unit.place(x=LABEL_BEGIN_X+UNIT_OFFSET+offsetX,y=LABEL_BEGIN_Y+list*OFFSET, anchor='nw')

# UPDATE FUNCTION
# Will assign random numbers to values whenever called.
def updateRandValues():
    transSpeed.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    motorSpeed_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    motorVoltage_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    motorCurrent_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    motorTemp1_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    motorTemp2_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    motorTemp3_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    motorTemp4_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    pressure_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    rideHeight_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    distance_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    velocity_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    acceleration_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    batteryVoltage_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    batteryCurrent_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    batteryTemp1_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    batteryTemp2_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    batteryTemp3_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)
    batteryTemp4_Label.value['text'] = round(random.uniform(MIN_FLOAT, MAX_FLOAT), DIGITS)

    # Recursive function to update values.
    root.after(REFRESH_RATE, updateRandValues)


# totally useful function.
def dispNothing():
    print('Nothing')


# TIME
# Creates workspace for all time elements.
# Set bg to 'blue' in time_canv to see the extent of the workspace.
TIME_HEIGHT=150
TIME_WIDTH=400
time_canv = tk.Canvas(main_canv, width=TIME_WIDTH, height=TIME_HEIGHT, highlightthickness=0, bg='black')    
time_canv.place(x=COL1, y=LOGO_HEIGHT+25, anchor='nw')

timeTitle = tkTitle(master=time_canv, title="Time", iconpos=0.35, titlepos=0.55, icon=time_icon)

elapse_label = tk.Label(time_canv, text='Time Elapsed:', bg='black', fg='white', font=('Courier',12,'bold'),justify='right')
elapse_label.place(x=LABEL_BEGIN_X+20,y=LABEL_BEGIN_Y, anchor='ne')
elapse_value = tk.Label(time_canv, text='00:00:00', bg='black', fg='white', font=('Courier',12,), justify='left')
elapse_value.place(x=LABEL_BEGIN_X+20 + 10,y=LABEL_BEGIN_Y)

estimate_label = tk.Label(time_canv, text='Expected Run Time:', bg='black', fg='white', font=('Courier',12,'bold'),justify='right')
estimate_label.place(x=LABEL_BEGIN_X+20,y=LABEL_BEGIN_Y + OFFSET, anchor='ne')
estimate_value = tk.Label(time_canv, text='00:00:00', bg='black', fg='white', font=('Courier',12), justify='left')
estimate_value.place(x=LABEL_BEGIN_X+20 + 10,y=LABEL_BEGIN_Y + OFFSET)

# COMMUNICATIONS
# Creates workspace for all communication elements.
# Set bg to 'blue' in com_canv to see the extent of the workspace.
COM_HEIGHT=225
COM_WIDTH=400
com_canv = tk.Canvas(main_canv, width=COM_WIDTH, height=COM_HEIGHT, highlightthickness=0, bg='black')   
com_canv.place(x=COL1, y=LOGO_HEIGHT+TIME_HEIGHT+35, anchor='nw')

comLabel = tkTitle(master=com_canv, title="Communication", iconpos=0.225, titlepos=0.6, icon=com_icon)

pod_com_label = tk.Label(com_canv, text='Pod Connection:', bg='black', fg='white', font=('Courier',12,'bold'),justify='right')
pod_com_label.place(x=LABEL_BEGIN_X+20,y=LABEL_BEGIN_Y, anchor='ne')
pod_com_value = tk.Label(com_canv, text='ESTABLISHED', bg='black', fg='GREEN', font=('Courier',12,'bold'), justify='left')
pod_com_value.place(x=LABEL_BEGIN_X+20 + 10,y=LABEL_BEGIN_Y)

spacex_com_label = tk.Label(com_canv, text='SpaceX Connection:', bg='black', fg='white', font=('Courier',12,'bold'),justify='right')
spacex_com_label.place(x=LABEL_BEGIN_X+20,y=LABEL_BEGIN_Y + OFFSET, anchor='ne')
spacex_com_value = tk.Label(com_canv, text='NOT ESTABLISHED', bg='black', fg='RED', font=('Courier',12,'bold'), justify='left')
spacex_com_value.place(x=LABEL_BEGIN_X+20 + 10,y=LABEL_BEGIN_Y + OFFSET)

transSpeed = tkLabelUnit(master=com_canv, str="Transfer Speed:", val=normalUnitArray[0], unit='Mb/s', list=2, offsetX=20)

# MOTOR
# Creates workspace for all motor elements.
# Set bg to 'blue' in motor_canv to see the extent of the workspace.
MOTOR_HEIGHT=320
MOTOR_WIDTH=400
motor_canv = tk.Canvas(main_canv, width=MOTOR_WIDTH, height=MOTOR_HEIGHT, highlightthickness=0, bg='black') 
motor_canv.place(x=COL2, y=20, anchor='nw')

motorTitle = tkTitle(master=motor_canv, title="Motor", iconpos=0.33, titlepos=0.56, icon=motor_icon)

motorSpeed_Label = tkLabelUnit(master=motor_canv, str='Motor Speed:', val=normalUnitArray[1], unit='RPM', list=0)
motorVoltage_Label = tkLabelUnit(master=motor_canv, str='Voltage IN:', val=normalUnitArray[2], unit='V', list=1)
motorCurrent_Label = tkLabelUnit(master=motor_canv, str='Current:', val=normalUnitArray[3], unit='A', list=2)
motorTemp1_Label = tkLabelUnit(master=motor_canv, str='Motor 1 Temp:', val=normalUnitArray[4], unit='°C', list=3)
motorTemp2_Label = tkLabelUnit(master=motor_canv, str='Motor 2 Temp:', val=normalUnitArray[5], unit='°C', list=4)
motorTemp3_Label = tkLabelUnit(master=motor_canv, str='Motor 3 Temp:', val=normalUnitArray[6], unit='°C', list=5)
motorTemp4_Label = tkLabelUnit(master=motor_canv, str='Motor 4 Temp:', val=normalUnitArray[7], unit='°C', list=6)


# POD
# Creates workspace for physical elements of the pod.
# Set bg to 'blue' in pod_canv to see the extent of the workspace.
POD_HEIGHT=160
POD_WIDTH=400
pod_canv = tk.Canvas(main_canv, width=POD_WIDTH, height=POD_HEIGHT, highlightthickness=0, bg='black')   
pod_canv.place(x=COL3, y=20, anchor='nw')

podTitle = tkTitle(master=pod_canv, title="Pod", iconpos=0.35, titlepos=0.55, icon=pod_icon)

pressure_Label = tkLabelUnit(master=pod_canv, str='Pressure:', val=normalUnitArray[8], unit='kPa', list=0)
rideHeight_Label = tkLabelUnit(master=pod_canv, str='Ride Height:', val=normalUnitArray[9], unit='cm', list=1)

# KINEMATICS
# Creates workspace for all motion related elements.
# Set bg to 'blue' in kin_canv to see the extent of the workspace.
KIN_HEIGHT=200
KIN_WIDTH=400
kin_canv = tk.Canvas(main_canv, width=KIN_WIDTH, height=KIN_HEIGHT, highlightthickness=0, bg='black')   
kin_canv.place(x=COL2, y=MOTOR_HEIGHT+40, anchor='nw')

kinematicTitle = tkTitle(master=kin_canv, title="Kinematics", iconpos=0.265, titlepos=0.575, icon=kin_icon)

distance_Label = tkLabelUnit(master=kin_canv, str='Distance Traveled:', val=normalUnitArray[10], unit='km', list=0)
velocity_Label = tkLabelUnit(master=kin_canv, str='Pod Speed:', val=normalUnitArray[11], unit='km/h', list=1)
acceleration_Label = tkLabelUnit(master=kin_canv, str='Acceleration:', val=normalUnitArray[12], unit='km/h²', list=2)

# BATTERY
# Creates workspace for elements relating to battery management.
# Set bg to 'blue' in bat_canv to see the extent of the workspace.
BAT_HEIGHT=300
BAT_WIDTH=400
bat_canv = tk.Canvas(main_canv, width=BAT_WIDTH, height=BAT_HEIGHT, highlightthickness=0, bg='black')   
bat_canv.place(x=COL3, y=POD_HEIGHT+50, anchor='nw')

batteryTitle = tkTitle(master=bat_canv, title="Battery", iconpos=0.34, titlepos=0.56, icon=battery_icon)

batteryVoltage_Label = tkLabelUnit(master=bat_canv, str='Voltage:', val=normalUnitArray[13], unit='V', list=0)
batteryCurrent_Label = tkLabelUnit(master=bat_canv, str='Current:', val=normalUnitArray[14], unit='A', list=1)
batteryLife_Label = tkLabelUnit(master=bat_canv, str='Battery Life:', val=0.01, unit='%', list=2)
batteryTemp1_Label = tkLabelUnit(master=bat_canv, str='Pack 1 Temp:', val=normalUnitArray[15], unit='°C', list=3)
batteryTemp2_Label = tkLabelUnit(master=bat_canv, str='Pack 2 Temp:', val=normalUnitArray[16], unit='°C', list=4)
batteryTemp3_Label = tkLabelUnit(master=bat_canv, str='Pack 3 Temp:', val=normalUnitArray[17], unit='°C', list=5)
batteryTemp4_Label = tkLabelUnit(master=bat_canv, str='Pack 4 Temp:', val=normalUnitArray[18], unit='°C', list=6)


# hello ceasar
# hello brendt
# hello bryce
# its me, myron


# POD PROGRESS
# Creates workspace for the progress bar of the pod.
# Set bg to 'blue' in prog_canv to see the extent of the workspace.
PROG_HEIGHT=200
PROG_WIDTH=750
PROG_OFFSET = 25
LINE_HEIGHT = PROG_HEIGHT/2
LINE_START_X = 100
LINE_END_X = PROG_WIDTH-100

# Progress position is dependent on distance.
PERCENTAGE = 0.2641354
PROGRESS_X = int(round(PERCENTAGE * (LINE_END_X - LINE_START_X)))

prog_canv = tk.Canvas(main_canv, width=PROG_WIDTH, height=PROG_HEIGHT, highlightthickness=0, bg='black')    
prog_canv.place(x=0, y=LOGO_HEIGHT+TIME_HEIGHT+COM_HEIGHT, anchor='nw')

progTitle = tk.Label(prog_canv, text='Pod Progess', bg='black', fg='white', font=('Helvetica',16,'bold'), pady=5)
progTitle.place(relx=0.05,rely=0.1, anchor='nw')
prog_canv.create_line(LINE_START_X,LINE_HEIGHT,LINE_END_X,LINE_HEIGHT,fill='white', width=5)

startLabel = tk.Label(prog_canv, text='START', bg='black', fg='white', font=('Courier',12,'bold'), pady=5)
startLabel.place(x=LINE_START_X, y=LINE_HEIGHT + PROG_OFFSET, anchor='n')
endLabel = tk.Label(prog_canv, text='END', bg='black', fg='white', font=('Courier',12,'bold'), pady=5)
endLabel.place(x=LINE_END_X, y=LINE_HEIGHT + PROG_OFFSET, anchor='n')

progressIcon = tk.Canvas(prog_canv, width=ICON_WIDTH, height=ICON_HEIGHT, highlightthickness=0,bg="black")
progressIcon.place(x=LINE_START_X+PROGRESS_X,y=LINE_HEIGHT,anchor='center')
progressIcon.create_image(0,0,anchor='nw', image=progress_icon)


# BUTTONS / CONTROL
# Creates workspace for buttons.
# Set bg to 'blue' in control_canv to see the extent of the workspace.
# Buttons will send commands to the pod.
CONTROL_HEIGHT = 200
CONTROL_WIDTH = WIDTH - PROG_WIDTH
control_canv = tk.Canvas(main_canv, width=CONTROL_WIDTH, height=CONTROL_HEIGHT, highlightthickness=0, bg='black')   
control_canv.place(x=PROG_WIDTH, y=LOGO_HEIGHT+TIME_HEIGHT+COM_HEIGHT, anchor='nw')

brakeButton = tk.Button(control_canv, text="BRAKES", font=('Courier',18,'bold'), command=dispNothing, justify='center', padx=40, pady=10, bg='black', fg='red')
brakeButton.place(relx=0.25,rely=0.40,anchor='center')
brakeLabel = tk.Label(control_canv, text='Brake Status:', bg='black', fg='white', font=('Courier',12,'bold'),justify='center')
brakeLabel.place(relx=0.25,rely=0.65, anchor='center')
brakeStatus = tk.Label(control_canv, text='DISENGAGED', bg='black', fg='GREEN', font=('Courier',12,'bold'),justify='center')
brakeStatus.place(relx=0.25,rely=0.8, anchor='center')

powerButton = tk.Button(control_canv, text="POWER", font=('Courier',18,'bold'), command=dispNothing, justify='center', padx=40, pady=10, bg='black', fg='red')
powerButton.place(relx=0.75,rely=0.40,anchor='center')
powerLabel = tk.Label(control_canv, text='Power Status:', bg='black', fg='white', font=('Courier',12,'bold'),justify='center')
powerLabel.place(relx=0.75,rely=0.65, anchor='center')
powerStatus = tk.Label(control_canv, text='POWER ON', bg='black', fg='GREEN', font=('Courier',12,'bold'),justify='center')
powerStatus.place(relx=0.75,rely=0.8, anchor='center')


# UPDATE / REFRESH
# This is start calling the update function which is recursive.
# The recursion is essentially the update / represh.
root.after(REFRESH_RATE, updateRandValues)

# END
root.mainloop()