print("For loop and break")
for x in range(9):
    if x == 4:
        break
    print(x)
print("For loop and Continue")
for i in range(9):
    if i == 4:
        continue
    print(i)

print("While loop and break")
i = 0
while i < 9:
    if i == 3:
        break
    print(i)
    i += 1

print("While loop and continue")
print("Print old number from 1 to 10")
i = 0
while i < 10:
    i += 1
    if i%2 == 0:
        continue
    print(i)

print("While loop and continue")
print("Print even number from 1 to 10")
i = -1
while i < 10:
    i += 1
    if i%2 == 1:
        continue
    print(i)


