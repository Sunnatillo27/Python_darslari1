# 3x3 matrix har bir elementi alohida qatorga chiqarsin.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 1-usul
for matrix in matrix:
    for i in matrix:
        print(i)
# 2- usul
for i in range(3):
    for j in range(3):
        print(matrix[i][j])
