yas = int(input("Lutfen yasinizi girin: "))

okul = input("Okuyor musunuz ?: ")

if yas >= 18 and not okul:
    print("Askere Gelme Yasiniz Geldi!")

elif yas > 18 and okul:
    print("Okulunuz Bittiginde Askere Geleceksiniz!")

else:
    print("Askerlik Yasiniz Daha Gelmedi!")
