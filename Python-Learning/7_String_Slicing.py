#Slicing = create a substring by extracting elements from another string
#           indexing [] or slice () slice(start,-stop)
#           [start:stop:step]

# name = "Bro Code"
#
# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[::2]
# reversed_name = name[::-1]
# print(reversed_name)

#multiple slice
website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4)

print(website1[slice])
print(website2[slice])