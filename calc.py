import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_vales(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_vales(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_vales(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_vales(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_vales(res)



window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False,False)# Ограничиваем размер окна
button_add = tk.Button(window, text="+", width = 5, height = 6, command=add)
button_add.place(x = 50, y = 140)
button_sub = tk.Button(window, text="-", width=5, height=6, command=sub)
button_sub.place(x = 110, y = 140)
button_mul = tk.Button(window, text="*", width=5, height=6, command=div)
button_mul.place(x = 200, y = 140)
button_div = tk.Button(window, text="/", width=5, height=6, command=mul)
button_div.place(x = 260, y = 140)
number1_entry = tk.Entry(window, width=13)
number1_entry.place(x = 50, y = 75)
number2_entry = tk.Entry(window, width=13)
number2_entry.place(x = 220, y = 75)
answer_entry = tk.Entry(window, width=29)
answer_entry.place(x = 90, y = 280)
namber1 = tk.Label(window, text="Первое число")
namber1.place(x = 50, y = 50)
namber2 = tk.Label(window, text="Второе число")
namber2.place(x = 220, y = 50)
answer = tk.Label(window, text="Ответ:")
answer.place(x = 160, y = 255)
window.mainloop()

