# 2x2 ro'yhat berilgan ana shu ro'yhatni 1 o'lchovli ro'yhatga o'zlashtirish
m = []
matrix = [[1, 2], [4, 5]]
for j in matrix: # anig ichidagi ro'yhatni oladi
    for i in j:  # olingan ro'yhatchani ichidagi elementni oladi
        m.append(i) # olingan ro'yhatni  i ga o'zlashtiriladi'
print(m)