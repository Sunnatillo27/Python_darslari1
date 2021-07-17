a = input("ism kiriting = ")
# b = int(input("b = "))
n = int(input("n = "))
# l = int(input("l = "))
# kv = lambda a, b, c, d: (a + b + c + d) / 4
# print(kv(a, b, c, d))
def dar(a):
   return lambda n: (a + ' ') * n
c = dar(a)
print(c(n))

