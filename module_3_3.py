def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(3)
print_params(8,9)
print_params(b = 25)
print_params(c=[1, 2, 3])

values_list = [333, 'integer', [5, 6, 7]]
values_dict = {'a':13, 'b': False, 'c': 'слово'}

print_params (*values_list)
print_params(**values_dict)

values_list_2 = ['int', 666]

print_params(*values_list_2, 42)