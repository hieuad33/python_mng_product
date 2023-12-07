import tkinter as tk
from tkinter import ttk
import pandas as pd

class Appcate(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pandas Table")
        self.df = pd.read_csv("products.csv")
        # Create Dropdown Menus
        self.search_options = ttk.Combobox(self, width=20)
        self.search_options["values"] =  list( self.df['product_type'].unique())
        self.search_options.pack(pady=10)


         # Create Search button
        self.search_button = ttk.Button(self, text="Search", command=self.search_data)
        self.search_button.pack(pady=10)
        
        # Create Treeview
        self.treeview = ttk.Treeview(self)
        self.treeview.pack(side="left", fill="both", expand=True)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.treeview.configure(yscrollcommand=self.scrollbar.set)

        # Load data
        self.df = pd.read_csv("products.csv")
        self.treeview["columns"] = list(self.df.columns)
        for column in self.treeview["columns"]:
            self.treeview.heading(column, text=column)
        self.df_rows = self.df.to_numpy().tolist()
        self.display_all_data()

        # Create Reload button
        self.reload_button = ttk.Button(self, text="Reload", command=self.reload_data)
        self.reload_button.pack(pady=10)

    def search_data(self):
        search_term = self.search_options.get() 
        filtered_data =  self.df[self.df['product_type'] ==str(search_term)].to_numpy().tolist()
        self.treeview.delete(*self.treeview.get_children())
        for row in filtered_data:
            self.treeview.insert("", "end", values=row)

    def display_all_data(self):
        self.treeview.delete(*self.treeview.get_children())
        for row in self.df_rows:
            self.treeview.insert("", "end", values=row)

    def reload_data(self):
        self.df = pd.read_csv("products.csv")
        self.treeview["columns"] = list(self.df.columns)
        for column in self.treeview["columns"]:
            self.treeview.heading(column, text=column)
        self.df_rows = self.df.to_numpy().tolist()
        self.display_all_data()
