# sonlar = [0, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for son in sonlar:
#     print(son)
#
# for son in range(10): # range(a)  0 dan a gacha bo'lgan sonlarni ketma-ket chiqarish
#     print(son)



# # range yordamida 1 dan 11 gacha sonlarning orasidan 7 va 9 soni chiqmasligi
# for son in range(1, 11): # range(a, b)  a dan b gacha bo'lgan sonlarni ketma-ket chiqarish
#     if son == 7 or son==9:
#         continue
#     print(son)


# # 2 dan 15 gacha sonlarni
# for son in range(2, 15, 2): # range(a, b, a)  a dan b gacha bo'lgan sonlarni ketma-ket chiqarish
#     print(son)


# range yordamida 1 dan 10 gacha sonlarning orasidan ,1,2,3,4,5 bilan tugaydigan sonlarni chiqmasligi
for son in range(1, 101): # range(a, b)  a dan b gacha bo'lgan sonlarni ketma-ket chiqarish
    if son % 10 <=5 and son//10>0:
        continue
    print(son)