mylist = ["apple", "banana", "cherry"]
mylist_2 = ["apple", "banana", "cherry", "apple", "cherry"]
mylist_3 = [3, 2, 1, 4, 7, 5, 6, 8, 9]
mylist_4 = list(("snowball1", "snowball2", "snowball3", True))

print(mylist)
print(mylist_2)
print(mylist_3)
print(mylist_4)

print(len(mylist))
print(len(mylist_2))
print(len(mylist_3))
print(len(mylist_4))

print(type(mylist))
print(type(mylist_3))
print(type(mylist_4))

print(mylist[1])
print(mylist_3[-1])

print(mylist_3[2:5])
print(mylist_3[:6])
print(mylist_3[6:])
print(mylist_3[-4:-1])

if "apple" in mylist:
    print("Yes")
else:
    print("No")

mylist[1] = "Snowball"
print(mylist)
mylist_2[2:4] = ["Snowball", "Snowballball"]
print(mylist_2)

mylist_4.insert(2, "Snowball2.5")
print(mylist_4)

mylist_4.append("Snowball4")
print(mylist_4)

mylist.extend(mylist_4)
print(mylist)

mylist_2.remove("apple")
print(mylist_2)

mylist_2.pop(1)
print(mylist_2)

del mylist_2[1]
print(mylist_2)

del mylist_2

mylist.clear()
print(mylist)

for x in mylist_4:
    print(x)

for i in range(len(mylist_4)):
    print(mylist_4[i])

i = 0
while i < len(mylist_4):
    print(mylist_4[i])
    i = i + 1

[print(x) for x in mylist_4]

print(mylist_4)
new_list = []
for x in mylist_4:
    if "ball" in str(x):
        new_list.append(x)
print(new_list)

new_list.append("apple")
new_list.append("banana")
newlist = [x for x in new_list if x != "apple"]
print(newlist)

mylist_5 = [x for x in range(10)]
print(mylist_5)

mylist_6 = [x for x in range(10) if x < 5]
print(mylist_6)

mylist_7 = [x if x != "banana" else "orange" for x in newlist]
# Return the item if is not banana, if it is banana return orange
print(mylist_7)

mylist_3.sort()
print(mylist_3)

mylist_3.sort(reverse=True)
print(mylist_3)

mylist_3.reverse()
print(mylist_3)

my_list = mylist_3.copy()
print(my_list)

my_list2 = [10, 11, 12, 13, 14, 15]
mylist_number = my_list + my_list2
print(mylist_number)
