from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import numpy as np
import serial as sr
import time as tm

global time_int

root = tk.Tk()
root.title('Push Button Counter')
root.configure(background='light green')
root.geometry("400x200")

#Time Label
timeLabel = tk.Label(root, text ="Timp(s):  ")
timeLabel.place(x = 300, y = 10)

def updateLabel(i):
    timeLabel.config(text = "Timp(s): " + str(i))
    root.update()

def print_time():
    print_time.counter+=1;
    root.after(1000, updateLabel(print_time.counter))
print_time.counter = 0

def sendTime():
    time = inputTime.get(1.0, "end-1c")
    global time_int
    time_int = int(time)
    time += 'r'
    s.write(time.encode('ascii'))

def send_and_print():
    sendTime()
    global time_int
    for i in range(time_int):
        print_time()

def receiveCounter():
    counter = s.readline().decode()
    counter = s.readline()
    l = list(bytes(counter))
    lbl.config(text = "Numar apasari buton: " + str((l[0] - 48)))

#Text Box creation
inputTime = tk.Text(root, height = 3, width = 7)
inputTime.place(x = 150, y = 10)

#Send Button Creation
sendButton = tk.Button(root, text = "Send", command = send_and_print)
sendButton.place(x = 163, y = inputTime.winfo_y() + inputTime.winfo_reqheight() + 20)

#Receive Button Creation
receiveButton = tk.Button(root, text = "Receive", command = receiveCounter)
receiveButton.place(x = 157, y = sendButton.winfo_y() + sendButton.winfo_reqheight() + 80)

#Label creation
lbl = tk.Label(root, text = "Numar apasari buton:   ")
lbl.place(x = 120, y = receiveButton.winfo_y() + receiveButton.winfo_reqheight() + 115)

s = sr.Serial('COM9', 115200)

if s.isOpen():
    print(s.name + ' is open...')

s.reset_input_buffer()

root.mainloop()