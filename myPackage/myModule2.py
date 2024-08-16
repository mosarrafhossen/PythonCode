def fnReverseNumber():
    n = int(input("Enter a number: "))
    l = len(str(n))
    for i in range(l):
        x = n % 10
        y = int(n / 10)
        print(x, end=' ')
        n = y
#fnReverseNumber()