from tkinter import *

def btnf1():
    r=var1.get()
    a = 3.142*r*r
    e2.insert(0,a)
    

def btnf2():
    e1.delete(0,END)
    e2.delete(0,END)




circle=Tk()


circle.title('area of a cirle')
circle.geometry('500x500+200+200')


mylabel=Label(text='CALCULATE THE AREA OF CIRCLE',fg='yellow',bg='black',font=12).grid(row=0,sticky=W)





var1=IntVar()


mylabel=Label(text='enter the radius',fg='yellow',padx=5,bg='blue',font=12).grid(row=2,sticky=W)
e1=Entry(width=10,textvariable=var1)
e1.grid(row=2,column=1,sticky=W)

mylabel=Label(text='AREA',fg='blue',bg='yellow',padx=47,font=12).grid(row=3,sticky=W)
e2=Entry(width=10)
e2.grid(row=3,column=1)
btn=Button(text='calcuate',width=10,fg='red',font=30,bg='black',padx=16,command=btnf1).grid(row=4,column=0,sticky=W)

btn2=Button(text='clear',width=10,fg='red',font=30,bg='black',padx=16,command=btnf2)
btn2.grid(row=4,column=1,sticky=W)



circle.mainloop()




