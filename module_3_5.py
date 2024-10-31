def get_multiplied_digits(number):
    str_number = str(number)

    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)


result1 = get_multiplied_digits(40203) # 4*(2*3)
print(result1)
