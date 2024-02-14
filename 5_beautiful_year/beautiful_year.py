def distinct(x):
    digits = set()
    while x != 0:
        d = x % 10
        x = x // 10
        if d in digits:
            return False
        digits.add(d)
    return True


n = int(input())
i = n + 1
while True:
    if distinct(i):
        print(i)
        break
    else:
        i = i + 1
