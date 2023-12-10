# gui.py
import datapd as dt
import pandas as pd
from tkinter import *
from forms import * 
import forms as fm
import tkinter as tk
from tkinter import ttk
from cate import Appcate


def on_add():
    # Xử lý nút thêm sản phẩm
    f=formdata()
    print('đ')
    # ...

def on_view():
    ct=Appcate()
    

def on_edit():
    # Xử lý nút chỉnh sửa sản phẩm
    print('đ')
    # ...


def on_product_selected(event):
    # Lấy sản phẩm được chọn
    product = treeview.item(event.widget.focus())['values']
    print(product)
    # Hiển thị thông tin chi tiết của sản phẩm
    i=0
    for item in product:
        txs[i].config(text=item)
        i+=1
   


def sort_col(col, reverse=False):
    l = [(treeview.set(k, col), k) for k in treeview.get_children()]
    l.sort(key=lambda t: t[0], reverse=reverse)

    # rearrange items in sorted order
    for index, (val, k) in enumerate(l):
        treeview.move(k, '', index)
def re_data():
    treeview.delete(*treeview.get_children())
    df = pd.read_csv("products.csv")
    df_rows =df.to_numpy().tolist()
    
    for row in df_rows:
        treeview.insert('', "end", values=row)
    
    
win = tk.Tk()
win.title("Frame Example")
win.config(bg="skyblue")

# Create Frame widget
left_frame = Frame(win, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

tool_bar = Frame(left_frame, width=180, height=185, bg="purple")
tool_bar.grid(row=2, column=0, padx=5, pady=5)


right_frame = Frame(win, width=650, height=400, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# Create frames and labels in left_frame
Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

# Create label above the tool_bar
Label(left_frame, text="Example Text").grid(row=1, column=0, padx=5, pady=5)
# Tạo label cho tiêu đề


title_label = tk.Label(win, text="Quản lý sản phẩm")
title_label.grid(row=0, column=0, columnspan=2)

# Tạo nút thêm sản phẩm

add_button = tk.Button(win, text="Thêm sản phẩm", command=on_add)
add_button.grid(row=1, column=0)

# Tạo nút xem tất cả sản phẩm

view_button = tk.Button(win, text="Tool", command=on_view)
view_button.grid(row=1, column=1)

# Tạo nút chỉnh sửa sản phẩm

edit_button = tk.Button(win, text="Chỉnh sửa sản phẩm", command=on_edit)
edit_button.grid(row=1, column=2)

treeview = ttk.Treeview(right_frame)
treeview.grid(row=0,column=0, padx=5, pady=5)


re_button = tk.Button(win, text="tai lai", command=re_data)
re_button.grid(row=3, column=0, columnspan=3)

# Tạo bảng để hiển thị danh sách sản phẩm



# Tạo các cột cho bảng




product_info_frame = tk.Frame(win)
product_info_frame.grid(row=2, column=3)
# Tạo các label cho thông tin sản phẩm



# Thêm sự kiện cho bảng

treeview.bind('<<TreeviewSelect>>', on_product_selected)
product_info_frame.config(borderwidth=1, relief="solid")
treeview.pack_propagate(False)
treeview.pack()

# Tạo các dòng cho bảng
#treeview.configure(yscrollcommand=self.scrollbar.set)
pro = dt.read_data("products.csv")
cate =dt.read_data("category.csv")
df=pd.merge(left=pro, right=cate, on='type_code')


treeview["columns"] = list(df.columns)
for column in treeview["columns"]:
    treeview.column(column,width=150)

for column in treeview["columns"]:
    treeview.heading(column, text=column)
    

df_rows = df.to_numpy().tolist()
for row in df_rows:
    print(row)
    treeview.insert('', "end", values=row)

for col in list(df.columns):
    treeview.heading(col, command=lambda c=col: sort_col(c))


# Thêm các cột cho bảng
i=0
txs=list()
for item in list(df.columns):
    lb=tk.Label(product_info_frame, text=item+":")
    lb.grid(row=i, column=0)
    tb=tk.Label(product_info_frame, text="")
    tb.grid(row=i, column=1)
    txs.append(tb)
    i+=1



win.mainloop()
