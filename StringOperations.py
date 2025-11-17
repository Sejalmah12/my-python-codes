A = input()
A = A + A
A = ''.join(c for c in A if not c.isupper())
A = ''.join('#' if c in 'aeiou' else c for c in A)
print(A)