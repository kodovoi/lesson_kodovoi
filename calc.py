import tkinter as tk

window = tk.Tk()

window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False,False)# Ограничиваем размер окна
button_add = tk.Button(window, text="+", width = 2, height = 2)
button_add.place(x = 80, y = 200)
button_sub = tk.Button(window, text="-", width=2, height=2)
button_sub.place(x = 150, y = 200)
button_mul = tk.Button(window, text="*", width=2, height=2)
button_mul.place(x = 200, y = 200)
button_div = tk.Button(window, text="/", width=2, height=2)
button_div.place(x = 250, y = 200)
number1_entry = tk.Entry(window, width=29)
number1_entry.place(x = 100, y = 75)
number2_entry = tk.Entry(window, width=29)
number2_entry.place(x = 100, y = 150)
answer_entry = tk.Entry(window, width=29)
answer_entry.place(x = 100, y = 300)
namber1 = tk.Label(window, text="Введите первое число")
namber1.place(x = 100, y = 50)
namber2 = tk.Label(window, text="Введите второе число")
namber2.place(x = 100, y = 125)
answer = tk.Label(window, text="Ответ")
answer.place(x = 100, y = 275)
window.mainloop()

