n = int(input("Enter a number: "))
l =len(str(n))
#print(l)

for i in range(l):
    x = n % 10
    y = int(n / 10)
    print(x, end='')
    n = y

print(n)