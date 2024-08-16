print("Print even number from 1 to N")
n = int(input("Enter a number"))
i = -1
while i < n:
    i += 1
    if i%2 == 1:
        continue
    print(i, end=" ")
