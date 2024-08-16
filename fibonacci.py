# a, b = 0, 1
#
# n = 10
#
# for i in range(n):
#
#    print(a)
#
#    a, b = b, a + b


# Fibonacci Series in Python Using For Loop
# initialize two variables, with value 0
a, b = 0, 1
series_length = 10

print(a, b, end=' ')
for i in range(series_length):
    c = a + b
    print(c, end=' ')
    a = b
    b = c

