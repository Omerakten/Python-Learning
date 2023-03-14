#---------------LİSTELER--------------
#Listeler içerisinde birden fazla veriyi barındırabileceğimiz koleksiyon dediğimiz yapılardırdar.
#Listeleri kullanarak aynı anda birden fazla numarayı metni yada veri tipini aynı değişken, aynı yapı içerisinde
#tutabiliriz.

mylist = [1,2,3,5,4,5,6,7,8]  #LİSTELER BU ŞEKİLDE [] KÖŞELİ PARANTEZLER İLE GÖSTERİLİR
print(mylist) #çıktı [1, 2, 3, 4, 5, 6, 7, 8]
print(type(mylist)) #mylist değişkeninin türüne bakınca çıktısı :  <class 'list'> olacaktır buradan liste olduğunuda görebiliriz

#liste içinde bir veriyi başka bir veriyle değiştirmek istersek;
mylist[0] = 9 # 0 ıncı indeksin yerine 9 yaz demiş oluyoruz
print(mylist) # çıktısı [9, 2, 3, 4, 5, 6, 7, 8]

#-------------------- LİSTE METODLARI ------------------------
#append
mylist.append(55)
print(mylist)
#listenin sonuna bir öğe ekler.

#clear
# mylist.clear()
# print(mylist)
# bir listedeki tüm öğeleri kaldırır.

#copy
clone = mylist.copy()
print(clone)
clone.append(23)
print(clone)
#copy metodu var olan bir listeyi kopyalayıp başka bir değişkende oluşturulmaya yarar

#count
print(mylist.count(5))
#count metodu seçilen liste içerisinde parantez içinde belirtilen nesneden kaç tane oldğunu gösterir

#extend
fruits = ['elma', 'muz', 'mandalina']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
#belirtilen liste öğelerini (veya herhangi bir yinelenebilir öğeyi) geçerli
# listenin sonuna ekler.

#index
print(mylist.index(3))
#belirtilen değerin ilk geçtiği yerdeki konumu döndürür.

#insert
fruits = ['elma', 'muz', 'mandalina']
fruits.insert(1,"portakal")
print(fruits)

#pop
print(mylist.pop())#55
print(clone.pop())#23
#eğer pop() olarak parantez boş kalırsa listenin sonuncu elemanını yazdırır
mylist.pop(0) #yani baştaki karakteri kaldıryor 0. indeks olduğu için 9 kalktı
print(mylist)

#remove
mylist.remove(5)
#belirtilen değere sahip öğenin ilk oluşumunu kaldırır.
print(mylist)

#reverse
mylist.reverse()
print(mylist)
#öğelerin sıralama düzenini tersine çevirir.

#sort
fruits = [200,15,6000]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
# listeyi varsayılan olarak artan şekilde sıralar.
# Sıralama ölçütlerine karar vermek için bir işlev de yapabilirsiniz.
# listeyi küçükten büyüğe sıralar
# reverse yaparsak büyükten küçüğe de sıralayabiliriz