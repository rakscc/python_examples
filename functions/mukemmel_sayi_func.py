
def mukemmel_mi(sayi):
    toplam = 0

    for i in range(1, sayi):

        if (sayi % i == 0):
            toplam += i

    return toplam == sayi

for i in range(1,1001):
    if( mukemmel_mi(i)):
        print(i)
  