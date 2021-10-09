
print("""
*******************************************************************

En buyuk sayiyi bulmaya hosgeldiniz

*******************************************************************

""")

a = int(input("birinci sayiyi giriniz"))
b = int(input("ikinci sayiyi giriniz"))
c = int(input("ucuncu sayiyi giriniz"))

if ( a>b and a>c):
    print("en buyuk sayi {}".format(a))
elif ( b>a and b>c):
    print("en buyuk sayi {}".format(b))
elif ( c>a and c>b):
    print("en buyuk sayi {}".format(c))
else:
    print("lutfen dogru deger giriniz")
    
    
