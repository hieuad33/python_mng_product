
import tkinter as tk
import datapd as dt
class formdata():
    def __init__(self):
        self.win = tk.Tk()
        self.code_entry = tk.Entry(self.win)
        self.code_entry.grid(row=0, column=1)
        self.name_entry = tk.Entry(self.win)
        self.name_entry.grid(row=1, column=1)
        self.cate_entry = tk.Entry(self.win)
        self.cate_entry.grid(row=2, column=1)
        self.price_entry = tk.Entry(self.win)
        self.price_entry.grid(row=3, column=1)
        self.quantity_entry = tk.Entry(self.win)
        self.quantity_entry.grid(row=4, column=1)
        # Tạo label cho tmax sản phẩm
        code_label = tk.Label(self.win, text="Mã sản phẩm:")
        code_label.grid(row=0, column=0)
        
        # Tạo entry cho tên sản phẩm    
        name_label = tk.Label(self.win, text="Tên sản phẩm:")
        name_label.grid(row=1, column=0)  
        # Tạo entry cho tên sản phẩm
        # Tạo label cho mô tả sản phẩm  
        cate_label = tk.Label(self.win, text="loại sản phẩm:")
        cate_label.grid(row=2, column=0)
    
        # Tạo entry cho loại sản phẩm
    
       
        # Tạo label cho giá sản phẩm
    
        price_label = tk.Label(self.win, text="Giá sản phẩm:")
        price_label.grid(row=3, column=0)
    
        # Tạo entry cho giá sản phẩm
    
       
        # Tạo label cho số lượng sản phẩm
    
        quantity_label = tk.Label(self.win, text="Số lượng sản phẩm:")
        quantity_label.grid(row=4, column=0)
    
        # Tạo entry cho số lượng sản phẩm
    
    
        # Tạo button để thêm sản phẩm
    
        submit_button = tk.Button(self.win, text="Thêm sản phẩm", command=self.on_submit)
        submit_button.grid(row=5, column=0, columnspan=2)
    
        self.win.mainloop()

    
    
    def on_submit(self):
        code= self.code_entry.get()
        name = self.name_entry.get()
        cate =self.cate_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        print(code)
        print(name)
        print(cate)
        print(price)
        print(quantity)
        dt.add_pr(code,name,quantity,price,cate)
    
        self.win.destroy()


  #  def data(code='',name='',qt='',type=''):
        
