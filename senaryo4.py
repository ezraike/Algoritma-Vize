while True:
    sozluk1={"Selpak":(30,20),"Kalem":(15,20),"Defter":(20,30),"Kitap":(23,45)}

    print("Başarıyla gün sonu ekranına giriş yaptınız!")
    a=input("Aratmak istediğiniz ürünün ismini yazınız:")

    if a in sozluk1:
        print("{} ürününün kalan adedi {} Toplam kazanç {}'dir".format(a,sozluk1[a][0],sozluk1[a][1]))
    else:
        print("Belirttiğiniz ürün sözlük içerisinde bulunmuyor")
