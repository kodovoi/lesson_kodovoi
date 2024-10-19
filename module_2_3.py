my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
result = []
x = 0
while x < len(my_list):
    if my_list[x] < 0:
        break
    result.append(my_list[x])
    x += 1
print(result)
