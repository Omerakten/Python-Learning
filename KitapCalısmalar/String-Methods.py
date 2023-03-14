#String Methods

#Capitalize
mystr = "  ömer akten 21 kırklareli lüleburgaz grafiker."
print(mystr.capitalize())
#Capitalize : string ifadenin baş harfini büyük yazdırmaya yarar
#capitalize metodunda sadece ilk harfi büyük yapıyor.

#Split
cnvrt= mystr.split()
print(cnvrt[0])
print(type(cnvrt))
#birden fazla kelimeli stringleri ayıran bu fonksiyon öncelikle mystr = "ömer akten" gibi
#iki veya daha fazla kelimelik bir string yazalım daha sonra mystr.split() kodunu yazalım ve bir cnvrt değişkenine atayalım
#print(cnvrt[0]) yazdığımızda çıktı ömer olarak yazırılacaktır
#KISACASI SPLİT STRİNG DEĞER İÇİNDEKİ BİRDEN FAZLA OLAN KELİMELERİ LİSTEYE ÇEVİRİR
#print(type(cnvrt)) olarak veri tipini kontrol ettiğimizdede class list olarak görüryoruz.

#Upper
print(mystr.upper())
#Upper metodu string ifade içerisindeki tüm karakterleri büyük harf yapmaya yarar

#Lower
print(mystr.lower())
#Lower metodu upper metodunun tam tersi olarkak calısır ve tüm karakterleri küçük harf olarka yazdırır

#Center
print(mystr.center(70))
#Center metodu, string ifadeyi yazdırırken 20 boşluk bıraktırıp yazdırmaya yarar
#her iki taraftan da 20 boşlk bıraktırmasını istedik
#output:      ömer akten
print(mystr.center(70,"-"))
#bu şekilde boşluk sayısı yazıp daha sonra virgünden sonra "" içindeki herhangi bir string
#veriyi, mystr verisinin önünü "" içinde doldurduğumuz string veriyle doldurur
#örnekte olduğu gibi
#output :  -----ömer akten-----

#Count
print(mystr.count("ömer"))
#Count metodu() içinde belirlediğimiz veriyi mystr string verisi içerisinde
#kaç adet olduğunu arar ve yazdırır .
#Out : 1

#startswith()
print(mystr.startswith("ö"))
#Dize belirtilen değerle başlıyorsa yöntem True, aksi takdirde False döndürür .

#endswith
print(mystr.endswith("."))
print(mystr.endswith("r"))
#endswith metodu parantez içinde yer alan veriyi baz alarak
#mystr verisinini kontrol eder ve eğer veri sonunda (".") nokta var ise
#true döndürür yok ise false döner

#Find
print(mystr.find("a"))#belirtilen şeyi arar ve hangi indekste olduğunu söyler
print(mystr.find("e")) #aynı şekil bu da öyle
print(mystr.find("e",10,25)) #out 21 . indekste e var 10 . indeksten sonra 25. indekse kadar aradı
print(mystr.find("x")) #bulamadı -1
#Yöntem, find()belirtilen değerin ilk geçtiği yeri bulur.
#find()Değer bulunamazsa yöntem -1 değerini döndürür .
#index() metodu ile tamamen aynı tek fark bulamazsa hata verir -1 dönmez

#isalnum()
isal = "asdasd0sad1"
print(isal.isalnum()) #string ve int değerler "" içindeyse true
# boşluk!#%&? gibi ibareler var ise false döndürür tamamen string ifadeyse true

#isaplha()
print(isal.isalpha()) #sadece string ifadeleri kabul eder ve o zaman true döner
#eğer veri içinde str harici bişey varsa false olur

#isascii()
print(isal.isascii())
#Tüm karakterler ascii karakterler (a-z) ise, yöntem True değerini döndürür .

#isdigit()
print(isal.isdigit())
#tüm karakterlerin rakam olup olmadığını kontrol eder

#isidentifier()
print(isal.isidentifier())
# dize geçerli bir tanımlayıcıysa True, aksi takdirde False döndürür.
#Bir dize, yalnızca alfasayısal harfler (az) ve (0-9) veya alt çizgi (_) içeriyorsa geçerli bir
# tanımlayıcı olarak kabul edilir. Geçerli bir tanımlayıcı bir sayı ile başlayamaz veya boşluk içeremez.

#islower()
print(isal.islower())
#tüm karakterler küçük harf ise True, aksi halde False döndürür.
#Rakamlar, semboller ve boşluklar kontrol edilmez, sadece alfabe
# karakterleri kontrol edilir.

#isnumeric() *******
print(isal.isnumeric())
#tüm karakterler sayısalsa (0-9) True, aksi takdirde False döndürür.

#isspace()
print(isal.isspace())
#bir dizedeki tüm karakterler boşluksa True, aksi takdirde False döndürür.

#istitle()
print(isal.istitle())
#bir metindeki tüm kelimeler büyük harfle başlıyorsa VE kelimenin geri
# kalanı küçük harflerden oluşuyorsa True, aksi halde False döndürür.

#isupper()
print(isal.isupper())
#tüm karakterler büyük harf ise True, aksi halde False döndürür.
#Rakamlar, semboller ve boşluklar kontrol edilmez, sadece alfabe
# karakterleri kontrol edilir.

#maketrans()
b = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(b.translate(mytable))
#translate()Bir eşleme tablosu oluşturun ve "S" karakterlerini "P" karakteriyle değiştirmek için yöntemde kullanın

#partition()
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
#belirtilen bir dizeyi arar ve dizeyi üç öğe içeren bir demet halinde böler.
#İlk eleman, belirtilen dizgeden önceki kısmı içerir.
#İkinci öğe, belirtilen dizeyi içerir.
#Üçüncü eleman, dizeden sonraki kısmı içerir.

#replace()
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
#belirtilen bir tümceciği belirtilen başka bir tümcecik ile değiştirir.

#rfind()
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
#sağdan sola calısır r yani right
#Yöntem, rfind()belirtilen değerin son geçtiği yeri bulur.
#rfind()Değer bulunamazsa yöntem -1 değerini döndürür .

#strip()
print(mystr.strip())
#baştaki (baştaki boşluklar) ve sondaki (sondaki boşluklar) karakterleri
# kaldırır (boşluk, kaldırılacak varsayılan baştaki karakterdir)

#swapcase()
print(mystr.swapcase())
#tüm büyük harflerin küçük olduğu ve tersinin olduğu bir dize döndürür.

#title()
print(mystr.title())
#her sözcükteki ilk karakterin büyük olduğu bir dize döndürür. Başlık veya başlık gibi.
#Kelime bir sayı veya sembol içeriyorsa, ondan sonraki ilk harf büyük harfe dönüştürülür.

