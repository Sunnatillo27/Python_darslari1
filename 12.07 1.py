# # # # a = int(input('a=:'))
# # # # b = int(input('b=:'))
# # # #
# # # #
# # # # def qushish(a, b):
# # # #     return a + b
# # # #
# # # #
# # # # def urta_arifmetik():
# # # #     return qushish(a, b) / 2  #ikki sonning o'rta arifmetigini chiqarish
# # # #
# # # #
# # # # print(urta_arifmetik())
# # # #
# # # n = int(input('n='))
# # #
# # #
# # # def myfunction(n):
# # #     qiymat = []
# # #     for i in range(1, n):
# # #         if i ** 2 < n:
# # #             qiymat.append(i)
# # #     return qiymat
# # #
# # # print(myfunction(n))
# # #
# # # 1-misol
# # # n = int(input('n='))
# # # def chiziq(n):
# # #     txt = ''
# # #     for i in range(n): 9-sinf misol
# # #         txt += '*'
# # #     print(txt)
# # #
# # #
# # # chiziq(n)
# #
# # # 2-misol
# # n = int(input('n='))
# #
# # 1-usul
# # def yulduzcha(n):
# #     for i in range(n):  # 9-sinf misol
# #         print(n * '*')
# #
# #
# # yulduzcha(n)
#
# # 2-usul
# # n = int(input('n='))
# # def yulduzcha_2(n):
# #     print((n*'*'+'\n')*n) 9-sinf misol 2 usul
# #
# # yulduzcha_2(n)
#
#
# # 2-masala 9-sinf darslik
# n = int(input('n='))
#
#
# def buluchilar(a):
#     txt = ''
#     for i in range(1, a + 1):
#         if a % i == 0:
#             txt += str(i) + ' ' # 9-sinf darslik sonning bo'luvchilarini topish va natija orasida probel tashlash
#     print(txt)
#
#
# buluchilar(n)

# 4 masala 9-sinf misol darslik
# 1 - usul
# n = int(input('n='))
#
#
# def xonayigindi(a):
#     bir = a % 10
#     un = a // 10 % 10
#     yuz = a // 100 % 10
#     print(bir + un + yuz)
#
#
# xonayigindi(n)


# 2-usul
# n = int(input('n='))


# def xona_yigindi(a):
#     yigindi = 0
#     for i in range(len(str(a))):
#         yigindi += a // (10 ** i) % 10
#
#     print(yigindi)

# 3-usul
# def xona_yigindi1(a):
#     summa = 0
#     a = str(a)
#     for i in a:
#         summa += int(i) #125=8
#     print(summa)
#
#
# xona_yigindi1(n)

n = int(input('n='))


def xona_soni(a):
   return len(str(a))
print(xona_soni(n))