# gui.py
import datapd as dt
import pandas as pd
from tkinter import *

import tkinter as tk
from tkinter import ttk




def on_view():
    ct=Appcate()
def on_product_selected(event):
    # Lấy sản phẩm được chọn
    product = treeview.item(event.widget.focus())['values']
    
    # Hiển thị thông tin chi tiết của sản phẩm
    i=0
    for item in product:
        txs[i].delete(0, "end")
        txs[i].insert(0, item)
        i+=1
     



def sort_col(col, reverse=False):
    l = [(treeview.set(k, col), k) for k in treeview.get_children()]
    l.sort(key=lambda t: t[0], reverse=reverse)

    # rearrange items in sorted order
    for index, (val, k) in enumerate(l):
        treeview.move(k, '', index)
def re_data():
    treeview.delete(*treeview.get_children())
    
    pro = dt.read_data("products.csv")
    _cate =dt.read_data("category.csv")
    df=pd.merge(left=pro, right=_cate, on='type_code')
    df_rows =df.to_numpy().tolist()
    for row in df_rows:
        treeview.insert('', "end", values=row)
def f_data(df_new):
    treeview.delete(*treeview.get_children())  
    df_rows =df_new.to_numpy().tolist()
    for row in df_rows:
        treeview.insert('', "end", values=row)
def on_combobox_change(event):
    # Get the selected item
    selected_item = event.widget.get()
    sl_cate=_cate.loc[_cate["type_name"].str.contains(str(selected_item))]
    txs[len(pro.columns)-1].delete(0, "end")
    txs[len(pro.columns)-1].insert(0, sl_cate.iloc[0, 1])
    txs[len(pro.columns)].delete(0, "end")
    txs[len(pro.columns)].insert(0, sl_cate.iloc[0, 0])
       
def add_row():
 
    code= txs[0].get()
    name= txs[1].get()
    quantity= txs[2].get()
    price= txs[3].get()
    catee= txs[4].get()
    pro=dt.add_pr(code,name,quantity,price,catee)
    re_data()
    del    code, name ,quantity,price,catee
def delete_row():
    code= txs[0].get()
    dt.delete_data(code)
   
    re_data()
def update_row():
    delete_row()
    add_row()
    print("ok")

def reset_form():
    i=0
    for item in df.columns:
        txs[i].delete(0, "end")
        txs[i].insert(0, "")
        i+=1
def search_data():
    mx=0
    mn=0
    s_name=formseach.get().strip()
    s_max=fmax.get().strip()
    s_min=fmin.get().strip()
    s_cate=fcate.get()
    
    if(s_max != ''):
        mx=float(s_max)
    if(s_min != ''):
        mn=float(s_min)
    print(s_cate)

    dfs=df
    if(s_cate!=''):
        dfs=dfs.loc[df['type_name'].str.contains(s_cate)]
    if (s_name!=''):
     dfs=dfs.loc[df['name'].str.contains(s_name)]
    
    if (mx != 0):
        if (mx>=mn):
          dfs= dfs.loc[df['price'].between(mn, mx)]
    f_data(dfs)
    
win = tk.Tk()
win.title("Frame Example")
win.config(bg="skyblue")

# Create Frame widget
left_frame = Frame(win, width=500, height=700)
left_frame.grid(row=2, column=0, padx=10, pady=5)

inf_frame = Frame(left_frame, bg="purple")
inf_frame.grid(row=2, column=0, padx=5, pady=5, columnspan=4)


right_frame = Frame(win, width=700, height=400, bg='grey')
right_frame.grid(row=2, column=1, padx=10, pady=5,rowspan=2)

# Create frames and labels in left_frame


# Create label above the tool_bar
Label(left_frame, text="Profuct detail").grid(row=1, column=0, padx=5, pady=5)
# Tạo label cho tiêu đề


title_label = tk.Label(win, text="Quản lý sản phẩm",bg="skyblue")
title_label.config(font=("Arial", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=2)

# Tạo nút thêm sản phẩm







treeview = ttk.Treeview(right_frame,)
treeview.grid(row=0,column=0,rowspan=2, padx=5, pady=5)




# Tạo bảng để hiển thị danh sách sản phẩm



# Tạo các cột cho bảng




product_info_frame = Frame(inf_frame)
product_info_frame.grid(row=2, column=3)
# Tạo các label cho thông tin sản phẩm



# Thêm sự kiện cho bảng

treeview.bind('<<TreeviewSelect>>', on_product_selected)
product_info_frame.config(borderwidth=1, relief="solid")

treeview.pack()

# Tạo các dòng cho bảng
#treeview.configure(yscrollcommand=self.scrollbar.set)
pro = dt.read_data("products.csv")
_cate =dt.read_data("category.csv")
df=pd.merge(left=pro, right=_cate, on='type_code')


treeview["columns"] = list(df.columns)
for column in treeview["columns"]:
    treeview.column(column,width=150)

for column in treeview["columns"]:
    treeview.heading(column, text=column)
    

df_rows = df.to_numpy().tolist()
for row in df_rows:
  
    treeview.insert('', "end", values=row)

for col in list(df.columns):
    treeview.heading(col, command=lambda c=col: sort_col(c))


# Thêm các cột cho bảng
i=0
txs=list()
for item in list(df.columns):
    lb=tk.Label(product_info_frame, text=item+":")
    lb.grid(row=i, column=0)
    entry = tk.Entry(product_info_frame,width=30 )
    
    entry.grid(row=i, column=1)
    txs.append(entry)
    i+=1
cate_options=ttk.Combobox(product_info_frame, width=20)
cate_options.grid(row=len(df.columns)+1, column=1)
cate_options["values"] =  list(_cate['type_name'])
cate_options.bind("<<ComboboxSelected>>", on_combobox_change)

btn_add=tk.Button(left_frame, text="Thêm", command=add_row)
btn_add.grid(row=3,column=0)
btn_reset=tk.Button(left_frame, text="đặt lại", command=reset_form)
btn_reset.grid(row=3,column=1)
btn_updata=tk.Button(left_frame, text="cập nhập", command=update_row)
btn_updata.grid(row=3,column=2)
btn_delete=tk.Button(left_frame, text="xóa", command=delete_row)
btn_delete.grid(row=3,column=3)

btleft_frame=Frame(win, width=500, height=700)
btleft_frame.grid(row=3,column=0,padx=10, pady=5)

search_frame = Frame(btleft_frame)
search_frame.grid(row=3,column=0)

tsearch=tk.Label(search_frame, text="Search").grid(row=0, column=0,pady=5,columnspan=2)

tname=tk.Label(search_frame, text="Name").grid(row=1, column=0)
formseach=tk.Entry(search_frame,width=30  )
formseach.grid(row=1,column=1,padx=5)

fmin=tk.Entry(search_frame ,width=30 )
tmin=tk.Label(search_frame, text="Min Price").grid(row=2, column=0)
fmin.grid(row=2,column=1,padx=5)
fmax=tk.Entry(search_frame,width=30  )
tmax=tk.Label(search_frame, text="Max Price").grid(row=3, column=0)
fmax.grid(row=3,column=1,padx=5)
tcate=tk.Label(search_frame, text="Type").grid(row=4, column=0)
fcate=ttk.Combobox(search_frame)
fcate.grid(row=4, column=1)
fcate["values"] =  list(_cate['type_name'])




re_button = tk.Button(search_frame, text="reload", command=re_data)
re_button.grid(row=5, column=1)

search_button = tk.Button(search_frame, text="Search", command=search_data)
search_button.grid(row=5, column=0)



sell_frame = Frame(win)
sell_frame.grid(row=4,column=1)











  



win.mainloop()
