import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%M"))
print(x.strftime("%m"))
print(x.strftime("%b"))
x = datetime.datetime(2024, 6, 22)
print(x)

x = input("What is your name? ")
print(f"Hello, {x}")

