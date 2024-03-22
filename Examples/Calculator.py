first = int(input("Islem yapmak istediginiz ilk sayiyi giriniz: "))
second = int(input("Islem yapmak istediginiz ikinci sayiyi giriniz: "))

islem = input("Yapmak istediginiz islemi giriniz(T= Toplama C=Cikarma Ca=Carpma B=Bolme): ")

if islem == "T":
    print("Sonuc: "+ str(first+second))
elif islem == "C":
    print("Sonuc: "+ str(first-second))
elif islem == "Ca":
    print("Sonuc: "+ str(first*second))
elif islem == "B":
    print("Sonuc: "+ str(first/second))
else:
    print("Yanlis bir islem girdiniz!")