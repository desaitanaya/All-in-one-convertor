import tkinter as tk
from functools import partial
tempVal = "Celsius"
def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp
def call_convert(rlabel1, rlabe12, inputn):
    tem = inputn.get()
    if tempVal == 'Temperature':
        f = float((float(tem) * 9 / 5) + 32)
        rlabel1.config(text="%f Fahrenheit" % f)
    elif tempVal == 'Speed':
        c = float((float(tem)*3.6))
        rlabel1.config(text="%f Speed in km/hr" % c)
    elif tempVal == 'Data':
        c = float(float(tem)/(1e+6))
        rlabel1.config(text="%f Data In GB" % c)
    elif tempVal =='Time':
        c=float(float(tem)/60)
        rlabel1.config(text="%f Minutes" % c)
    elif tempVal == 'Exit':
        root.destroy()
root = tk.Tk()
root.geometry('400x150+100+200')
root.title('Convertor')
root.configure(background='#09A3BA')
root.resizable(width=False, height=False)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1) 
numberInput = tk.StringVar()
var = tk.StringVar()
# label and entry field
input_label = tk.Label(root, text="Enter Data", background='#09A3BA', foreground="#FFFFFF")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=1)
input_entry.grid(row=1, column=1)
 
# result label's for showing the other two temperatures
result_label1 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label1.grid(row=3, columnspan=4)
result_label2 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label2.grid(row=4, columnspan=4)
 
# drop down initalization and setup
dropDownList = ['','Temperature','Speed','Data','Time','Exit' ]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=1, column=3)
dropdown.config(background='#09A3BA', foreground="#FFFFFF")
dropdown["menu"].config(background='#09A3BA', foreground="#FFFFFF")
 
# button click
call_convert = partial(call_convert, result_label1, result_label2, numberInput)
result_button = tk.Button(root, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")
result_button.grid(row=2, columnspan=4)
 
root.mainloop()
 


 

