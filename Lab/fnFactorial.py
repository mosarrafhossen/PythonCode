def fnFactorial(n):
    if n == 0 or n ==1:
        return 1
    elif n>1:
        return n * fnFactorial(n-1)

n = int(input("Enter a number: "))
print(fnFactorial(n))
