def rev(s):
    return s if s == "" else rev(s[1:]) + s[0]

print(rev(input()))