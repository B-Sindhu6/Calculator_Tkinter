# Code written by B. Sindhu
# Simple GUI calculator using Tkinter in python

import tkinter as tk
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1) # to enhance the output window
root = tk.Tk()
root.geometry('+500+400') # to set the output window position on screen
root.resizable(0,0) # to fix the window size / disable maximize option
root.title("My_Calc")
var=tk.StringVar()
var.set('')
reset=0
# root.minsize(207,270) 
# root.maxsize(207,270)

def onclick(char):
    global reset
    if reset ==1:
        clear()
        reset=0
    look.insert(len(look.get()),char)

def delete():
    look.delete(len(look.get())-1)

def clear():
    look.delete(0,'end')
    var.set('')

def equal(event=None):
    global var
    global reset
    exp=look.get()
    if exp.startswith('0'):
        while exp[0]=='0':
            if len(exp)==1:
                break
            exp= exp[1:]
    try:
        res=round(eval(exp),4)
        look.delete(0,'end')
        look.insert(0,res)

    except:
        look.delete(0,'end')
        look.insert(0,exp)
        if len(exp)==0:
            exp=''
        else: 
            exp='error'
    var.set(exp)
    reset=1

look=tk.Entry(root, text='0',justify=tk.RIGHT)
look.grid(row=1,column=0,columnspan=4,ipady=5, sticky='news')
look.focus()
root.bind("<Return>",equal)

tk.Button(root, width=8, text='C',command=clear).grid(row=2, column=0,sticky='news')
tk.Button(root, width=8, text='(',command=lambda: onclick('(')).grid(row=2, column=1,ipady=5,sticky='news')
tk.Button(root, width=8, text=')',command=lambda: onclick(')')).grid(row=2, column=2,sticky='news')
tk.Button(root, width=8, text='del',command=delete).grid(row=2,ipady=5,column=3,sticky='news')

tk.Button(root, text='7',command=lambda: onclick('7')).grid(row=3,ipady=5,column=0,sticky='news')
tk.Button(root, text='8',command=lambda: onclick('8')).grid(row=3,ipady=5,column=1,sticky='news')
tk.Button(root, text='9',command=lambda: onclick('9')).grid(row=3,ipady=5,column=2,sticky='news')
tk.Button(root, text='/',command=lambda: onclick('/')).grid(row=3, column=3,sticky='news')

tk.Button(root, text='4',command=lambda: onclick('4')).grid(row=4,ipady=5,column=0,sticky='news')
tk.Button(root, text='5',command=lambda: onclick('5')).grid(row=4,ipady=5,column=1,sticky='news')
tk.Button(root, text='6',command=lambda: onclick('6')).grid(row=4,ipady=5,column=2,sticky='news')
tk.Button(root, text='*',command=lambda: onclick('*')).grid(row=4, column=3,ipady=5,sticky='news')

tk.Button(root, text='1',command=lambda: onclick('1')).grid(row=5,ipady=5,column=0,sticky='news')
tk.Button(root, text='2',command=lambda: onclick('2')).grid(row=5,ipady=5,column=1,sticky='news')
tk.Button(root, text='3',command=lambda: onclick('3')).grid(row=5,ipady=5,column=2,sticky='news')
tk.Button(root, text='-',command=lambda: onclick('-')).grid(row=5, column=3,sticky='news')

tk.Button(root, text='.',command=lambda: onclick('.')).grid(row=6,column=0,sticky='news')
tk.Button(root, text='0',command=lambda: onclick('0')).grid(row=6,ipady=5,column=1,sticky='news')
tk.Button(root, text='=',command=equal).grid(row=6, column=2,sticky='news')
tk.Button(root, text='+',command=lambda: onclick('+')).grid(row=6, column=3,ipady=5,sticky='news')

Display=tk.Label(root,textvariable=var,justify=tk.RIGHT)
Display.grid(row=0,columnspan=4, ipady=5,sticky='news')

root.mainloop()
