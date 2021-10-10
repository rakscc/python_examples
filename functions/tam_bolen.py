
print(" Merhaba pozitif tam sayi bolme hosgeldiniz")

tam_bolenler = []

def bolenler(number):
    for i in range(1,number+1):
        if ( number % i == 0 ):
            tam_bolenler.append(i)

        else:
            continue
    print(tam_bolenler)



sayi = int(input("Degeri girin : "))

bolenler(sayi)
