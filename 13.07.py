"""Xatoliklar bilan ishlash"""
# SyntaxError
# print ("hello"

# IdentationError:
# try:
# for i in range(5):
# print(i)
# NameError
# try:
#     ism = "Sunnatillo"
#     print(isim)
# except:
#     print("Xato -> NameError")
# valueError
# try:
#     x="1.2"
#     int(x)
# except:
#     print("ValueError")

# Xatoliklar bilash ishlash
# try:
#     y = 0
#     print("Salom")
# except:
#     y += 1
#     print("try dagi nimadur xato")
# finally:
#     if y==1:
#         print("Dasturda xato yo'q")
#     else:
#         print("Dasturda xato bor")
n = int(input("raqam kiriting "))
try:
    y = 0
except:
    y += 1
    print("try dagi nimadur xato")
finally:
    if y % 2 == 0:
        print("Dasturda xato bor")

        if y % 2 == 1:
            print("Dasturda xato yo'q")
