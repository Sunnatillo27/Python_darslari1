# # talaba = [{
# #     "ism": "Zilola",
# #     "kursi": 1,
# #     "bahosi": 5,
# #     "jinsi": "Ayol",
# #     "otasining_ismi": "Faxriddin"
# #     },
# #     {
# #     "ism": "Aziz",
# #     "kursi": 2,
# #     "bahosi": 4,
# #     "jinsi": "erkak",
# #     "otasining_ismi": "Dilshod"
# #     },
# #     {
# #     "ism": "Azim",
# #     "kursi": 2,
# #     "bahosi": 3,
# #     "jinsi": "erkak",
# #     "otasining_ismi": "Allanazar"
# #     }
# #     ]
# # # for i in talaba:
# # #     if i["ism"][0] == "A":
# # #         print(i)
# # yil = int(input("necha yil utdi----->"))
# # for i in talaba:
# #     i["kursi"] = yil + i["kursi"]
# #     print(i["kursi"])
# # shaxs = [{
# #     "ismi": "Farrux",
# #     "yoshi": 10,
# #     "o'quvchi": True
# # }]
# # yil = int(input("yil-----="))
# # for i in shaxs:
# #     i["yoshi"] = yil + i["yoshi"]
# #     if i["yoshi"] > 18:
# #         i["o'quvchi"] = False
# #         i.clear()
# #     print(i)
# talaba = { # 1 usul
#     "ism": "Zilola",
#     "yoshi": 22
# }
# if "yoshi" in talaba:
#     print("bor")
# else:
#     print("yo'q")
#
# talaba = { # 2 usul
#     "ism": "Zilola",
#     "yoshi": 22
# }
# for i in talaba:
#     if i == "yoshi":
#         print("bor")
#         break
# else:
#     print("yo'q")

# oila = {
#     "ota": {
#         "ism": "Anna",
#         "yoshi": 20
#     },
#     "bola": {
#         "ismi": "Devat",
#         "yoshi": 20
#     }
# }
# print(oila.get("bola").get("ismi"))
# print(oila["bola"]["ismi"])


EnUz = {
    "i": "men",
    "he": "U ""'ayol kishiga nisbatadan'"
}
suz = input("Inglizcha so'z kiriting: ")
suz = suz.lower()
if suz in EnUz.keys():
    print(EnUz[suz])

else:
    print("Bunday so'z lug'atda yo'q")