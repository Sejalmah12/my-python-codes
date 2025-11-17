def inc(n):
    if n == 0: return
    inc(n-1)
    print(n, end=" ")

inc(int(input()))