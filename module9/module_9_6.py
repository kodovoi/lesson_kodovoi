def all_variants(text):
    length = len(text)

    for i in range(length):
        yield text[i]

    for i in range(length - 1):
        yield text[i:i+2]

    if length >= 3:
        yield text

# Пример использования функции
a = all_variants("abc")

for i in a:
    print(i)

