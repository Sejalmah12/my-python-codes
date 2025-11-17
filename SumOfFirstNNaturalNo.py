def sumN(n):
    return 0 if n == 0 else n + sumN(n-1)

print(sumN(int(input())))