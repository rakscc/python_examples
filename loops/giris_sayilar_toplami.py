
print(" dongu toplamına hosgeldiniz "
      "sirayla sayilari girin"
      "eger toplamak ve cikis yapmak istiyorsanız 'q' ya basiniz")


toplam = 0
while True:
    sayi = input()
    if ( sayi == "q" ):
        break
    toplam += int(sayi)

print(" cikis yapiliyor sayilarin toplami : ",toplam)

