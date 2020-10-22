from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

window = Tk()

selected = IntVar()

window.title("Packet Generator")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Make Packet')
tab_control.add(tab2, text='Random Packet')

tab_control.pack(expand=1, fill='both')

label_Action = Label(window, text="Action:", font=("Arial Bold", 12))
label_Action.place(x=20, y=50)
rad1 = Radiobutton(window,text='Allow', value=1, variable=selected)
rad2 = Radiobutton(window,text='Deny', value=2, variable=selected)
rad1.place(x=90, y=52)
rad2.place(x=170, y=52)
def clicked():

   print(selected.get())

label_Direction = Label(window, text="Direction:", font=("Arial Bold", 12))
label_Direction.place(x=20, y=80)

label_Interface = Label(window, text="Interface:", font=("Arial Bold", 12))
label_Interface.place(x=20, y=110)

label_src_address = Label(window, text="Src_address:", font=("Arial Bold", 12))
label_src_address.place(x=20, y=140)

label_src_mask = Label(window, text="Mask:", font=("Arial Bold", 12))
label_src_mask.place(x=370, y=140)

label_src_port = Label(window, text="Src_port:", font=("Arial Bold", 12))
label_src_port.place(x=20, y=170)

label_dst_address = Label(window, text="Dst_address:", font=("Arial Bold", 12))
label_dst_address.place(x=20, y=200)

label_dst_mask = Label(window, text="Mask:", font=("Arial Bold", 12))
label_dst_mask.place(x=370, y=200)

label_dst_port = Label(window, text="Dst_port:", font=("Arial Bold", 12))
label_dst_port.place(x=20, y=230)

label_protocol = Label(window, text="Protocol:", font=("Arial Bold", 12))
label_protocol.place(x=20, y=260)

window.geometry("530x400")

window.mainloop()
