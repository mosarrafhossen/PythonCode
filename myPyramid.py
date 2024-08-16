for i in range(0,10):
    print("#"*i)


for i in range(10,0,-1):
    print("#"*i)

print("Two dimension array")
for i in range(1,6):
    for j in range(1,6):
        print(f"({i},{j})")


x, y = map(int, input().split())
print(x, y)
print(y, x)
number =list(map(int,input("Enter some value").split()))
print(number)
print(*number)

