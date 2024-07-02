import requests # type: ignore
import tkinter as tk
from tkinter.font import Font


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
    
        
        
        areas = ['中正區', '大同區', '中山區', '萬華區', 
        '信義區', '松山區', '大安區', '南港區', 
        '北投區', '內湖區', '士林區', '文山區']

        #介面
        self.title("台北市長照機構")
        TopFrame = tk.Frame(self, bd=2, relief=tk.GROOVE, padx=10, pady=7)
        buttonFont = Font(family='微軟正黑體', size=12)

       
        for index, area in enumerate(areas):
        
            btn = tk.Button(TopFrame, text=area, font=buttonFont, bg="#D7C4BB", fg="#6A4028", padx=5, pady=8)
            btn.pack(side=tk.LEFT, padx=5)
     
        TopFrame.pack(side=tk.LEFT, padx=10, pady=(0, 10))







if __name__ == "__main__":
    window = Window()
    window.geometry("+50+50")
    window.mainloop()