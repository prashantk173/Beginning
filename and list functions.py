lucky_nums = [1,3,7,17]
fav_animes = ["One_piece", "Haikyuu","GTO", "Demon_Slayer"]

print(fav_animes)
# using extend and append function

fav_animes.append("DBZ") # append is used to add more elements in the list.
print(fav_animes)
fav_animes.extend(lucky_nums) # extend fn is used to add a list to the existing list.
print(fav_animes)
fav_animes.insert(1,"Durarara") #insert fn is used to add an elemnt in the list in the desired location using the index value.
print(fav_animes)
fav_animes.remove("Durarara") # remove fn is used to remove a elemt from the list.
print(fav_animes)
fav_char= ["Luffy", "Zoro"]
fav_animes.extend(fav_char)
print(fav_animes)

fav_animes.remove("DBZ") # the remove fn only takes strings and cannot be used for lists. so removing DBZ
print(fav_animes)
fav_animes.pop()# pop fn is used to remove an element from the list
print(fav_animes)
fav_animes.pop(5)
print(fav_animes)
print(fav_animes.index("GTO")) # gives the index position of the element in the list and also this can be used to find the presence of the element in the list.
fav_animes.append("GTO")
print(fav_animes)
print(fav_animes.count("GTO")) # counts the number of times the element is repeated in the list.
print(fav_animes)
print(len(fav_animes))# gives the total no of elements in the list.
lucky_nums.sort() # sort fn sorts the values in ascending order. in combination of int and str it will not work.
print(lucky_nums)
lucky_nums.reverse() # to reverse order.
print(lucky_nums)
fav_animes.reverse()# reverse option isused to reverse the whole list elements wether they are int or str.
print(fav_animes)
fav_anime2 = fav_animes.copy() # creating a copy of the list
print(fav_anime2)# any changes made to the copy will not reflect in the main list.
fav_anime2.append("Mob_Psycho")
print(fav_anime2)
fav_animes.clear() # clears the list elements and makes the list empty
print(fav_animes)
