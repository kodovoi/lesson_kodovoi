immutable_var = 1,2,'string',True
print ('Immutable tuple:',(immutable_var))
# immutable_var[1] = 3 Кортежи это неизменяемые последовательности, после создания кортежа элементы в нём нельзя изменить, добавить или удалить.
mutable_list = [13,26,'string',False]
mutable_list[:] = 33,76,'int',True
print('Mutable list:',(mutable_list))