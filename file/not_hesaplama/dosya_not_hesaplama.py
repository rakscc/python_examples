
def not_hesaplama(satir):

    satir = satir[:-1]

    liste = satir.split(",")
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    ogrenci_notu = int(not1*0.3 + not2*0.3 + not3*0.4)

    if (ogrenci_notu >= 90):

        harf = "AA"
    elif (ogrenci_notu >= 85):
        harf = "BA"
    elif (ogrenci_notu >= 80):
        harf = "BB"
    elif (ogrenci_notu >= 75):
        harf = "CB"
    elif (ogrenci_notu >= 70):
        harf = "CC"
    elif (ogrenci_notu >= 65):
        harf = "DC"
    elif (ogrenci_notu >= 60):
        harf = "DD"
    elif (ogrenci_notu >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + " ------------->" + harf + "\n"




with open("C:\\Users\\halil\Desktop\\dosya_okuma\\bilgiler.txt","r",encoding= "utf-8") as file:

    eklenecekler_listesi = []

    for i in file:
        eklenecekler_listesi.append(not_hesaplama(i))

    with open("C:\\Users\\halil\Desktop\\dosya_okuma\\notlar.txt", "w", encoding="utf-8") as file2:

        for j in eklenecekler_listesi:
            file2.write(j)
