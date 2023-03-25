import math
import time
import sympy
import sympy
from sympy import *
from sympy.abc import _clash1, _clash2, _clash
from sympy.algebras.quaternion import Quaternion
from sympy import symbols, I
x,y,z,t, = symbols('x y z t')
from sympy.plotting import plot3d

print("""
-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz 
İşlemler;
1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
5. Üs Alma 
6. Logaritma 
7. Daire Alanı Hesasplama
8. Daire Çevresi Hesaplama
9. Faktoriyel Hesaplama 
10. Kök Hesapalama
11. Girilen fonksyonun Türevini alma 
12. Türev hesaplama 
13. Limit hesaplama
14. Belirsiz integral Hesaplama 
15. Belirli integral Hesaplama 
16. Denklemleri Çarpanlara Ayırma 
17. Denklemin Köklerini Bulma 
18. 2D Grafik Çizme
19. 3D Grafik Çizme 

    ÇIKIŞ için "q" 
-------------------------------------------------
""")

while True :
    işlem = input("Yapmak istedğiniz işlemi seçiniz (1-19 yada q) : ")

    if(işlem == "q"):
        print("İşleminiz Gerçekleştiriliyor")
        time.sleep(2)
        print("Çıkış Yaptınız...")
        break

    elif (işlem == "1"):
        sayı1 = int(input(" 1.sayıyı giriniz : "))
        sayi2 = int(input(" 2.sayıyı giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} + {} = {}".format(sayı1, sayi2, sayı1 + sayi2))

    elif (işlem == "2"):
        sayı1 = int(input(" 1.sayıyı giriniz : "))
        sayi2 = int(input(" 2.sayıyı giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} - {} = {}".format(sayı1, sayi2, sayı1 - sayi2))

    elif (işlem == "3"):
        sayı1 = int(input(" 1.sayıyı giriniz : "))
        sayi2 = int(input(" 2.sayıyı giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} * {} = {}".format(sayı1, sayi2, sayı1 * sayi2))

    elif (işlem == "4"):
        sayı1 = int(input(" 1.sayıyı giriniz : "))
        sayi2 = int(input(" 2.sayıyı giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} / {} = {}".format(sayı1, sayi2, sayı1 / sayi2))

    elif (işlem == "5"):
        sayı1 = int(input(" taban değerini  giriniz : "))
        sayi2 = int(input(" üs değerini  giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} sayısının {} dereceden üssü = {} ".format(sayı1, sayi2, math.pow(sayı1, sayi2)))

    elif (işlem == "6"):
        logüs = int(input(" Logaritmanın üs değerini giriniz  : "))
        logtaban = int(input(" Logaritmanın taban değerini giriniz  : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} sayısının {} tabanında logaritması  = {} ".format(logüs, logtaban, math.log(logüs, logtaban)))

    elif (işlem == "7"):

        Yarıcap = int(input(" Alanını bulmak isteğiniz dairenin yarıçapını giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Yarıçapı {} olan dairenin alanı = {} ".format(Yarıcap,math.pi*(Yarıcap)**2))

    elif (işlem == "8"):
        Yarıcap = int(input(" Çevresini  bulmak isteğiniz çemberin yarıçapını giriniz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Yarıçapı {} olan çemberin çevresi = {} ".format(Yarıcap,math.pi*2*Yarıcap))

    elif (işlem == "9"):
        sayı1 = int(input("Hangi sayının faktöriyelini bulmak istiyorsunuz : "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} sayısının faktoriyeli = {}".format(math.factorial(sayı1)))

    elif (işlem == "10"):
        sayı1 = int(input("Hangi sayının karekökünü bulmak istiyorsunuz "))
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("{} sayısının karekökü = {} ".format(sayı1,math.sqrt(sayı1)))

    elif(işlem == "11"):
        print("NOT : Çok değişkenli fonksyonlarda x,y,z ve t değişkenleri dışında değişken kulanmamaya özen gösteriniz ")
        time.sleep(0.3)
        denklem = input("lütfen türevini almak isteddiğiniz denklemi giriniz : ")
        degisken = input("hangi değişkene göre türev alınacaktır ? : ")
        print("işleminiz gerçekleşiyor... ")
        time.sleep(1)
        print("[ {} ] denkleminin {} değiskenine göre türevi = [ {} ]'dir".format(denklem,degisken, diff(denklem,degisken)))

    elif(işlem == "12"):
        print("NOT : Çok değişkenli fonksyonlarda tek değişkene göre türev hesabı yapılmaktadır ")
        print("NOT : Çok değişkenli fonksyonlarda x,y,z ve t değişkenleri dışında değişken kulanmamaya özen gösteriniz ")
        time.sleep(0.3)
        denklem =input("lütfen türevini almak isteddiğiniz denklemi giriniz : ")
        degisken = input("hangi değişkene göre türev alınacaktır ? : ")
        deger = input("hangi sayıya göre türev alınacak :  ")
        if(deger == "e" ):
            deger = exp
        elif (deger == "-e"):
            deger = -exp
        elif(deger == "pi"):
            deger = pi
        else:
            deger = int(deger)
        print("işleminiz gerçekleşiyor... ")
        time.sleep(1)
        print("[ {} ] denkleminin türevi = [ {} ]'dir".format(denklem, diff(denklem,degisken)))
        denklem = diff(denklem,degisken)
        print("denklemin {} değişkenine göre {} değerinde türev değeri {} 'dir  ".format(degisken, deger,denklem.subs(degisken,deger)))

    elif(işlem == "13"):
        denklem = input('Lütfen limitini bulmak istediğiniz fonksiyonu giriniz : ')
        deger =(input('Lütfen limitini bulmak istediğiniz değeri girin: '))
        if (deger == "e"):
            deger = exp
        elif (deger == "-e"):
            deger = -exp
        elif (deger == "pi"):
            deger = pi
        else:
            deger = float(deger)
        degisken = input("hangi değişkene göre limit alınacaktır ? : ")
        lim = Limit(denklem, degisken, deger).doit()
        print("işleminiz gerçekleşiyor... ")
        time.sleep(1)
        print(f'Limit: {lim}')

    elif(işlem == "14"):
        while True :
            print("Lütfen tek değişken içeren fonksiyonlar giriniz ")
            time.sleep(0.3)
            denklem = input("Lütfen integralini bulmak istediğiniz fonksiyonu girin: ")
            degisken = input("Hangi değişekene göre integral alacaksınız  ")
            print("işleminiz gerçekleşiyor... ")
            time.sleep(1)
            try:
                İntegral = integrate(denklem,degisken)
                print(f'İntegral: {İntegral}')
                break
            except ValueError:
                print("Hata !!! Lütfen tek bir değişken içeren denkleme yazınızız örneğin : sadece x ya da y değişkeni içeren ")

    elif(işlem == "15"):
        while True :
            print("Lütfen tek değişken içeren fonksiyonlar giriniz ")
            time.sleep(0.3)
            denklem = input("Lütfen integralini bulmak istediğiniz fonksiyonu giriniz: ")
            degisken = input("Hangi Değisekene Göre integral alıcaksınız ? :")
            alt_sinir =input("Alt Sınırınız Ne ? :")

            if (alt_sinir == "e"):
                alt_sinir = exp
            elif (alt_sinir == "-e"):
                alt_sinir = -exp
            elif (alt_sinir== "pi"):
                alt_sinir = pi
            else:
                alt_sinir = float(alt_sinir)

            ust_sinir = (input("Üst Sınırınız Ne ? :"))
            if (ust_sinir == "e"):
                ust_sinir = exp
            elif (ust_sinir == "-e"):
                ust_sinir = -exp
            elif (ust_sinir== "pi"):
                ust_sinir = pi
            else:
                ust_sinir = float(ust_sinir)

            print("işleminiz gerçekleşiyor... ")
            time.sleep(1)
            try:
                İntegral = integrate(denklem,degisken)
                print(f'İntegral: {İntegral}')
                sonuc = integrate(denklem, (degisken, alt_sinir, ust_sinir))
                print("integralinizin Cevabı : {} ".format(sonuc))
                break

            except ValueError:
                print("Hata !!! Lütfen tek bir değişken içeren denkleme yazınızız örneğin : sadece x ya da y değişkeni içeren ")

    elif(işlem == "16"):
        denklem = input("Lütfen Hangi fonksyonu çarpanlara ayırmak istediğinizi giriniz : ")
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Girdiğiniz denklemin çarpanlara ayrılmış hali = {} ".format(factor(denklem)))

    elif(işlem == "17"):
        print("Tek değişken içeren denklem girerseniz daha kesin cevap alabilirsiniz ")
        time.sleep(0.3)
        denklem = input("Lütfen Köklerini Bulmak İstediğiniz Denklemi Giriniz :  ")
        print("işleminiz yapılıyor...")
        time.sleep(1)
        print("Girdiğiniz {} Denkleminin Kökleri = {} ".format(denklem , solve(denklem)))

    elif(işlem == "18"):
        while True :

            denklem = input("Grafiği çizilecek fonksyonu giriniz : ")
            renk = input("lütfen grafiğinizin rengini giriniz (red,blue,green,yellow,vb. ) :  ")

            print("işleminiz yapılıyor...")
            time.sleep(1)
            try:
                plot(denklem,line_color = str(renk))
                break
            except ValueError:
                print("Hata !!! Lütfen tek bir değişken içeren denkleme yazınızız örneğin : sadece x ya da y değişkeni içeren ")

    elif(işlem == "19"):
        denklem = input("3D Grafiği çizilecek fonksyonu giriniz : ")
        print("işleminiz yapılıyor...")
        time.sleep(1)
        plot3d(denklem)

















