numbers = (10, 2, 3, 4, 5, 6)
#
maks = max(numbers)
minimum = min(numbers)
print(maks + minimum)

 # urta arifnetigini topish
urta_arif = sum(numbers) / len(numbers)

print(urta_arif)

# boshqacha usul

i = 0
summa = 0
for number in numbers:
    i += 1
    summa += number

urta_arifmetik = summa / 1
print(urta_arifmetik)
