import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_lower = lower_var.get()
    include_upper = upper_var.get()
    include_digit = digit_var.get()
    include_symbol = symbol_var.get()

    characters = ''
    if include_lower:
        characters += string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digit:
        characters += string.digits
    if include_symbol:
        characters += string.punctuation

    if not characters:
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, "请选择至少一种字符类型")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def increase_length(event):
    current_length = int(length_entry.get())
    new_length = current_length + 1
    length_entry.delete(0, tk.END)
    length_entry.insert(0, str(new_length))

def decrease_length(event):
    current_length = int(length_entry.get())
    new_length = max(current_length - 1, 1)  # 限制最小长度为1
    length_entry.delete(0, tk.END)
    length_entry.insert(0, str(new_length))
def handle_enter(event):
    generate_password()

# 创建主窗口
window = tk.Tk()
window.title("Passwd")

# 创建密码长度标签和输入框
length_label = tk.Label(window, text="密码长度：")
length_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)
length_entry = tk.Entry(window, width=12)
length_entry.insert(tk.END, "8")
length_entry.grid(row=0, column=1, padx=10, pady=10)

# 创建密码字符类型选择复选框
lower_var = tk.IntVar()
lower_var.set(1)
lower_checkbtn = tk.Checkbutton(window, text="小写字母", variable=lower_var)
lower_checkbtn.grid(row=1, column=0, sticky="W", padx=10, pady=5)

upper_var = tk.IntVar()
upper_var.set(1)
upper_checkbtn = tk.Checkbutton(window, text="大写字母", variable=upper_var)
upper_checkbtn.grid(row=1, column=1, sticky="W", padx=10, pady=5)

digit_var = tk.IntVar()
digit_var.set(1)
digit_checkbtn = tk.Checkbutton(window, text="数字", variable=digit_var)
digit_checkbtn.grid(row=2, column=0, sticky="W", padx=10, pady=5)

symbol_var = tk.IntVar()
symbol_checkbtn = tk.Checkbutton(window, text="符号", variable=symbol_var)
symbol_checkbtn.grid(row=2, column=1, sticky="W", padx=10, pady=5)

# 创建密码生成按钮
generate_button = tk.Button(window, text="生成密码", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# 创建密码展示文本框
password_entry = tk.Entry(window, width=30)
password_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# 绑定上下键事件
length_entry.bind("<Up>", increase_length)
length_entry.bind("<Down>", decrease_length)
window.bind("<Return>", handle_enter)

# 禁止窗口调整大小
window.resizable(False, False)

# 运行主循环
window.mainloop()
