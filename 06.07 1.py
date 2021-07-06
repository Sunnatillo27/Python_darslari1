numbers = (1, 2, 3, 4) # bu kortej -> tuple
numbers1 = [1, 2, 3, 4]# bu kortej -> list

print(type(numbers))
print(type(numbers1))

"""konstruktor"""
a = tuple([1, 2, 3, 4])
print(type(a))

"""kortej elementlarga murojaat"""
numbers = (1, 2, 3, 4)
print(numbers[3])
# bu amallar index lar orqali amalga oshiriladi

"""kortejni yangilashni faqat ro'yhatga o'tkazib keyin bajarsa bo'ladi"""
numbers = (1, 2, 3, 4)

# avval korejni ro'yhatga aylantiramiz
numbers = list(numbers)

# endi yangilymiz
numbers[1]=9

numbers = tuple(numbers)
print(numbers)

