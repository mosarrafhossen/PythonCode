
def fibo(n):
    a = 0
    b = 1
    print(a)
    print(b)
    x = 0

    while x <= n:
        c = a + b
        x = x + 1
        print(c)
        #list1 = {c}
        #print (list1)
        a = b
        b = c

fibo(10)