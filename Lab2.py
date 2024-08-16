# Name = "Hasan"
# txt = f"Congrations! Mr. {Name}"
# print(txt)
import random

#
# f = open("Lab2.txt", "w")
# f.write("Welcome to EDGE Project\n. After Newline ")
# f.close()
# f = open(f"Lab2.txt", "r")
# print(f.read())
#
# f = open("Lab2.txt", "a+")
# f.write("\nNewly Added line")
# f.close()
#
# f = open(f"Lab2.txt", "r")
# print(f.read())


# f = open("demofile.txt", "r")
# print(f.read())

# print("........ using loop")
# print(".......")
# f = open("demofile.txt","r")
# for x in f:
#     print(x)
# f.close()


# print("deleted contents")
# f = open("Lab2.txt","w")
# f.write("Woo! Contents has been deleted")
# f.close()

# print("file creation")
# f = open("demofile4.txt","x")
# f.write("Newly created files")
# f.close()

# f = open("demofile4.txt","r")
# print(f.read())
#FileNotFoundError) or permissions issues.
# try:
#     with open('demofile4.txt', 'r') as file:
#         content = file.read() # process content
#         print(content)
# except FileNotFoundError:
#     print("File not found!")
# except PermissionError:
#     print("Permission denied to open file!")
# except Exception as e:
#     print("Error:", e)

# x = "EDGE"
# try:
#   print(xx)
# except:
#   print("An exception occurred")
#Write a program that writes 100 random numbers to a file named 'numbers.txt'. Each random number should be seperated in a white space in the range of 1 through 100
file = open("numbers.txt", "w")
sumOfNumber = 0
for i in range(100):
    number = int(random.randint(1,100))
    sumOfNumber = sumOfNumber + number
    file.write(str(number) + ' ')
file.close()
print(sumOfNumber)
file2 = open("numbers.txt","r")
print(file2.read())
file2.close()


