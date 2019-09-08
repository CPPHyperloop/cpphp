# THIS FILE IS NOT MEANT FOR RELEASE.
# THIS FILE IS MEANT FOR TESTING AN IDEA BEFORE ACTUAL IMPLEMENTATION.

import tkinter as tk
import random
import time

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
REFRESH_RATE = 25

hrs = 2
mins = 52
secs = 42
ms = 56
timeformat = '{:02d}:{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs, ms)
t0 = time.time()

'''def startCount():
    t = 0
    while True:
        mins, secs = divmod(x,60)
        mins = round(mins)
        secs = round(secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t += 1'''

root = tk.Tk()
root.resizable(False, False)
main_canv = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='black',highlightthickness=0)
main_canv.pack()

def func():
        t1 = time.time() 
        nowtime = (t1-t0) + (59*60)+57
        ms = int((nowtime*100)%100)
        secs = int(nowtime % 60)
        mins = int((nowtime/60)%60)
        hrs = int(nowtime/3600)
        timeformat = '{:02d}:{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs, ms)
        val['text']=timeformat
        root.after(REFRESH_RATE,func)

lab = tk.Label(main_canv, text="Time:", bg='black', fg='white', font=('Courier',12,'bold'), justify='right')
lab.place(relx=0.2, rely=0.5, anchor='center')

val = tk.Label(main_canv, text=timeformat, bg='black', fg='white', font=('Courier',12,'bold'), justify='right')
val.place(relx=0.8, rely=0.5, anchor='center')


print(timeformat)

'''self.label = tk.Label(master, text=str, bg='black', fg='white', font=('Courier',12,'bold'), justify='right')
        self.label.place(x=LABEL_BEGIN_X+offsetX, y=LABEL_BEGIN_Y+list*OFFSET, anchor='ne')

        self.value = tk.Label(master, text=val, bg='black', fg='white', font=('Courier',12,), justify='right')
        self.value.place(x=LABEL_BEGIN_X+VALUE_OFFSET+offsetX,y=LABEL_BEGIN_Y+list*OFFSET, anchor='ne')'''

root.after(REFRESH_RATE,func)

root.mainloop()