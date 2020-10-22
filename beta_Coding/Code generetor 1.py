from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('720x400')

name = Label(window, text="Packet Generator")
name.place(relx = 0.5,rely = 0.1,anchor='center')

action = Label(window, text="Action")
action.grid(column=0, row=1)

direction = Label(window, text="Direction")
direction.grid(column=0, row=2)

ethernet_port = Label(window, text="Ethernet_port")
ethernet_port.grid(column=0, row=3)

src_address = Label(window, text="Source address")
src_address.grid(column=0, row=4)

src_mask = Label(window, text="Mask")
src_mask.grid(column=0, row=5)

src_port = Label(window, text="Port")
src_port.grid(column=0, row=6)

dst_address = Label(window, text="Destination address")
dst_address.grid(column=0, row=7)

dst_mask = Label(window, text="Mask")
dst_mask.grid(column=0, row=8)

dst_port = Label(window, text="Port")
dst_port.grid(column=0, row=9)

name.pack()

window.mainloop()
