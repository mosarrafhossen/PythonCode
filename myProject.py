def checkOddEven(n):
    if n % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")
#n = int(input("Enter a number: "))
# checkOddEven(n)
def calFact(n):
    if n==1 or n==0:
        print(n)
        return 1
    elif n>1:
        print(n)
        return n * calFact(n-1)


#print(".......")
#n = int(input("Enter a number: "))
#print(calFact(n))

def number_to_string(argument):
    #n = input("Enter a number: ")
    match argument:
        case 'f':
            n = int(input("Number: "))
            calFact(n)
            return calFact(n)
        case 'o':
            n = int(input("Number: "))
            return checkOddEven(n)
        # case 2:
        #     return "two"
        # case 3:
        #     return "Three"
        # case 4:
        #     return "Four"
        # case 5:
        #     return "Five"
        # case 6:
        #     return "Six"
        # case 7:
        #     return "Seven"
        # case 8:
        #     return "Eight"
        # case 9:
        #     return "Nine"
        case x:
            return 0

print("Enter your choice")
print("f for factorial")
print("o for odd/even")
print("p for pyramid")
print(("x for exit"))
n = input("Enter your choice: ")
head = number_to_string(n)
print(head)