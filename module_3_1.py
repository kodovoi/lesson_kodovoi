calls = 0

def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)


def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list_to_search)



info = string_info("Hello World")
info1 = string_info("Alexander")
print("String Info:", info)
print("String Info:", info1)

contains = is_contains("UrbaN", ["urban", "city", "town"])
contains1 = is_contains("BitcoIN", ["urban", "city", "town"])


print("Contains 'UrbaN' in list:", contains)
print("Contains 'BitcoiN' in list:", contains1)
print("Total function calls:", calls)
