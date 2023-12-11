import tkinter as tk

# Tạo cửa sổ
root = tk.Tk()

# Tạo nhãn cho ô mã sản phẩm
label_ma_san_pham = tk.Label(root, text="Mã sản phẩm")

# Tạo ô nhập mã sản phẩm
entry_ma_san_pham = tk.Entry(root)

# Tạo nhãn cho ô tên sản phẩm
label_ten_san_pham = tk.Label(root, text="Tên sản phẩm")

# Tạo ô nhập tên sản phẩm
entry_ten_san_pham = tk.Entry(root)

# Tạo nhãn cho ô số lượng
label_so_luong = tk.Label(root, text="Số lượng")

# Tạo ô nhập số lượng
entry_so_luong = tk.Entry(root)

# Tạo nhãn cho ô ngày bán
label_ngay_ban = tk.Label(root, text="Ngày bán")

# Tạo ô chọn ngày bán
entry_ngay_ban = tk.Entry(root, width=10)

# Tạo nút "Thêm"
button_them = tk.Button(root, text="Thêm")

# Sắp xếp các widget
label_ma_san_pham.grid(row=0, column=0)
entry_ma_san_pham.grid(row=0, column=1)
label_ten_san_pham.grid(row=1, column=0)
entry_ten_san_pham.grid(row=1, column=1)
label_so_luong.grid(row=2, column=0)
entry_so_luong.grid(row=2, column=1)
label_ngay_ban.grid(row=3, column=0)
entry_ngay_ban.grid(row=3, column=1)
button_them.grid(row=4, column=1)

# Bắt sự kiện khi nhấn nút "Thêm"
def on_click_them():
    # Lấy dữ liệu từ các ô nhập
    ma_san_pham = entry_ma_san_pham.get()
    ten_san_pham = entry_ten_san_pham.get()
    so_luong = entry_so_luong.get()
    ngay_ban = entry_ngay_ban.get()

    # In thông tin đã nhập
    print(f"Mã sản phẩm: {ma_san_pham}")
    print(f"Tên sản phẩm: {ten_san_pham}")
    print(f"Số lượng: {so_luong}")
    print(f"Ngày bán: {ngay_ban}")

button_them.config(command=on_click_them)

# Chạy cửa sổ



root.mainloop()
