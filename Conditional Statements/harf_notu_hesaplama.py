
print(" Harf notu hesaplamaya hosgeldiniz")

vize1 = int(input(" vize 1 notunuzu giriniz "))
vize2 = int(input(" vize 2 notunuzu giriniz "))
final = int(input(" final notunuzu giriniz "))

hesap_vize1 = vize1*0.3
hesap_vize2 = vize2*0.3
hesap_final = final*0.4

toplam_not = hesap_vize1 + hesap_vize2 + hesap_final

if ( toplam_not >= 90):
    print("Notunuzu {} 'dır. Harf notunuz ise AA 'dır".format(toplam_not))
elif ( toplam_not >= 85):
    print("Notunuz {} 'dır . Hatf notunuz ise BA 'dır".format(toplam_not))
elif ( toplam_not >= 80):
    print("Notunuz {} 'dır . Hatf notunuz ise BB 'dır".format(toplam_not))
elif (toplam_not >= 75):
    print("Notunuz {} 'dır . Hatf notunuz ise CB 'dır".format(toplam_not))
elif ( toplam_not >= 70):
    print("Notunuz {} 'dır . Hatf notunuz ise CC 'dır".format(toplam_not))
elif (toplam_not >= 65):
    print("Notunuz {} 'dır . Hatf notunuz ise DC 'dır".format(toplam_not))
elif (toplam_not >= 60):
    print("Notunuz {} 'dır . Hatf notunuz ise DD 'dır".format(toplam_not))
elif (toplam_not >= 55):
    print("Notunuz {} 'dır . Hatf notunuz ise FD 'dır".format(toplam_not))
elif ( toplam_not <= 55):
    print("Notunuz {} 'dır . Hatf notunuz ise FF 'dır".format(toplam_not))
else:
    print(" Lutfen dogru deger giriniz! ")
    