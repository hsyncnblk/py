
CanHesap={
    "ad":"can",
    "hesapNo":"123456789",
    "bakiye":5000,
    "krediLimit":2500

}

AliHesap={
    "ad":"ali",
    "hesapNo":"987654321",
    "bakiye":3000,
    "krediLimit":1000

}

def ParaCek(isim,miktar):
    print(f"merhaba {isim['ad']}")

    if (isim['bakiye']>=miktar):
        isim['bakiye'] -=miktar
        print("paranızı alabilirsiniz")
        bakiyeSorgu(CanHesap)

    else:
        toplam=isim['bakiye']+isim['krediLimit'] 

        if (toplam>=miktar):
            kredi=input("kredi çekilsin mi e/h:")
            if kredi=="e":
                cekilenkredi=miktar-isim["bakiye"]
                isim["bakiye"]=0
                isim["krediLimit"] -=cekilenkredi

                print("para çekildi")
                bakiyeSorgu(CanHesap)

            else:
                print("işlem iptal edidi")   
                bakiyeSorgu(CanHesap) 


        else:
            print("limit aşıldı para çekilemedi")
            bakiyeSorgu(CanHesap)


def bakiyeSorgu(isim):
    print(f'{isim["hesapNo"]} nolu hesabınızda {isim["bakiye"]} TL bulunmaktadır  kredi limitiniz {isim["krediLimit"]} TL dir')



ParaCek(CanHesap,3000)
#bakiyeSorgu(CanHesap)

