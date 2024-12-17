def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        result[func.__name__] = func(int_list)
    return result

def custom_max(lst):
    return max(lst)

def custom_min(lst):
    return min(lst)

def custom_len(lst):
    return len(lst)

def custom_sum(lst):
    return sum(lst)

def custom_sorted(lst):
    return sorted(lst)


print(apply_all_func([6, 20, 15, 9], custom_max, custom_min))
print(apply_all_func([6, 20, 15, 9], custom_len, custom_sum, custom_sorted))
