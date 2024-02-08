s = input()
i = 0
r = ""
while i < len(s):
    if s[i] == ".":
        r += "0"
        i += 1
    elif i < len(s) - 1 and s[i] == "-":
        if s[i + 1] == ".":
            r += "1"
        else:
            r += "2"
        i += 2
print(r)