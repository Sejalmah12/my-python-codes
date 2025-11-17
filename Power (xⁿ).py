def power(x, n):
    return 1 if n == 0 else x * power(x, n-1)

x, n = map(int, input().split())
print(power(x, n))