myDict={
    "brand": "Fold",
    "Country": "AUS",
    "Model": "Fold40",
    "Manufacture": "1964",
    "Color": ["red", "green", "blue"]
}
print(myDict)
print("Length: ", len(myDict))
print(myDict["Country"])
print(myDict["Manufacture"])
print(myDict["Color"])
print(type(myDict))

newDict =dict(name="Mosarraf", age=42, dob="14/07/1982")
print(newDict)
print(newDict.get("dob"))
print(newDict.keys())
newDict["district"] = "Satkhira"
print(newDict.keys())
print(newDict.values())
print("All items")
print(newDict.items())
if "Model" in myDict:
    print("Yes")


newDict.update({"Division": "Khulna"})
print(newDict)
print("Removing Item")
newDict.pop("Division")
print(newDict)

newDict.popitem()
print(newDict)
print("remove by del keyword")

del newDict["age"]
print(newDict)

# newDict.clear()
# print(newDict)

print("Loop in dictionary")
for x in newDict:
    print(x)

print("all values in a dictionary using loop")
for x in myDict:
    print(myDict[x])

print("values()")
for x in myDict.values():
    print(x)
print("keys()")
for x in myDict.keys():
    print(x)
print("Both key and values")
for x, y in myDict.items():
    print(x, y)


car1 = {
    "brand": "Fold",
    "Country": "AUS",
    "Model": "Fold40",
    "Manufacture": "1964",
}

car2 = {
    "brand": "Toyota",
    "Country": "Japan",
    "Model": "Toyota",
    "Manufacture": "1994",
}


car3 = {
    "brand": "BMW",
    "Country": "Japan",
    "Model": "BMW",
    "Manufacture": "1984",
}

myCars = {
    "car1": car1,
    "car2": car2,
    "car3": car3
}

print(myCars)
print(myCars["car2"]["brand"])

print("accessing nested dictionary")
for x, obj in myCars.items():
    print(x)
    for y in obj:
        print(y + ": ", obj[y])


