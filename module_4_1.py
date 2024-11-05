from fake_math import divide as d_1
from true_math import divide as d_2

result_1 = d_1(69, 3)
result_2 = d_1(3, 0)
result_3 = d_2(49, 7)
result_4 = d_2(15, 0)

print(f'Результат 1: {result_1}')
print(f'Результат 2: {result_2}')
print(f'Результат 3: {result_3}')
print(f'Результат 4: {result_4}')