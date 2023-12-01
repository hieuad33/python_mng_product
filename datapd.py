import pandas as pd
def initdata():
    inout_data = pd.DataFrame({
    'name': ['Sản phẩm 1', 'Sản phẩm 2', 'Sản phẩm 3'],
    'quantity': [10, 20, 30],
    'code': ['ABC123', 'DEF456', 'GHI789'],
    'price':[10, 20, 30] ,
    'product_type': ['Thiết bị điện', 'Thiết bị điện tử', 'Thiết bị gia dụng']
    })
   
    save_data(inout_data)

def add_category(cates,newcate):
    cates.append({
        'name': newcate
         })
def save_category(cates):
    data.to_csv('categotys.csv')
def save_data(data,fl='products.csv'):
    data.to_csv(fl)
def delete_data(product_data,data):
    product_data = product_data.drop(data)
def read_data(fl='products.csv',keyid=0):
    data = pd.read_csv(fl, index_col=keyid)
    return data

def show_data(data):
    print(data.to_string())


def delete_row(data,index):
    return data.pop(index)
def add_pr(code,name,quantity,price,product_type):
        # Thêm dữ liệu
    data=read_data()
   
    new_row = pd.Series({"code": code, "name": name, "quantity": quantity, "price": price, "product_type": product_type})
    print(new_row)
    data = pd.concat([data, new_row.to_frame()], ignore_index=True)
    print(data)
    save_data(data)
initdata() 