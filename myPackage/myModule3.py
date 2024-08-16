def fibo():
    n = int(input("\nEnter a number for series: "))
    a, b = 0, 1
    print(a)
    x = 0
    while x <= n:
        c = a + b
        x = x + 1
        print(c, end=' ')
        a = b
        b = c


#fibo(10)