from tkinter import *
root=Tk()
root.iconbitmap('images/p.ico')
root.title('just app')
'''''''''
labletext=Label(root,text="hello from label1 text")
labletext2=Label(root,text="hello from label2 text")
labletext3=Label(root,text="hello from label3 text")
labletext.pack(pady=10)
labletext2.pack(pady=10)
labletext3.pack(pady=10)
'''''''''
labletext4=Label(root,text="hello from label1 text",fg='red')
labletext5=Label(root,text="hello from label2 text",bg='blue')
labletext6=Label(root,text="hello from label3 text")
labletext4.grid(row=0,column=0)
labletext5.grid(row=1,column=1)
labletext6.grid(row=1,column=2,padx=10)
root.mainloop()