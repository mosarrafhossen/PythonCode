#A list can contain different data types:
lst = ["xyz", 45.5, 45, True, "Male", 'car']

print(lst)
print(type(lst))


#Using the list() constructor to make a List:
myList = list(('Toyota','BMW', 'Pajero'))
print(myList)
print(myList[0])

if 'RR' in myList:
    print("Yes, Toyota is in myList")
else:
    print("No, Not in myList")


    myList[1] = 'Rols Royace'

print(myList)

myList.append("Bugatti Veyron")
print(myList)

myList.insert(2, "Labmergini")
print(myList)

myList.insert(3, "Range Rover")
print(myList)

fruits = ["apple", "banana", "cherry"]
myList.extend(fruits)
print(myList)

myContry = ("BD", "CN", "AUS", "USA", "KSA", "IRAN")
myList.extend(myContry)
print(myList)
myList.append("USA")
print(myList)

myList.append("Bugatti Veyron")
print(myList)

myList.append("Bugatti Veyron")
print(myList)

print("..........")
myList.remove("Bugatti Veyron")
print(myList)

myList.pop(15)
print(myList)

del myList[15]
print(myList)

for x in myList:
    print(x)

print("For Loop in List")
for i in range(len(myList)):
    print(myList[i])

print("Using while loop")

i = 0
while i < len(myList):
    print(myList[i])
    i+= 1


#List comprehension
newList = []
for x in myList:
    if 'A' in x:
        newList.append(x)
print(newList)


nnewList =[]
nnewList = [x for x in myList if 'A' in x]
print(nnewList)

print("usign range() function")

nnewList = [x for x in range(15) if x < 10]
print(nnewList)


nnewList =[]
nnewList = [x.lower() for x in myList if 'A' in x]
print(nnewList)

nnewList =[]
nnewList = ["Cars" for x in myList if 'A' in x]
print(nnewList)
print("list", myList)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print("Case sensitive sort")
thislist = ["orange", "Mango", "kiwi", "pineapple", "Banana"]
thislist.sort(key=str.upper)
print(thislist)

print("Case sensitive sort")
thislist = ["orange", "Mango", "kiwi", "pineapple", "Banana"]
thislist.sort(key=str.lower)
print(thislist)

print("copy in list")
nnewList2 = myList.copy()
print(nnewList2)

print("copy in list using list")
nnewList3 = list(myList)
print(nnewList3)


print("List Join")
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c']

print(list1 + list2)

print("List join using append")
for x in list2:
    list1.append(x)
print(list1)

print("Use the correct method to add multiple items (more_fruits) to the fruits set")
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)



