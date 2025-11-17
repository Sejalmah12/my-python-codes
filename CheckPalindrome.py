def pal(s):
    return s if len(s) <= 1 else (pal(s[1:-1]) if s[0] == s[-1] else "no")

s = input()
print("Palindrome" if pal(s) != "no" else "Not Palindrome")