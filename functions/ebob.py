
def ebob(sayi1,sayi2):

    bolenler_sayi1 = []
    bolenler_sayi2 = []

    gecici_sayi1 = 0
    gecici_sayi2 = 0

    for i in range(0,sayi1+1):
        gecici_sayi2 += sayi2
        bolenler_sayi1.append(gecici_sayi2)
    for j in range(0,sayi2+1):
        gecici_sayi1 += sayi1
        bolenler_sayi2.append(gecici_sayi1)

    ortaklar = list(set(bolenler_sayi1).intersection(bolenler_sayi2))

    ekoksonuc = min(ortaklar)

    print(ekoksonuc)

    return


sayi3 = int(input("sayi 1 : "))
sayi4 = int(input("sayi 2 : "))

ebob(sayi3,sayi4)

