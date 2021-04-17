from tkinter import *
from packet_generator.rule_requirement import *
from packet_generator.Function import *
from dnn_model.training import *
from evaluate.evaluate import *

import tkinter as tk
from tkinter import ttk
import os
import pathlib
import shutil

path = str(pathlib.Path().absolute())
# debug1 = generate_packet()

def build_template():
    # change name to 'data_info.csv' after and trainsetname as train_n (ex. train_1)
    generate_template()
    text.configure(text="template generated..")
    
    
def build_csv():
    generate_result()
    training_result()
    evaluate_result()
    text.configure(text="table generated..")

def gen():
    generate_packet()
    text.configure(text="packets generated..")

def train():
    train_model()
    text.configure(text="training done..")
    
def test():
    evaluate_model()
    text.configure(text="evaluating done..")

def open_template():
    try:
        os.startfile(path + '/_csv/template.csv')
        text.configure(text="open template.csv")
    except:
        text.configure(text="template.csv not found!")
        
def open_data_info():
    try:
        os.startfile(path + '/_csv/data_info.csv')
        text.configure(text="open data_info.csv")
    except:
        text.configure(text="data_info.csv not found!")

def change_name():
    try:
        shutil.move("_csv/template.csv", "_csv/data_info.csv")
        text.configure(text="name changed successful")
    except:
        text.configure(text="data_info.csv not found!")

def open_gen_result():
    try:
        os.startfile(path + '/_csv/result/generate_result.csv')
        text.configure(text="open generate_result.csv")
    except:
        text.configure(text="generate_result.csv not found!")

def open_train_result():
    try:
        os.startfile(path + '/_csv/result/training_result.csv')
        text.configure(text="open training_result.csv")
    except:
        text.configure(text="training_result.csv not found!")

def open_evaluate_result():
    try:
        os.startfile(path + '/_csv/result/evaluate_result.csv')
        text.configure(text="open evaluate_result.csv")
    except:
        text.configure(text="evaluate_result.csv not found!")

root = tk.Tk()

text = ttk.Label(root,width=47, text = '>_')

# ------------- Button Command ----------------------

button_open_csv1 = ttk.Button(root, text='open template', width=20, command=open_template)
button_open_csve = ttk.Button(root, text='open input table', width=20, command=open_data_info)
button_open_csv2 = ttk.Button(root, text='open generate result', width=20, command=open_gen_result)
button_open_csv3 = ttk.Button(root, text='open training result', width=20, command=open_train_result)
button_open_csv4 = ttk.Button(root, text='open evaluate result', width=20, command=open_evaluate_result)

gen_template = ttk.Button(root, text='generate template', width=20, command=build_template)
changename = ttk.Button(root, text='template -> data_info', width=20, command=change_name)
gen_table = ttk.Button(root, text='generate table', width=20, command=build_csv)
gen_packet = ttk.Button(root, text='generate packets', width=20, command=gen)
training = ttk.Button(root, text='training model', width=20, command=train)
evaluate = ttk.Button(root, text='evaluate model', width=20, command=test)

# ------------- Button place ----------------------

button_open_csv1.place(x=200,y=50)
button_open_csve.place(x=200,y=80)
button_open_csv2.place(x=200,y=140)
button_open_csv3.place(x=200,y=170)
button_open_csv4.place(x=200,y=200)

gen_template.place(x=40,y=50)
changename.place(x=40,y=80)
gen_table.place(x=40,y=110)
gen_packet.place(x=40,y=140)
training.place(x=40,y=170)
evaluate.place(x=40,y=200)

text.place(x=40, y=240)

# ------------- Window ----------------------------

root.geometry("370x270")

root.title('AI-Firewall (research only)')

root.iconbitmap('firewall_icon.ico')

# -------------------------------------------------

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))

root.mainloop()