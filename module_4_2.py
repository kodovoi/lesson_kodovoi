def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызываю inner_function внутри test_function
    inner_function()

# Вызываю inner_function вне test_function
#inner_function()
# Получаем ошибку : NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

# Вызов test_function, чтобы увидеть результат
test_function()

# Попробую вызвать inner_function вне test_function
try:
    inner_function()
except NameError as e:
    print("Ошибка:", e)