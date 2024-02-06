x, y, z = 0, 0, 0
n = int(input())
for i in range(n):
    v = input()
    v = v.split()
    x += int(v[0])
    y += int(v[1])
    z += int(v[2])
if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
