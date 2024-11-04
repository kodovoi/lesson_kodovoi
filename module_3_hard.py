data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum (*args):
    total_sum = 0
    def recurse(data):
        nonlocal total_sum

        if isinstance(data, (int, float)):
            total_sum += data

        elif isinstance(data, str):
            total_sum += len(data)

        elif isinstance(data, (list, tuple, set)):
            for element in data:
                recurse(element)

        elif isinstance(data, dict):
            for key, value in data.items():
                recurse(str(key))
                recurse(value)

    for arg in args:
        recurse(arg)

    return total_sum
result = calculate_structure_sum(*data_structure)
print(result)

