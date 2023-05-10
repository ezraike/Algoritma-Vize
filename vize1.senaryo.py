while True:
    print("Yapmak istediğiniz işlemi girin(sayı kodu):\n"
          " 1-Stok Girişi Yap (Stok). 2- Kasada Ürün Sat (Kasa) 3-Gün Sonu Al (GünSonu)."
          " 4- Çıkış yap (Evet/Hayır)\n")
    a=int(input("Karar:"))
    if a==1:
        b=str(input("Ürünün adını giriniz:"))
        c=int(input("Ürün kodunu giriniz:"))
        d= str(input("Tedarikçi Adını giriniz"))
        e=str(input("Stok adedini giriniz:"))
        f=str(input("Reyon kategorisi giriniz:"))
        continue
    elif a==2:
        b = str(input("Ürünün adını giriniz:"))
        c = int(input("Ürün kodunu giriniz:"))
        print("Ürün başarıyla satıldı.!")
        continue
    elif a==3:
        print("Gün sonu başarıyla alındı.")
        continue
    elif a==4:
        g=str(input("Çıkış yapmak istediğinize emin misiniz?"))
        if g=="evet" or "Evet":
            break
        elif g=="hayır" or "Hayır":
            continue
        else:
            pass