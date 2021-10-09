
print(" Atmye hosgeldiniz")

bakiye = int(1000)

while True:
    print("""
        Bakiye sorgulama icin : 1
        Para yatırma icin :     2
        Para cekmek icin :      3
        Atmden cikis yapmak icin lutfen 'cikis' yaziniz
    """)
    islem = input()
    if ( islem == "cikis" ):
        print(" Cikis yapilmistir. Tekrardan gorusmek uzere")
        break
    elif ( islem == "1" ):
        print(" Mevcut bakiyeniz : {}".format(bakiye))
    elif ( islem == "2" ):
        yatirma = abs(int(input(" Yatirilacak miktari girin")))
        bakiye+= yatirma
        print(" {} tl yatirilmistir. Guncel bakiyeniz : {} ".format(yatirma,bakiye))
    elif ( islem == "3" ):
        cekme = abs(int(input(" Cekilecek miktari girin")))
        if ( bakiye - cekme < 0 ):
            print( " HATA! Yeterli bakiyeniz bulunmamaktadir. En fazla {} tl cekebilirsiniz ".format(bakiye))
        else:
            print(" {} tl cekilmistir. Mevcut bakiyeniz {} tldir".format(cekme,bakiye-cekme))
    else:
        print(" Lutfen dogru deger giriniz")
        break
