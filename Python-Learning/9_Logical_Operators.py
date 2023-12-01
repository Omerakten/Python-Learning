# Logical operators (and , or) = used to check info two or more conditinional statements is true

temp = int(input("What is the temperature outside?: "))
if temp >= 0 and temp <=30:
    print("the temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!")
    print("stay inside!")
