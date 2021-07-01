sonlar = [8, 4, 5, 4, 1, 0, 9]

for index in range(len(sonlar)):
    for key in range(len(sonlar)):
        if sonlar[index] < sonlar[key]:
            sonlar[index]=sonlar[key]+sonlar[index]
            sonlar[key] = sonlar[index] - sonlar[key]
            sonlar[index] = sonlar[index] - sonlar[key]
            print(sonlar)
