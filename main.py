# gui.py
import datapd as dt
import pandas as pd
from tkinter import *
import tkinter as tk
import bd 
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np




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
     
    entry_ma_san_pham.delete(0, "end")
    entry_ma_san_pham.insert(0, product[0])

    entry_ten_san_pham.delete(0, "end")
    entry_ten_san_pham.insert(0, product[1])
    


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


treeview = ttk.Treeview(right_frame,)
treeview.grid(row=0,column=0,rowspan=2, padx=5, pady=5)

product_info_frame = Frame(inf_frame)
product_info_frame.grid(row=2, column=3)

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

sell_form_frame = Frame(sell_frame)
sell_form_frame.grid(row=0,column=0)

label_ma_san_pham = tk.Label(sell_form_frame, text="Mã sản phẩm")

# Tạo ô nhập mã sản phẩm
entry_ma_san_pham = tk.Entry(sell_form_frame)

# Tạo nhãn cho ô tên sản phẩm
label_ten_san_pham = tk.Label(sell_form_frame, text="Tên sản phẩm")

# Tạo ô nhập tên sản phẩm
entry_ten_san_pham = tk.Entry(sell_form_frame)

# Tạo nhãn cho ô số lượng
label_so_luong = tk.Label(sell_form_frame, text="Số lượng")

# Tạo ô nhập số lượng
entry_so_luong = tk.Entry(sell_form_frame)

# Tạo nhãn cho ô ngày bán
label_ngay_ban = tk.Label(sell_form_frame, text="Ngày bán")

# Tạo ô chọn ngày bán
entry_ngay_ban = tk.Entry(sell_form_frame, width=10)

# Tạo nút "Thêm"
button_them = tk.Button(sell_form_frame, text="Thêm")

# Sắp xếp các widget
label_titlesell = tk.Label(sell_form_frame, text="Bán hàng").grid(row=0, column=0,columnspan=2)
label_ma_san_pham.grid(row=1, column=0)
entry_ma_san_pham.grid(row=1, column=1)
label_ten_san_pham.grid(row=2, column=0)
entry_ten_san_pham.grid(row=2, column=1)
label_so_luong.grid(row=3, column=0)
entry_so_luong.grid(row=3, column=1)
label_ngay_ban.grid(row=4, column=0)
entry_ngay_ban.grid(row=4, column=1)
button_them.grid(row=5, column=1)



sell_table_frame=Frame(sell_frame)
sell_table_frame.grid(row=0,column=1)

selltreeview = ttk.Treeview(sell_table_frame)
selltreeview.pack(side="left", fill="both", expand=True)

sell=dt.read_data("sell_data.csv")



selltreeview["columns"] = list(sell.columns)
for column in selltreeview["columns"]:
    selltreeview.column(column,width=150)

for column in selltreeview["columns"]:
    selltreeview.heading(column, text=column)

sell_rows = sell.to_numpy().tolist()
for row in sell_rows:
    selltreeview.insert('', "end", values=row)

for col in list(sell.columns):
    selltreeview.heading(col, command=lambda c=col: sort_col(c))

def datasell():
    selltreeview.delete(*selltreeview.get_children()) 
    sell=dt.read_data("sell_data.csv")
    df_rows =sell.to_numpy().tolist()
    for row in df_rows:
        selltreeview.insert('', "end", values=row)
def on_click_them():
    # Lấy dữ liệu từ các ô nhập
    ma_san_pham = entry_ma_san_pham.get()
    so_luong = entry_so_luong.get()
    ngay_ban = entry_ngay_ban.get()

    sell.loc[len(sell)+1] = [str(ma_san_pham),str(so_luong),str(ngay_ban)] 

    dt.save_data(sell,fl='sell_data.csv')
    # In thông tin đã nhập
    print(f"Mã sản phẩm: {ma_san_pham}")
   
    print(f"Số lượng: {so_luong}")
    print(f"Ngày bán: {ngay_ban}")
    datasell()

button_them.config(command=on_click_them)


def show_plot_sell():
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6), tight_layout=True)
    product_df = pd.read_csv('products.csv')
    sell_df=pd.read_csv('sell_data.csv')
    data = pd.merge(left=product_df, right=sell_df, on='code')
    data=data.groupby(['code','name','price'])[['quantity_sell']].sum()
    colors = plt.cm.Set1.colors[:len(data)]
    # Vẽ biểu đồ cột

    axes[0].bar(data.index.get_level_values("name"), data['quantity_sell'],color=colors)
    axes[0].set_xlabel("Sản phẩm")
    axes[0].set_ylabel("Số lượng đơn hàng")
    axes[0].set_title("Số đơn hàng theo sản phẩm")
 
    data['sales_total']= data['quantity_sell']*data.index.get_level_values("price")  
   
    axes[1].bar(data.index.get_level_values("name"), data['sales_total'], color=colors)
    axes[1].set_title("Giá trị sản phẩm đa bán theo sản phẩm")
    axes[1].set_xlabel("sản phẩm")
    axes[1].set_ylabel("tổng tiền")    
    # Hiển thị biểu đồ   
    plt.show()
def show_plot_pr():
    product_df = pd.read_csv('products.csv')
    category_df = pd.read_csv('category.csv')
    thong_ke = product_df.groupby('type_code')['quantity'].sum().sort_values(ascending=True)
   
    pr=product_df["price"].astype(np.int32)
    colors = plt.cm.Set1.colors[:len(product_df)]
    plt .bar(product_df["quantity"],pr, color=colors)
    plt.title("Số lượng sản phẩm theo mức giá")
    plt.xlabel("Mức giá")
    plt.ylabel("Số lượng")
    plt.show()


tk_frame=Frame(win, width=500, height=700)
tk_frame.grid(row=4,column=0)

label_ttk = tk.Label(tk_frame, text="Thống kê")
label_ttk.grid(row=0,column=0)

button_tk_type= tk.Button(tk_frame, text="theo loại sản phẩm", width=20)
button_tk_type.grid(row=1, column=0)
button_tk_type.config(command=bd.tk_typeprr)

button_tk_sell= tk.Button(tk_frame, text="thống kê bán hàng", width=20)
button_tk_sell.grid(row=2, column=0)
button_tk_sell.config(command=show_plot_sell)


button_tk_pr= tk.Button(tk_frame, text="theo mức giá", width=20)
button_tk_pr.grid(row=3, column=0)
button_tk_pr.config(command=show_plot_pr)













  



win.mainloop()
