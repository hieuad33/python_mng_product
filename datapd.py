import pandas as pd
def finditembycode(df,code):
    a=df.loc[df["code"] == code]
    return a

def save_data(data,fl='products.csv'):
    data.to_csv(fl)
def delete_data(code):
    
    data=read_data()
    ind=finditembycode(data,code).index
    data = data.drop(ind)
    
    save_data(data,fl='products.csv')
    return data
                                    
def read_data(fl='products.csv',keyid=0):
    data = pd.read_csv(fl, index_col=keyid)
    return data

def show_data(data):
    print(data.to_string())



def add_pr(code,name,quantity,price,product_type):
        # Thêm dữ liệu
    tb=read_data("products.csv")
    
    tb.loc[len(tb)+1] = [str(code),str(name),int(quantity),float(price),int(product_type)] 

    
    save_data(tb)
    return tb
