#

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
result = []
x = 0
while x < len(my_list):
    if my_list[x] < 0:
        break
    if my_list[x] > 0:
        result.append(my_list[x])
    x += 1
print(result)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for i in (numbers):
#     if i == 1:
#         continue
#     is_prime = True
#     if i < 2:
#         is_prime = False
#
#     for j in range (2, int(i**0.5)+1):
#         if i % j == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         primes.append(i)
#     else:
#         not_primes.append(i)
# print(primes)
# print(not_primes)






# def print_params(*params):
#     print(params)
#
#
# print_params(1,2,3,4,5,6,7)


# def print_params(a,b,c):
#     print(a, b, c)
#
# list_ = [1, 2, 3]
# print_params(list_, 2, 3)


# def print_params(a,b,c):
#     print(a, b, c)
#
# list_ = [1, 2, 3]
# print_params(*list_)

#
# def print_params(a,b,c):
#     print(a, b, c)
#
# doct_ = {'a': 1, 'b': 2, 'c': 3}
# print_params(**doct_)


# максимум в списке
# def test_max(list_):
#     max = 0
#     for i in list_:
#         if i > max:
#             max = i
#     return max
# print(test_max([22, 34, 56, 789]))
#
#
# #подсчёт чётных чисел в списке
#
# def chet_int(list_):
#     x = 0
#     for i in list_:
#         if i == 0:
#             continue
#         if i % 2 == 0:
#             x+=1
#     return x
#
# print(chet_int([2,6,5,9,8,4,0]))
#
#
# # УНИКАЛЬНЫЕ ЧИСЛА
# list_ = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
#
# def unique(list_):
#     new_list = []
#     for i in list_:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
#
# print(unique(list_))