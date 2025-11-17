def count(n):
    return 1 if n < 10 else 1 + count(n // 10)

print(count(int(input())))
