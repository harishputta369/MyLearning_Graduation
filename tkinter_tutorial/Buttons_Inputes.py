from tkinter import *
root=Tk()

#creating buttons
B1=Button(root,text="click B1")
I=Entry(root,font=("Arial",25),width=10)
B2=Button(root,text="clcik B2")
B2.pack(padx=20,pady=20) #pack avvagane tikinter window loki vachesthundi
I.pack(padx=20,pady=20)
B1.pack(padx=30,pady=30)
root.mainloop()