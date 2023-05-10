
satis1=[0,0]
i=3
while i>0:
    a=str(input("Ürün adını giriniz:"))
    b=int(input("Ürün fiyatını giriniz:"))
    c=int(input("Ürün adedini giriniz:"))
    liste1=[a,int(b),int(c)]


    satis1[0]+=b
    satis1[1]+=c
    i-=1
    if i==0:
        break

    else:
        continue
print("Toplam kazanç {}".format(satis1[0]))
print("Satılan ürün adedi{}".format(satis1[1]))

""" Not: Başka ürün var mı kısmını yazarken  döngüyü if-else komutlarıyla kırmaya çalıştım ancak başarılı 
olamadım. Sonsuz döngüye girdim, o yüzden ürün girişini 3 ile sınırlı tuttum"""




