
print(" faktoriyel hesaplamaya hosgeldiniz")

fak = input("lütfen hesaplanacak faktoriyel sayisini giriniz"
                "cıkmak icin q tusuna basın")

while True:
    if ( fak == "q" ):
        print(" programdan cikis yapiliyor")
        break

    
    fak = int(fak)

    faktoriyel = 1
    for i in range(2,fak+1):
        faktoriyel *= i

    print(" {} sayisiniz faktoriyeli {} 'dir".format(fak,faktoriyel))
    break

