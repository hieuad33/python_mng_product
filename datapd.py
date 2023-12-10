import pandas as pd


    
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
    data.loc[len(data.index)] = [str(name),int(quantity), str(code),float(price),str(product_type)] 

    print(data)
    save_data(data)
