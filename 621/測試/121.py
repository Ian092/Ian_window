import tkinter as tk
from tkinter import  ttk
import csv
from tkinter.messagebox import showinfo

class Window(tk.Tk):
    def __init__(self):
        super().__init__();
        self.title("台北市長照機構")
        self.style = ttk.Style(self)
        self.datas = read_csv("01.csv")
        self.geometry('960x600')
        self.treeView = ttk.Treeview(self, columns=('#1','#2','#3', '#4', '#5', '#6', '#7','#8','#9','#10','#11','#12'),show='headings')
        self.treeView.heading('#1',text='序號')
        self.treeView.heading('#2', text='行政區')
        self.treeView.heading('#3', text='屬性')
        self.treeView.heading('#4', text='機構名稱')
        self.treeView.heading('#5', text='機構類型')
        self.treeView.heading('#6', text='成人日間照顧床位數量')
        self.treeView.heading('#7', text='全日型住宿床位數量')
        self.treeView.heading('#8', text='早療日間照顧')
        self.treeView.heading('#9', text='夜間型住宿床位數量')
        self.treeView.heading('#10', text='緊急短期安置床位數量')
        self.treeView.heading('#11', text='地址')
        self.treeView.heading('#12', text='網址')


        self.treeView.grid(row=0, column=0, sticky='nsew')
        self.treeView.bind("<<TreeviewSelect>>",self.item_selected)

        for _ in range(10):
            for data in self.datas[1:]:
                self.treeView.insert('',tk.END,values=data)
                

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.treeView.yview)
        self.treeView.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0,column=1,sticky='ns')


        self.treeView.column('#1', width=50)
        self.treeView.column('#2', width=80)
        self.treeView.column('#3', width=80)
        self.treeView.column('#4', width=150)
        self.treeView.column('#5', width=200)
        self.treeView.column('#6', width=80)
        self.treeView.column('#7', width=80)
        self.treeView.column('#8', width=80)
        self.treeView.column('#9', width=80)
        self.treeView.column('#10', width=80)
        self.treeView.column('#11', width=80)
        self.treeView.column('#12', width=80)



    def item_selected(self,event):
        #selection()取出的為一個元素的tuple
        #item(rowID)
        #取出的item為Dictionary)
        item = self.treeView.item(self.treeView.selection()[0])
        record = item['values']
        #showinfo(title='選取資訊',message=','.join(record))
        dialog = ShowDialog(self,'測試',['one','two','AAA'])


class ShowDialog:
    def closeWindow(self):

        self.subWindow.destroy()


    def __init__(self,root,message, options):
        self.subWindow = tk.Toplevel(root)
        self.subWindow.geometry('300x300')
        self.subWindow.transient()
        tk.Label(self.subWindow, text=message).pack()
        for item in options:
            ttk.Button(self.subWindow, text=item, command=self.closeWindow).pack()
        #self.subWindow.mainloop()


def read_csv(fileName):
    try:
        fileObject = open(fileName,'r',encoding='utf8')
    except Exception as e:
        print("讀取錯誤")
        fileObject.close()
        return None

    csvReaderObject = csv.reader(fileObject)
    return list(csvReaderObject)



if __name__ == "__main__":
    window = Window()
    window.mainloop()