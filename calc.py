import tkinter as tk

window = tk.Tk()

window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False,False)# Ограничиваем размер окна
button_add = tk.Button(window, text="+", width = 5, height = 6)
button_add.place(x = 50, y = 140)
button_sub = tk.Button(window, text="-", width=5, height=6)
button_sub.place(x = 110, y = 140)
button_mul = tk.Button(window, text="*", width=5, height=6)
button_mul.place(x = 200, y = 140)
button_div = tk.Button(window, text="/", width=5, height=6)
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

