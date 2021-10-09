
print("""
*****************************************************************

Beden Kitle Endeksine Hosgeldin

*****************************************************************
""" )

boy = float(input(" Lutfen Boyunuzu giriniz.(m)"))
kilo = float(input(" Lutfen Kilonuzu giriniz.(kg)"))

bke = (kilo / (boy ** 2))
print(" Beden Kitle Endeksiniz {} 'dır ".format(bke))

if ( bke <= 18.5):
    print(" Zayıfsiniz ")
elif (18.25 <= bke <= 25):
    print(" Normalsiniz")
elif ( 25 <= bke <= 30 ):
    print(" Fazla Kilolusunuz")
elif ( 30<= bke):
    print(" Obezitesiniz")
else:
    print(" Lutfen dogru deger girin !")
