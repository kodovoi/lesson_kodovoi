def generate_password(n):
    pairs = []

    for i in range(1, n):  # i от 1 до n-1
        for j in range(i + 1, n + 1):  # j от i+1 до n
            pairs.append((i, j))

    password = ''
    for a, b in pairs:
        pair_sum = a + b
        if n % pair_sum == 0:
            password += f"{a}{b}"

    return password

for i in range(3, 21):
    result = generate_password(i)
    print(f"{i} - {result}")
