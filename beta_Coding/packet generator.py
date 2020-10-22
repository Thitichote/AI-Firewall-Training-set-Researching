import tkinter as tk
from tkinter import ttk
import random
import re
import csv
import math

root = tk.Tk()
root.title("Packet Generator")

canvas = tk.Canvas(root, width=600, height=450, relief='raised')
canvas.pack()

head = tk.Label(root, text='Generate Packet')
head.config(font=('helvetica', 14))
canvas.create_window(300, 35, window=head)

action = tk.Label(root, text='action')
action.config(font=('helvetica', 10))
canvas.create_window(150, 80, window=action)
eact = ttk.Combobox(root)
eact['values'] = ('allow', 'deny')
canvas.create_window(395, 80, width=195, window=eact)

srcip = tk.Label(root, text='source ip and mask')
srcip.config(font=('helvetica', 10))
canvas.create_window(150, 110, window=srcip)
esrcip = ttk.Combobox(root)
esrcip['values'] = ('161.246.0.0/24', '156.87.62.0/24', '198.175.30.0/24', '96.183.127.0/24')
canvas.create_window(395, 110, width=195, window=esrcip)

srcpt = tk.Label(root, text='source port')
srcpt.config(font=('helvetica', 10))
canvas.create_window(150, 140, window=srcpt)
esrcpt = ttk.Combobox(root)
esrcpt['values'] = ('53,67,68,80,110,119,123,143,161,194,443,25')
canvas.create_window(333, 140, width=70, window=esrcpt)

desip = tk.Label(root, text='destination ip and mask')
desip.config(font=('helvetica', 10))
canvas.create_window(150, 170, window=desip)
edesip = ttk.Combobox(root)
edesip['values'] = ('192.168.5.0/24', '137.251.75.0/24', '216.40.100.0/24', '52.172.64.0/24')
canvas.create_window(395, 170, width=195, window=edesip)

despt = tk.Label(root, text='destination port')
despt.config(font=('helvetica', 10))
canvas.create_window(150, 200, window=despt)
edespt = ttk.Combobox(root)
edespt['values'] = '53,67,68,80,110,119,123,143,161,194,443,25'
canvas.create_window(333, 200, width=70, window=edespt)

prot = tk.Label(root, text='protocol')
prot.config(font=('helvetica', 10))
canvas.create_window(150, 230, window=prot)
eprot = ttk.Combobox(root)
eprot['values'] = ('tcp', 'udp', 'any')
canvas.create_window(395, 230, width=195, window=eprot)

number = tk.Label(root, text='generate N')
number.config(font=('helvetica', 10))
canvas.create_window(150, 260, window=number)
num_n = ttk.Combobox(root)
num_n['values'] = ("-", 10, 20, 30)
canvas.create_window(333, 260, width=70, window=num_n)

def action_getinfo(): # test what output is
    act = eact.get()
    s_add = esrcip.get()
    s_port = esrcpt.get()
    d_add = edesip.get()
    d_port = edespt.get()
    pp = eprot.get()
    print(act, s_add, s_port, d_add, d_port, pp)

def generate():
    

gen_button = tk.Button(text='Make one',command=action_getinfo, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas.create_window(300, 360, window=gen_button)

gen_button1 = tk.Button(text='Generate',command=action_getinfo, bg='green yellow', fg='navy', font=('helvetica', 9, 'bold'))
canvas.create_window(400, 360, window=gen_button1)

# add command = ,command=5646464

root.mainloop()
