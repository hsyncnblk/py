"""
1 ile 100 arasında bilgisayarın random olarak tuttuğu sayıyı bulmaya çalış 

unutma sadece 5 hakkın var

"""

import random

sayı=random.randint(1,100)
hak=5
sayac=0

while hak>0:
    hak -=1
    sayac +=1
    tahmin=int(input("tahminin nedir:"))

    if sayı ==tahmin:
        print(f"tebrikler {sayac}. defada bildin")
        break

    elif sayı<tahmin:
        print("aşağı")

    else:
        print("yukarı")

    if hak ==0:
        print("hakkın bitti")    
