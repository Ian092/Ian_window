import tkinter as tk

# 創建主窗口
root = tk.Tk()

# 創建一個標籤小部件，將它的 master 設置為 root
label = tk.Label(root, text="Hello, World!")
label.pack()

# 創建一個獨立的頂級窗口
top_level = tk.Toplevel(root)
top_level.title("Another Window")

# 在頂級窗口中添加其他小部件
button = tk.Button(top_level, text="Close Window", command=top_level.destroy)
button.pack()

# 運行主迴圈
root.mainloop()
