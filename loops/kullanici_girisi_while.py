
print(" While ile kullanici girisine hosgeldiniz")

username = "raks"
password = "123456"

print(" 5 giris hakkiniz vardir")

giris_hakki = 5

while True:
    input_username = input(" Lutfen kullanici adini girin")
    input_password = input(" Lutfen sifreyi girin")

    if ( username != input_username and password == input_password):
        print(" Kullanici adi hatala fakat parola dogru")
        giris_hakki -=1
        

    elif ( username == input_username and password != input_password):
        print( " Kullanici adi dogru fakat parola yanlis")
        giris_hakki -=1
        
    elif ( username != input_username and password != input_password):
        print(" Kullanici adi ve parola yanlis")
        giris_hakki -=1

    else:
        print(" Tebrikler bilgiler dogru basariyla giris yaptınız")
        break
        
    print("{} giris hakkiniz kalmistir".format(giris_hakki))

    if ( giris_hakki == 0):
        print(" Maalesef giris hakkınız dolmustur")
        break


