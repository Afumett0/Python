ehliyet = True
araba = False

if ehliyet and araba:
    print("Araba kullanabilirsin.")

elif araba and not ehliyet:
    print("Bizim surucu kursumuzu tercih edebilirsiniz.")

elif ehliyet or araba:
    print("Araba kullanmana cok az kaldi.")

else:
    print("Araba kullanman icin cok zaman var.")