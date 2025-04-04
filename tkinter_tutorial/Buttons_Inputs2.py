from tkinter import *
root=Tk()
def fun1():
    l=Label(root,text="you clicked on first Button",font=("Arial",22))
    l.pack()
def fun2():
    l=Label(root,text="I love you Harish 😘😘😘😘😘😘",font=("Arial Black",30))
    l.pack()
i=Entry(root,width=20,font=("Ink Free",14))
i.pack()
B=Button(root,text="Click😁",font=("Calibri",10),padx=30,pady=30,command=fun1)
B.pack(side=LEFT)
B2=Button(root,text="click me",font=("BankGothic Md BT",10),padx=20,pady=20,command=fun2)
B2.pack(side=RIGHT)
root.mainloop()