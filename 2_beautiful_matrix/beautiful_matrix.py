matrix = []
for i in range(5):
    matrix.append([])
    a = input()
    a = a.split()
    for j in range(5):
        matrix[i].append(int(a[j]))

# 1 should go to matrix[2][2]
ii, jj = 0, 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            if i < 2:
                ii = 2 - i
            else:
                ii = i - 2
            if j < 2:
                jj = 2 - j
            else:
                jj = j - 2

print(ii + jj)
