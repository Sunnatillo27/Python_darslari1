import datetime as dt  # as qisqacha nom berish buyug'i
from tkinter import *
import time
# while True:
#     print(datetime.datetime.now())

# print(dt.datetime.now().year)
import this

#vaqt = dt.datetime.now().second

# print(vaqt.year)  # yil
# print(vaqt.month)  # oy
# print(vaqt.day)  # kun
# print(vaqt.weekday())  # hafta kuni noldan boshlanadi
# print(vaqt.hour)  # soat
# print(vaqt.minute)  # minut
# print(vaqt.second)  # sekund
# print(vaqt.microsecond)  # mikrosekund
# print(vaqt.strftime("%a"))
# t = dt.datetime.now()


# def vaqt(t):
#     print(f"soat {t.hour}:{t.minute} bo'ldi")
#
#
#vaqt(t)
# while True:
#     if vaqt + 5 == dt.datetime.now().second: # 5 SEKUND dan keyin salom so'zi chiqishi
#         print("Salom")
#         this.c
#         break
class Frame(Tk):
    def __init__(self):
        self.canvas = c = Canvas(self, width=70, height=190, bg="black")