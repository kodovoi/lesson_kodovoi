first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
third_result = first_strings + second_strings

first_result = [len(a) for a in first_strings if len(a) >= 5]
second_result = [(sl_1, sl_2) for sl_1 in first_strings for sl_2 in second_strings if len(sl_1) == len(sl_2)]
third_result = {a: len(a) for a in third_result if len(a) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
