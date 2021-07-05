# ikki o'lchovli matrixning juft elementlarini chiqarish

a = [[1, 2], [3, 4]]
for i in range(2):
    for j in range(2):
        if a[i][j] % 2 == 0:
            a[i][j] = int(a[i][j] / 2)
        elif a[i][j] % 2 == 1:
            a[i][j] = a[i][j] * 2
print(a)
