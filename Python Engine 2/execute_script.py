"all run from this"
from tkinter import *
from packet_generator.rule_requirement import *
from packet_generator.Function import *
from dnn_model.training import *
from evaluate.evaluate import *

def build_template():
    # change name to 'data_info.csv' after and trainsetname as train_n (ex. train_1)
    generate_template()
    
    
def build_csv():
    generate_result()
    training_result()
    evaluate_result()

def gen():
    generate_packet()

def train():
    training()
    
def test():
    evaluate()
    
def button1():
    label1.configure(text="Button was clicked !!")
    build_template()
    label1.configure(text="Done!")
    
def button2():
    label2.configure(text="Button was clicked !!")
    build_csv()
    label2.configure(text="Done!")
    
def button3():
    label3.configure(text="Button was clicked !!")
    gen()
    label3.configure(text="Done!")
    
def button4():
    label4.configure(text="Button was clicked !!")
    train()
    label4.configure(text="Done!")
    
def button5():
    label5.configure(text="Button was clicked !!")
    test()
    label5.configure(text="Done!")


window = Tk()

window.title("Ai Firewall res. (Temp)")

window.geometry('300x200')

label1 = Label(window, text="build template")
label1.grid(column=0, row=0)
button1 = Button(window, text="Click Me", command=button1)
button1.grid(column=1, row=0)

label2 = Label(window, text="build table compare")
label2.grid(column=0, row=1)
button2 = Button(window, text="Click Me", command=button2)
button2.grid(column=1, row=1)

label3 = Label(window, text="generate packet")
label3.grid(column=0, row=2)
button3 = Button(window, text="Click Me", command=button3)
button3.grid(column=1, row=2)

label4 = Label(window, text="training")
label4.grid(column=0, row=3)
button4 = Button(window, text="Click Me", command=button4)
button4.grid(column=1, row=3)

label5 = Label(window, text="evaluate")
label5.grid(column=0, row=4)
button5 = Button(window, text="Click Me", command=button5)
button5.grid(column=1, row=4)

window.mainloop()