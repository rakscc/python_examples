import time
import random
from threading import Timer


class Kumanda():

    def __init__(self, tv_durum="Kapali", tv_ses_seviyesi=0,
                 tv_mute_durum="Mute Kapali", tv_kanallar=["Trt", "fox", "kanald", "show", "atv"],
                 tv_suanki_kanal="trt"):

        self.tv_durum = tv_durum
        self.tv_ses_seviyesi = tv_ses_seviyesi
        self.tv_mute_durum = tv_mute_durum
        self.tv_kanallar = tv_kanallar
        self.tv_suanki_kanal = tv_suanki_kanal

    def tv_acik_kapali_ayar(self):

        while True:

            if (self.tv_durum == "Kapali"):

                user_tv_kapali_ayar_input = input("Televizyon şuan kapali. Açmak için 'ac' yaziniz : \n"
                                                  "Anamenuye donmek icin 'anamenu' yaziniz:  ")

                if (user_tv_kapali_ayar_input == "ac"):
                    print("Televizyon aciliyor. Lutfen bekleyin ....")
                    time.sleep(2)
                    self.tv_durum = "Acik"
                    print("Televizyon acildi.")

                elif (user_tv_kapali_ayar_input == "anamenu"):
                    print("Cikis yapiliyor lütfen bekleyin....")
                    time.sleep(2)
                    print("Cikis yapildi. ")
                    break

                else:
                    print("Gecersiz deger girdiniz...")

            elif (self.tv_durum == "Acik"):

                user_tv_acik_ayar_input = input("Televizyon şuan açık. Kapatmak için 'kapat' yaziniz : \n"
                                                "Anamenuye donmek icin 'anamenu' yaziniz:  ")

                if (user_tv_acik_ayar_input == "kapat"):
                    print("Televizyon kapatiliyor. Lutfen bekleyin ....")
                    time.sleep(2)
                    self.tv_durum = "Kapali"
                    print("Televizyon kapatildi.")

                elif (user_tv_acik_ayar_input == "anamenu"):
                    print("Cikis yapiliyor lütfen bekleyin....")
                    time.sleep(2)
                    print("Cikis yapildi. ")
                    break

            else:
                print("gecersi deger girdiniz")

    def ses_ayar(self):

        while True:

            user_ses_input = input("Sesi artırmak için '+' yaziniz :\n"
                                   "Sesi azaltmaz için '-' yaziniz :\n"
                                   "Anamenuye donmek icin 'anamenu' yaziniz: : ")

            if (user_ses_input == "+"):

                if (self.tv_ses_seviyesi >= 0):
                    self.tv_ses_seviyesi += 1
                    print("Ses seviyesi artirildi.Guncel ses seviyesi : ", self.tv_ses_seviyesi)

                elif (self.tv_ses_seviyesi == 32):
                    print("Ses seviyesi maximumdur. Daha fazla artirilamaz")

            elif (user_ses_input == "-"):

                if (self.tv_ses_seviyesi < 32):
                    self.tv_ses_seviyesi -= 1
                    print("Ses seviyesi azaltildi.Guncel ses seviyesi : ", self.tv_ses_seviyesi)

                elif (self.tv_ses_seviyesi == 0):
                    print("Ses seviyesi en dusuktur. Dusurulemez")

            elif (user_ses_input == "anamenu"):
                print("Anamenuye donuluyor....")
                time.sleep(2)
                print("Anamenuye donuldu. Guncel ses seviyesi : ", self.tv_ses_seviyesi)
                break

            else:
                print("Gecersiz deger girdiniz!")

    def ses_mute_ayar(self):

        if (self.tv_mute_durum == "Mute Kapali"):
            user_ses_mute_kapali_input = input("Mute kapali.Acmak icin 'ac' yaziniz : ")

            if (user_ses_mute_kapali_input == "ac"):
                print("Mute aciliyor. Lutfen Bekleyin...")
                self.tv_mute_durum = "Mute Acik"
                self.tv_ses_seviyesi = 0
                time.sleep(2)
                print("Mute acildi")

            else:
                print("Gecersiz deger girdiniz")

        elif (self.tv_mute_durum == "Mute Acik"):
            user_ses_mute_acik_input = input("Mute acik. Kapatmaik icin 'kapat' yaziniz : ")

            if (user_ses_mute_acik_input == "kapat"):
                print("Mute kapatiliyor. Lutfen Bekleyin...")
                time.sleep(2)
                self.tv_mute_durum = "Mute Kapali"
            else:
                print("Gecersiz deger girdiniz")

    def ses_goster(self):

        print("Ses seviyesi : ", self.tv_ses_seviyesi)

    def kanallari_goster(self):

        index = 1

        for value in self.tv_kanallar:
            print(index, value)
            index += 1

    def kanal_ekle(self):

        eklenecek_kanal = input("Eklenecek kanal adini giriniz : ")
        print(eklenecek_kanal + " Kanali ekleniyor")
        self.tv_kanallar.append(eklenecek_kanal)
        print(eklenecek_kanal + " Kanali basariyla eklendi.")

    def kanal_cikarma(self):

        cikarilacak_kanal_number = str(input("Cikarilacak kanal numarasini giriniz."
                                             " (Kisayol: Kanal listesine ulasmak icin 'q' girin ) : "))
        if (cikarilacak_kanal_number == "q"):
            self.kanallari_goster()
            cikarilacak_kanal_number2 = int(input("Cikarilacak kanal numarasini giriniz: "))
            print("{} numarali {} kanali kanal listesinden cikariliyor...".format(str(cikarilacak_kanal_number2),
                                                                                  self.tv_kanallar[
                                                                                      cikarilacak_kanal_number2 - 1]))
            del self.tv_kanallar[int(cikarilacak_kanal_number2) - 1]
            time.sleep(2)
            print(self.tv_kanallar[cikarilacak_kanal_number2 - 1] + " kanali basariyla cikarildi")

        elif (cikarilacak_kanal_number.isnumeric() == True):

            if (int(cikarilacak_kanal_number) < int(len(self.tv_kanallar))):
                print("{} numarali {} kanali kanal listesinden cikariliyor...".format(str(cikarilacak_kanal_number),
                                                                                      self.tv_kanallar[
                                                                                          int(cikarilacak_kanal_number) - 1]))
                del self.tv_kanallar[int(cikarilacak_kanal_number) - 1]
                time.sleep(2)
                print(self.tv_kanallar[int(cikarilacak_kanal_number) - 1] + " kanali basariyla cikarildi")

            else:
                print("O kadar kanal yok. Lütfen dogru rakam gir")
        else:
            print("Doğru deger gir")

    def ust_kanala_gecme(self):

        suan_kanal = self.tv_suanki_kanal
        suan_kanal_number = self.tv_suanki_kanal.index(suan_kanal)
        self.tv_suanki_kanal = self.tv_kanallar[suan_kanal_number + 2]
        print("Ust kanala geciliyor...")
        time.sleep(2)
        print("Ust kanala gecildi. Guncel kanal : ", self.tv_suanki_kanal)

    def alt_kanala_gecme(self):

        suan_kanal = self.tv_suanki_kanal
        suan_kanal_number = self.tv_suanki_kanal.index(suan_kanal)
        self.tv_suanki_kanal = self.tv_kanallar[suan_kanal_number - 1]
        print("Alt kanala geciliyor...")
        time.sleep(2)
        print("Alt kanala gecildi. Guncel kanal : ", self.tv_suanki_kanal)

    def numaradan_kanala_gec(self):

        user_gidecegi_numara = input("Gidecegin kanalin numarasini gir : ")
        print(user_gidecegi_numara + " numarali kanala gidiliyor...")
        time.sleep(2)
        self.tv_suanki_kanal = self.tv_kanallar[int(user_gidecegi_numara) - 1]
        print(user_gidecegi_numara + " numarali kanala gidili")
        print("güncel kanal : ", self.tv_suanki_kanal)

    def random_kanala_gec(self):

        print("rastele sayiya gidiliyor...")
        time.sleep(2)
        rastgele = random.randint(0, len(self.tv_kanallar) - 1)
        self.tv_suanki_kanal = self.tv_kanallar[rastgele]
        print("rastgele sayiya gidildi güncel kanal: ", self.tv_suanki_kanal)

    def kanal_tasima(self):

        tasinacak_kanal = int(input("tasinacak kanalin numarasini gir: "))
        tasinacak_numara = int(input("tasinacak yerin numarasini gir : "))
        print(str(tasinacak_kanal) + " numarali kanal " + str(tasinacak_numara) + " numarasina tasiniyor...")
        time.sleep(2)
        self.tv_kanallar.insert(tasinacak_numara - 1, self.tv_kanallar.pop(tasinacak_kanal - 1))
        print("Tasima islemi tamamlandi.\n"
              "güncel kanal listesi : ")
        self.kanallari_goster()

    def sleep_modu(self):

        print("Televizyon kapaniyorr....")
        time.sleep(2)
        self.tv_durum = ("Kapali")
        print("Televizyon kapandi")

    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum,
                                                                                          self.tv_ses_seviyesi,
                                                                                          self.tv_kanallar,
                                                                                          self.tv_suanki_kanal)


kumanda1 = Kumanda()

print("""

				Televizyon Kumandasi


1. Power tusu					7. Kanal cikar

2. Ses ayar tusu				8. kanal + ( ust kanala gecme )

3. Mute							9. kanal - (alt kanala gecme)

4. Ses seviyesi					10. kanala git		

5. Kanallari goster 			11. Kanal tasi

6. Kanal ekle					12. Rastgele kanala git

                                13. uyku modu


				Çıkmak için 'q' ya basın.

""")

while True:

    islem = input("Lutfen islemi seciniz : ")

    if (islem == "q"):
        print("Program sonlandiriliyor...")
        break

    elif (islem == "1"):
        kumanda1.tv_acik_kapali_ayar()

    elif (islem == "2"):
        kumanda1.ses_ayar()

    elif (islem == "3"):
        kumanda1.ses_mute_ayar()

    elif (islem == "4"):
        kumanda1.ses_goster()

    elif (islem == "5"):
        kumanda1.kanallari_goster()

    elif (islem == "6"):
        kumanda1.kanal_ekle()

    elif (islem == "7"):
        kumanda1.kanal_cikarma()

    elif (islem == "8"):
        kumanda1.ust_kanala_gecme()

    elif (islem == "9"):
        kumanda1.alt_kanala_gecme()

    elif (islem == "10"):
        kumanda1.numaradan_kanala_gec()

    elif (islem == "11"):
        kumanda1.kanal_tasima()

    elif (islem == "12"):
        kumanda1.random_kanala_gec()

    elif (islem == "13"):

        sleep_modu_saniye = int(input("Kac saniye sonra televizyon kapansin"))

        t = Timer(sleep_modu_saniye, kumanda1.sleep_modu)
        t.start()

    elif (islem == "99"):
        print(kumanda1)

    else:
        print("gecersiz deger giridiniz")