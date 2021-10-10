
def asalmi(number):
    if ( number == 1 ):
        print("{} sayisi asal degildir ".format(number))
        return
    elif ( number == 2 ):
        print("{} sayisi asaldır".format(number))
        return
    else:
        for i in range(2,number):
            if ( number % i == 0 ):
                print("{} sayisi asal degildir".format(number))
                return
            else:
                print("{} sayisi asal sayidir".format(number))
                return 

print("Merhaba Asal sayi hesaplamasina hos geldiniz"
      "Cikis yapmak icin 'q' degerini girin")
while True:
    sayi = input("Sayi: ")
    if ( sayi  == 'q'):
        print(" Programdan cikis yapiliyor")
        break
    else:
        sayi = int(sayi)
        asalmi(sayi)

