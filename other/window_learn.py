import tkinter as tk


window=tk.Tk()
window.title("Ian's page")
window.geometry("500x400")


def click():
    #lbl1.configure(text="click") #configure為變更、配置屬性

    a=txt1.get() #先設定變數，再用Entry中get的方法獲取輸入框中的文本內容
    lbl1.configure(text=a)


#Label 標籤
lbl1=tk.Label(window,text="Label1",width=10,bg="orange")
#lbl1.pack(side="left") #pack會在整個視窗中置中的上下左右
lbl1.grid(row=0,column=0)
#lbl1.place(x=50,y=50)

lbl2=tk.Label(window,text="Label2",width=10,bg="orange")
lbl2.grid(row=1,column=1) #若沒有lbl1，則lbl2會在起始左上角

#Button 按鈕
btn1=tk.Button(window,text="btu1",width=10,bg="pink",command=click)#command事件，給按紐下指令，之後定義click後改變lbl1的文字內容
btn1.grid(row=2,column=0)

#Entry 輸入框
txt1=tk.Entry(window)
txt1.grid(row=3,column=0)



window.mainloop()
