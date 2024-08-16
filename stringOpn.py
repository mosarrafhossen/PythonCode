a = "Hello, World!"
print(a.lower())
print(a.upper())


aa = "Hello, World!"
print(aa.replace("H", "J"))


a = "  Hello, World!  "
print(a.strip()) # returns "Hello, World!"


print(aa.split(","))


age = 42
print(f"My name is Mosharraf, I am {age : .2f}")

print("zfill()	Fills the string with a specified number of 0 values at the beginning")

txt = "50"

x = txt.zfill(6)

print(x)

txtnum = "104"
x = txtnum.zfill(5)
print(x)


#string method

txtString = f"welcome to WZPDCL, ICT WZPDCL"
y = txtString.capitalize()
print(y)


y = txtString.upper()
print(y)

print(txtString.lower())

print(txtString.title())
print(txtString.encode())
print(txtString.count('WZPDCL'))
txtString = "I love apples, apple are my favorite fruit"
print(txtString.count("apple", 5, 24))

#Join all items in a tuple into a string, using a hash character as separator: join()

myTuple = ("Zabir", "Nayeem", "Mosharraf", "Aanas", "Siddiqua")
x = "# ".join(myTuple)
print(x)

print("............")
#The join() method takes all items in an iterable and joins them into one string.
myDict = {"name " : "Mosharraf", "Country" : "BD"}
mySeperator = "& "
x = mySeperator.join(myDict)
print(x)


print(bool("xyz"))


a = 30
b = 200

if (a > b):
    print("a greater than b")
else:
    print("a less than b")

