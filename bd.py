import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Đọc dữ liệu từ file CSV
product_df = pd.read_csv('products.csv')
category_df = pd.read_csv('category.csv')
sell_df=pd.read_csv('sell_data.csv')

def map_typecode_to_typename(type_code):
    type_code = list(type_code)
    mapping_dict = dict(zip(category_df['type_code'], category_df['type_name']))
    mapped_values = map(mapping_dict.get, type_code)
    return list(mapped_values)

# Thống kê số lượng sản phẩm theo type_code và sắp xếp giảm dần
thong_ke = product_df.groupby('type_code')['quantity'].sum().sort_values(ascending=True)
gombang=pd.merge(left=product_df, right=category_df, on='type_code')
thong_ke = product_df.groupby('type_code')['quantity'].sum().sort_values(ascending=True)

# Tạo giao diện Tkinter



def tk_typeprr():
    
    window = tk.Tk()
    window.title("Thống kê số lượng sản phẩm và Biểu đồ Chấm Chấm")
    
    # Tạo Figure và Axes của Matplotlib với 1 dòng 3 cột
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 6), tight_layout=True)
    
    # Bảng màu cho cột và tròn
    colors = plt.cm.Set1.colors[:len(thong_ke)]
  
    # Subplot 1: Biểu đồ cột
    legends = map_typecode_to_typename(thong_ke.index)
    rects = axs[0].bar(legends, thong_ke, color=colors)
    axs[0].set_title('Biểu đồ cột - Số lượng sản phẩm theo loại')
    axs[0].set_xlabel('Loại sản phẩm')
    axs[0].set_ylabel('Số lượng sản phẩm')
    
    # Thêm chỉ số lượng cụ thể trên mỗi cột
    for rect, label in zip(rects, thong_ke):
        height = rect.get_height()
        axs[0].text(rect.get_x() + rect.get_width()/2, height, label,
                    ha='center', va='bottom')
    
    # Subplot 2: Biểu đồ tròn
    axs[1].pie(thong_ke, labels=legends, autopct='%1.1f%%', startangle=90, colors=colors)
    axs[1].set_title('Biểu đồ tròn - Số lượng sản phẩm theo loại')
    
    # Subplot 3: Biểu đồ chấm chấm
    
   
    sns.stripplot(x='type_name', y='price', data=gombang, ax=axs[2], palette='Set1', hue='type_name', jitter=True, dodge=True, legend=False)

    axs[2].set_title('Biểu đồ Chấm Chấm - Giá theo Loại sản phẩm')
    axs[2].set_xlabel('Loại sản phẩm')
    axs[2].set_ylabel('Giá')
    
    # Nhúng biểu đồ vào giao diện Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, padx=10, pady=10)
    
    # Chạy giao diện
    window.mainloop()



