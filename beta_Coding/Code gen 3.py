import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import random
import re

root = tk.Tk()
root.title("Packet Generator")

canvas = tk.Canvas(root, width=600, height=450, relief='raised')
canvas.pack()

action = tk.Label(root, text='action')
action.config(font=('helvetica', 10)
    act1 = Radiobutton(canvas,text='Allow', value=1)
act2 = Radiobutton(canvas,text='Deny', value=2)
action.grid(column=0, row=0)
act1.grid(column=1, row=0)
act2.grid(column=2, row=0)


direc = tk.Label(root, text='direction')
direc.config(font=('helvetica', 10))
canvas.create_window(150, 110, window=direc)
edirec = ttk.Combobox(root)
edirec['values'] = ('in', 'out', 'any')
canvas.create_window(395, 110, width=195, window=edirec)

intf = tk.Label(root, text='interface')
intf.config(font=('helvetica', 10))
canvas.create_window(150, 140, window=intf)
eintf = ttk.Combobox(root)
eintf['values'] = ('eth0', 'wlp2s0', 'any')
canvas.create_window(395, 140, width=195, window=eintf)

srcip = tk.Label(root, text='source ip and mask')
srcip.config(font=('helvetica', 10))
canvas.create_window(150, 170, window=srcip)
esrcip = ttk.Combobox(root)
esrcip['values'] = ('161.246.0.0/24', '156.87.62.0/24', '198.175.30.0/24', '96.183.127.0/24')
canvas.create_window(395, 170, width=195, window=esrcip)

srcpt = tk.Label(root, text='source port')
srcpt.config(font=('helvetica', 10))
canvas.create_window(150, 200, window=srcpt)
esrcpt = ttk.Combobox(root)
esrcpt['values'] = ('53,67,68,80,110,119,123,143,161,194,443,25')
canvas.create_window(333, 200, width=70, window=esrcpt)

desip = tk.Label(root, text='destination ip and mask')
desip.config(font=('helvetica', 10))
canvas.create_window(150, 230, window=desip)
edesip = ttk.Combobox(root)
edesip['values'] = ('192.168.5.0/24', '137.251.75.0/24', '216.40.100.0/24', '52.172.64.0/24')
canvas.create_window(395, 230, width=195, window=edesip)

despt = tk.Label(root, text='destination port')
despt.config(font=('helvetica', 10))
canvas.create_window(150, 260, window=despt)
edespt = ttk.Combobox(root)
edespt['values'] = '53,67,68,80,110,119,123,143,161,194,443,25'
canvas.create_window(333, 260, width=70, window=edespt)

prot = tk.Label(root, text='protocol')
prot.config(font=('helvetica', 10))
canvas.create_window(150, 290, window=prot)
eprot = ttk.Combobox(root)

eprot['values'] = ('tcp', 'udp', 'any')
canvas.create_window(395, 290, width=195, window=eprot)

root.mainloop()
