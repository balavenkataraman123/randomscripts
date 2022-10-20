import os
from tkinter import *
def show_values(val):
	os.system('xrandr --output eDP --brightness ' + str(int(w1.get())/100))
	os.system('xrandr --output HDMI-A-0 --brightness ' + str(int(w2.get())/100))

master = Tk()
text = Label(master, text="laptop screen")
text.pack()
w1 = Scale(master, from_=100, to=10, command=show_values)
w1.set(100)
w1.pack()
text1 = Label(master, text="external screen")
text1.pack()
w2 = Scale(master, from_=100, to=0, command=show_values)
w2.set(100)
w2.pack()


mainloop()

## a thing to control the brightness of an external monitor
## "hdmi-a-0" and "eDP" varies by device
