import tkinter as tk

root = tk.Tk()


root.geometry('300x350')
root.title("PyCalc")

textbox = tk.Text(root, height=3, font=('Arial', 18))
textbox.tag_configure("right", justify='right')
textbox.tag_add("right", 1.0, "end")
textbox.pack(padx=10, pady=10)


buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

global curr_num
curr_num = []
global saved_num
saved_num = []
global operator
operator = ""

def ClearEverything():
    textbox.delete('1.0', tk.END)    
    textbox.insert('end', "0")

def AddNum(num):
    curr_num.append(num)
    result = int(''.join(map(str, curr_num)))
    textbox.delete('1.0', tk.END)    
    textbox.insert('end', result)

def SetOperator(newoperator):
    operator = newoperator
    saved_num = curr_num
    curr_num = []
    textbox.delete('1.0', tk.END)

def OnEquals():
    if saved_num:
        saved = float(''.join(saved_num))
    else:
        saved = 0.0
    if curr_num:
        current = float(''.join(curr_num))
    else:
        current = 0.0

    textbox.delete('1.0', tk.END)
    if operator == '/':
        textbox.insert('end', saved / current)
    elif operator == '*':
        textbox.insert('end', saved * current)
    elif operator == '-':
        textbox.insert('end', saved - current)
    elif operator == '+':
        textbox.insert('end', saved + current)
    else:
        operator == '/'
        textbox.insert('end', "ERROR")

    


# Column 1
col1btn1 = tk.Button(buttonframe, text='CE', command=ClearEverything, font=('Arial', 18), width=3)
col1btn1.grid(row=0, column=0)

col1btn2 = tk.Button(buttonframe, text='7', command=lambda: AddNum(7), font=('Arial', 18), width=3)
col1btn2.grid(row=1, column=0)

col1btn3 = tk.Button(buttonframe, text='4', command=lambda: AddNum(4), font=('Arial', 18), width=3)
col1btn3.grid(row=2, column=0)

col1btn4 = tk.Button(buttonframe, text='1', command=lambda: AddNum(1), font=('Arial', 18), width=3)
col1btn4.grid(row=3, column=0)


# Column 2
col2btn1 = tk.Button(buttonframe, text='C', font=('Arial', 18), width=3)
col2btn1.grid(row=0, column=1)

col2btn2 = tk.Button(buttonframe, text='8', command=lambda: AddNum(8), font=('Arial', 18), width=3)
col2btn2.grid(row=1, column=1)

col2btn3 = tk.Button(buttonframe, text='5', command=lambda: AddNum(5), font=('Arial', 18), width=3)
col2btn3.grid(row=2, column=1)

col2btn4 = tk.Button(buttonframe, text='2', command=lambda: AddNum(2), font=('Arial', 18), width=3)
col2btn4.grid(row=3, column=1)

col2btn5 = tk.Button(buttonframe, text='0', command=lambda: AddNum(0), font=('Arial', 18), width=3)
col2btn5.grid(row=4, column=1)

# Column 3
col3btn1 = tk.Button(buttonframe, text='←', font=('Arial', 18), width=3)
col3btn1.grid(row=0, column=2)

col3btn2 = tk.Button(buttonframe, text='9', command=lambda: AddNum(9), font=('Arial', 18), width=3)
col3btn2.grid(row=1, column=2)

col3btn3 = tk.Button(buttonframe, text='6', command=lambda: AddNum(6), font=('Arial', 18), width=3)
col3btn3.grid(row=2, column=2)

col3btn4 = tk.Button(buttonframe, text='3', command=lambda: AddNum(3), font=('Arial', 18), width=3)
col3btn4.grid(row=3, column=2)

col3btn5 = tk.Button(buttonframe, text='.', font=('Arial', 18), width=3)
col3btn5.grid(row=4, column=2)

# Column 4
col4btn1 = tk.Button(buttonframe, text='÷', command=lambda: SetOperator('/'), font=('Arial', 18), width=3)
col4btn1.grid(row=0, column=3)

col4btn2 = tk.Button(buttonframe, text='×', command=lambda: SetOperator('*'), font=('Arial', 18), width=3)
col4btn2.grid(row=1, column=3)

col4btn3 = tk.Button(buttonframe, text='-', command=lambda: SetOperator('-'), font=('Arial', 18), width=3)
col4btn3.grid(row=2, column=3)

col4btn4 = tk.Button(buttonframe, text='+', command=lambda: SetOperator('+'), font=('Arial', 18), width=3)
col4btn4.grid(row=3, column=3)

col4btn5 = tk.Button(buttonframe, text='=', command=lambda: OnEquals(), font=('Arial', 18), width=3)
col4btn5.grid(row=4, column=3)


buttonframe.pack()

root.mainloop()