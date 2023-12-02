import time
# for loops = a statement that will execute it`s block of code
#              a limited amount of times
#              while loop = unlimited
#              for loop = limited

for i in range (10):
    print(i+1)

for i in range(50,100+1,2): # (start, end , kacar kacar artsin)
    print(i)

for seconds in range(10,0,-1):
        print(seconds)
        time.sleep(1)  # 1 saniye aralikla yazdiriyor .sleep yapisi icin time import etmen gerek
print("Happy New Year!")
