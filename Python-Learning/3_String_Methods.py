name = "Bro"
print(len(name)) # how long characters len meth
print(name.find("r"))# kaçıncı indekste olduğunu gösteriyor
print(name.capitalize())
print(name.upper()) # Bütün harfleri büytür
print(name.lower())  # Bütün harfleri küçük yazar
print(name.isdigit()) # Eğer name in içinde sayısal bi değer varsa TRUE eğer sadece string veri varsa False
print(name.isalpha()) # İsdigit in tam tersi calısıyo
print(name.count("o")) # kaç tane o olduğunu sayıyor
print(name.replace("o","a")) # old eski hali new yeni değiştirilen hali yani o yu a ya çeviriyor
print(name*3) #3 defa aynı veriyi yazdırıyor