# gui.py
import datapd as dt
import pandas as pd
from forms import * 
import forms as fm
import tkinter as tk
from tkinter import ttk

def on_add():
    # Xử lý nút thêm sản phẩm
    f=formdata()
    print('đ')
    # ...

def on_view():
    # Xử lý nút xem tất cả sản phẩm
    print('đ')
    # ...

def on_edit():
    # Xử lý nút chỉnh sửa sản phẩm
    print('đ')
    # ...


def on_product_selected(event):
    # Lấy sản phẩm được chọn
    product = treeview.item(event.widget.focus())['values']
    print(product)
    # Hiển thị thông tin chi tiết của sản phẩm
    product_code_label.config(text=product[3])
    product_name_label.config(text=product[1])
    product_type_label.config(text=product[5])
    product_price_label.config(text=product[4])
    product_quantity_label.config(text=product[2])


def dataTable(table):
    print(1)
    
    
win = tk.Tk()

# Tạo label cho tiêu đề

title_label = tk.Label(win, text="Quản lý sản phẩm")
title_label.grid(row=0, column=0, columnspan=3)

# Tạo nút thêm sản phẩm

add_button = tk.Button(win, text="Thêm sản phẩm", command=on_add)
add_button.grid(row=1, column=0)

# Tạo nút xem tất cả sản phẩm

view_button = tk.Button(win, text="Xem tất cả sản phẩm", command=on_view)
view_button.grid(row=1, column=1)

# Tạo nút chỉnh sửa sản phẩm

edit_button = tk.Button(win, text="Chỉnh sửa sản phẩm", command=on_edit)
edit_button.grid(row=1, column=2)

# Tạo bảng để hiển thị danh sách sản phẩm

treeview = ttk.Treeview(win)
treeview.grid(row=2, column=0, columnspan=3)

# Tạo các cột cho bảng




product_info_frame = tk.Frame(win)
product_info_frame.grid(row=2, column=3)
# Tạo các label cho thông tin sản phẩm

product_name_label = tk.Label(product_info_frame, text="Tên sản phẩm")
product_code_label = tk.Label(product_info_frame, text="Mã sản phẩm")
product_type_label = tk.Label(product_info_frame, text="loại sản phẩm")
product_price_label = tk.Label(product_info_frame, text="Giá sản phẩm")
product_quantity_label = tk.Label(product_info_frame, text="Số lượng sản phẩm")

# Thêm các label vào frame
product_code_label.grid(row=0, column=0)
product_name_label.grid(row=1, column=0)
product_type_label.grid(row=2, column=0)
product_price_label.grid(row=3, column=0)
product_quantity_label.grid(row=4, column=0)

# Thêm sự kiện cho bảng

treeview.bind('<<TreeviewSelect>>', on_product_selected)
product_info_frame.config(borderwidth=1, relief="solid")

# Tạo các dòng cho bảng
#treeview.configure(yscrollcommand=self.scrollbar.set)
df = pd.read_csv("products.csv")
treeview["columns"] = list(df.columns)
for column in treeview["columns"]:
    treeview.heading(column, text=column)
    df_rows = df.to_numpy().tolist()
for row in df_rows:
    treeview.insert('', "end", values=row)


# Thêm các cột cho bảng



win.mainloop()
