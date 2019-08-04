from tkinter import * 
import backend 


bn = backend.bank()

    
def viewCommand():
    lb1.delete(0,END)
    lb2.delete(0,END)
    for rows in bn.view():
        lb1.insert(END,rows)
    lb2.insert(END,"STATEMENT")

def depositCommand():
    try:
        lb2.delete(0,END)
        bn.deposit(float(dep_text.get()))
        lb2.insert(END,"DEPOSIT")
    except:
        pass

def withdrawCommand():
    try:
        lb2.delete(0,END)
        bn.withdraw(float(wit_text.get()))
        lb2.insert(END,"WITHDRAWL")
    except:
        pass
    

    
app = Tk()

# 1. Entry classes 
dep_text = StringVar()
wit_text = StringVar()
e1 = Entry(app, textvariable = dep_text)
e2 = Entry(app, textvariable = wit_text)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# 2. Label classes
l1 = Label(app, text="Deposit", width=10)
l2 = Label(app, text="Withdraw", width=10)

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

# 3. Listbox Classes 
lb1 = Listbox(app, height=7, width=35)
lb2 = Listbox(app, height=1, width=12)

lb1.grid(row=2, column=0, rowspan=3, columnspan=2)
lb2.grid(row=0, column=3)

# 4. Scrollbar class
sb1 = Scrollbar(app)
sb1.grid(row=3, column=2)


# 5. Configure Listbox and Scrollbox
lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)


# 6. Button classes
b1 = Button(app, text="Deposit", width=10, command= depositCommand)
b2 = Button(app, text="Withdraw", width=10, command= withdrawCommand)
b3 = Button(app, text="View All", width=10, command= viewCommand)
b4 = Button(app, text="Close", width=10, command= app.destroy)

b1.grid(row=2, column=3)
b2.grid(row=3, column=3)
b3.grid(row=4, column=3)
b4.grid(row=5, column=3)



app.mainloop()