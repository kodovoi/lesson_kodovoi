first = int(input('введите первое число: '))
second = int(input('введите второе число: '))
third = int(input('введите третие число: '))
if first == second == third :
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
