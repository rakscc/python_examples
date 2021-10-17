with open("C:\\Users\\halil\\Desktop\\dosya_okuma\\futbolcular.txt","r",encoding="utf-8") as file:

    gs_liste = list()
    rize_liste = list()
    madrid_liste = list()

    for satir in file:
        satir = satir[:-1]
        satir_elemanlari = satir.split(",")

        if (satir_elemanlari[1] == "Galatasaray"):
            gs_liste.append(satir + "\n")

        elif (satir_elemanlari[1] == "Rizespor"):
            rize_liste.append(satir + "\n")

        else:
            madrid_liste.append(satir + "\n")

    with open("C:\\Users\\halil\\Desktop\\dosya_okuma\\galatasaray.txt","w",encoding="utf-8") as file1:
        for i in gs_liste:
            file1.write(i)

    with open("C:\\Users\\halil\\Desktop\\dosya_okuma\\rizespor.txt", "w", encoding="utf-8") as file2:
        for i in rize_liste:
            file2.write(i)

    with open("C:\\Users\\halil\\Desktop\\dosya_okuma\\realmadrid.txt", "w", encoding="utf-8") as file3:
        for i in madrid_liste:
            file3.write(i)
