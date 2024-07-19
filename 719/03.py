import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)

# 定義列
tree['columns'] = ('name', 'age')

# 設定列標題
tree.heading('name', text='Name')
tree.heading('age', text='Age')

# 插入根項目
root_item = tree.insert('', 'end', text='Root Item', values=('Root', 0))

# 插入子項目
child_item_1 = tree.insert(root_item, 'end', text='Child 1', values=('Child 1', 10))
child_item_2 = tree.insert(root_item, 'end', text='Child 2', values=('Child 2', 20))

# 插入子項目的子項目
grandchild_item = tree.insert(child_item_1, 'end', text='Grandchild 1', values=('Grandchild 1', 5))

tree.pack()
root.mainloop()
