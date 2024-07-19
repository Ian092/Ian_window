import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def item_selected(event):
    selected_items = tree.selection()
    for selected_item in selected_items:
        item = tree.item(selected_item)
        
        # 提取 item['values']
        values = item['values']
        # 提取 item['text']
        text = item['text']
        
        # 显示 item['values'] 和 item['text']
        message = f"Text: {text}\nValues: {', '.join(map(str, values))}"
        showinfo(title='Item Information', message=message)

root = tk.Tk()
root.title('Treeview Example')
root.geometry('400x200')

# 定义列
columns = ('Name', 'Age')

# 创建 Treeview
tree = ttk.Treeview(root, columns=columns, show='headings')

# 设置列标题
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')

# 插入数据
tree.insert('', 'end', iid='1', text='Alice', values=('Alice', 30))
tree.insert('', 'end', iid='2', text='Bob', values=('Bob', 25))

# 绑定选择事件
tree.bind('<<TreeviewSelect>>', item_selected)

tree.pack(fill=tk.BOTH, expand=True)

root.mainloop()
