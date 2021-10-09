print("""
************************************************************

Geometri seklini bulmaya hosgeldiniz

************************************************************

""")

print("""
Geometri sekliniz ucgen mi dortgen mi ?
Ucgen ise 1 yaziniz.
Dorgen ise 2 yaziniz.
""")

cevap_sekil = int(input())

if ( cevap_sekil == 1):
    a = abs(int(input("Lutfen ucgenin birinci kenarini giriniz")))
    b = abs(int(input("Lufen ucgenin ikinci kenarini giriniz")))
    c = abs(int(input("Lutfen ucgenin ucuncu kenarini giriniz")))
    if ((abs(b-c) < a < b+c ) and (abs(a-c) < b < a+c) and (abs(a-b) < c < a+b)):
        print(" Tebrikler dogru ucgen girdiniz ")
        if( a == b == c):
            print("Girdiginiz degerlere gore Eskenar Ucgen")
        elif( a == b or a == c or b == c):
            print("Girdiginiz degerlere gore Ikızkenar Ucgen")
        else:
            print("Girdiginiz degerlere gore Normal Ucgen")

    else:
        print(" Girdiginiz degerler ucgen olusturmuyor! ")


elif ( cevap_sekil == 2):
    x = abs(int(input("Dortgenin birinci kenarini giriniz")))
    y = abs(int(input("Dortgenin ikinci kenarini giriniz")))
    z = abs(int(input("Dortgenin ucuncu kenarini giriniz")))
    w = abs(int(input("Dortgenin dorduncu kenarini giriniz")))
    if( x == y == z == w):
        print("Girdiginiz degerlere gore Karedir")
    elif ( (x == y and z == w ) or ( x == z and y == w) or ( x == w and y == z)):
        print("Girdiğiniz degerlere gore Diktortgen")
    else:
        print("Girdiğiniz degerlere gore Dortgen")

else:
    print("Hatalı degerler giriyorsun!")
