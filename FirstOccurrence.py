A = input()
B = int(input())
ch = chr(B)
print(A.find(ch) if ch in A else -1)