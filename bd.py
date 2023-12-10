import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# Tạo dữ liệu
x = np.arange(0, 10)
y = x ** 2

# Tạo giao diện người dùng
root = tk.Tk()

# Tạo canvas
canvas = tk.Canvas(root, width=500, height=500)

# Vẽ biểu đồ đường
plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Thêm canvas vào giao diện người dùng
canvas.pack()

# Cập nhật biểu đồ đường mỗi giây
def update_graph():
    global x, y

    x = x + 1
    y = x ** 2

    # Vẽ biểu đồ đường mới
    plt.cla()
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    # Đặt lại thời gian chờ
    canvas.after(1000, update_graph)

# Khởi động vòng lặp chính
update_graph()
root.mainloop()
