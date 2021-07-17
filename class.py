class Xodim:
    def __init__(self, ismi, manzili, maoshi):
        self.ismi = ismi
        self.manzili = manzili
        self.maoshi = maoshi

    def gap(self):
        if self.maoshi < 1000000:
            print(f"Mening ismim {self.ismi} maoshim {self.maoshi} so'm sal kamroq boriga shukur")
        else:
            print(f"Mening ismi {self.ismi} maoshim {self.maoshi} so'm")


xodimlar = []
n = int(input("xodimlar soni="))
for i in range(n):
    print(f"{i + 1}-xodim")
    ism = input("ism-")
    manzil = input("manzil-")
    maoshi = int(input("maoshi-"))
    xodimlar.append(Xodim(ismi=ism, manzili=manzil, maoshi=maoshi))
for xodim in xodimlar:
    xodim.gap()
