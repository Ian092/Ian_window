import tkinter as tk
from ttkbootstrap import Style


style=Style(theme="solar")
ttt=style.master
window=tk.Tk()
window.title("Ian's page")
window.geometry("600x200")

lbl1=tk.Label(window,text="四則運算器")
lbl1.grid(row=0,column=1)


def click1():
   
    a=txt1.get()
    b=txt2.get()
    c=int(a)+int(b)
    lbl2.configure(text=c)

def click2():
   
    a=txt1.get()
    b=txt2.get()
    c=int(a)-int(b)
    lbl2.configure(text=c)    


def click3():
   
    a=txt1.get()
    b=txt2.get()
    c=int(a)*int(b)
    lbl2.configure(text=c)        


def click4():
   
    a=txt1.get()
    b=txt2.get()
    c=int(a)/int(b)
    lbl2.configure(text=c)        



txt1=tk.Entry(window) #INPUT 1
txt1.grid(row=3,column=0)

txt2=tk.Entry(window) #INPUT 2
txt2.grid(row=3,column=2)


btn1=tk.Button(window,text="+",width=2,bg="pink",command=click1)
btn1.grid(row=1,column=1)

btn2=tk.Button(window,text="-",width=2,bg="pink",command=click2)
btn2.grid(row=2,column=1)

btn3=tk.Button(window,text="*",width=2,bg="pink",command=click3)
btn3.grid(row=3,column=1)

btn4=tk.Button(window,text="/",width=2,bg="pink",command=click4)
btn4.grid(row=4,column=1)



lbl1=tk.Label(window,text="=",width=10)
lbl1.grid(row=3,column=3)

lbl2=tk.Label(window,text=" ",width=10,bg="orange")
lbl2.grid(row=3,column=4)


txt1=tk.Entry(window) #OUTPUT
txt1.grid(row=3,column=0)

window.mainloop()
