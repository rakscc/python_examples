class Hayvanlar():

    def __init__(self,omur, dollenme_sekli, kalp_odacik_sayisi, vucut_isisi, bosaltim_turu):

        self.omur = omur
        self.dollenme_sekli = dollenme_sekli
        self.kalp_odacik_sayisi = kalp_odacik_sayisi
        self.vucut_isisi = vucut_isisi
        self.bosaltim_turu = bosaltim_turu


    def bilgileri_goster(self):

        print(" Hayvanin Omru : {}\n Dollenme sekli: {}\nKalp odacik sayisi: {}\nVucut isisi: {}\nBosaltim turu : {} ".format(self.omur,self.dollenme_sekli,self.kalp_odacik_sayisi,self.vucut_isisi,self.bosaltim_turu))


class Kopek(Hayvanlar):

    def __init__(self,omur, dollenme_sekli, kalp_odacik_sayisi, vucut_isisi, bosaltim_turu,cinsi,uyrugu,dis_sayisi):

        super().__init__(omur,dollenme_sekli,kalp_odacik_sayisi,vucut_isisi,bosaltim_turu)

        self.cinsi = cinsi
        self.uyrugu = uyrugu
        self.dis_sayisi = dis_sayisi


    def saldırganmi(self):

        if (self.kalp_odacik_sayisi == 5 and self.cinsi == "pitbull" and self.dis_sayisi == 32):

            print("Bu kopek saldirgandir")

        else:

            print("Bu kopek saldirgan degildir")

    def bilgileri_goster(self):

        print("Kopegin Omru : {}\nKopegin Dollenme sekli: {}\n Kopegin kalp odacik sayisi : {}\nKopegin bosaltim turu : {}\nKopegin uyurugu : {}\nKopegin dis sayisi {}: ".format(self.omur,self.dollenme_sekli,self.kalp_odacik_sayisi,self.vucut_isisi,self.bosaltim_turu,self.uyrugu,self.dis_sayisi))


kopek1 = Kopek(5,"dis",5,35,"urik","amazon pitbullu","pitbull",32)

kopek1.bilgileri_goster()
kopek1.saldırganmi()


