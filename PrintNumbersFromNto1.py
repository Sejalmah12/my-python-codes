def dec(n):
    if n == 0: return
    print(n, end=" ")
    dec(n-1)

dec(int(input()))