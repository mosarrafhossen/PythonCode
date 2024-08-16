import random
import time
import re


def main_menu():
    time.sleep(1)
    print("MAIN MENU")
    print("1. String Operation")
    print("2. Number Operation")
    print("3. EXIT")


def main():
    #intro()
    while (True):
        main_menu()
        choice = input('\nEnter choice(1, 2 or 3): ')
        print()

        if choice == '1':
            while True:
                #report_menu()
                rchoice = input('Choice(1-> EmailValidation,2-> RandomNumberGenerator, 3->Pyramid): ')
                print()
                if rchoice == '1':
                    email = input("\nEnter an email address: ")
                    if (fnEmailValidation(email)) is True:
                        print(f"\nProvided email address [{email}] is valid")
                    else:
                        print(f"\nProvided email address [{email}] not valid")
                    pass
                elif rchoice == '2':
                    #search_record()
                    #print("Write multiple line in file")
                    filename = "outputFile.txt"  # Specify the file name
                    write_lines_to_file(filename)
                    #pass
                elif rchoice == '3':
                    #print("How many number?")
                    n = int(input("How many number?"))
                    createPyramid(n)
                elif rchoice == '4':
                    break
                else:
                    print('\nInvalid input !!!')
                print()

        if choice == '2':
            while True:
                #admin_menu()
                print("\n 1 for Number Reverse")
                print("\n 2 for Fibonacci Series")
                print("\n 3 for Find Factorial of a Number")
                print("\n 4 for Even Number Set")
                print("\n 5 for Greatest number between 3")
                print("\n 6 for Generate 100 Random Number and write in a file")
                echoice = input('\nEnter choice(1-6): ')
                print()
                if echoice == '1':
                    #write_record()
                    fnReverseNumber()
                    #pass
                elif echoice == '2':
                    #read_records()
                    fibo()
                    #pass
                elif echoice == '3':
                    #search_record()
                    n = int(input("Enter a number: "))
                    print(f"Factorial of {n} is {fnFactorial(n)}")
                    pass
                elif echoice == '4':
                    #modify_record()
                    fnEvenNumberSet()
                elif echoice =='5':
                    x = input("Enter a number")
                    y = input("Enter a number")
                    z = input("Enter a number")
                    print(f"Greatest number between {x}, {y} and {z} is {max_of_three(x, y, z)}")
                elif echoice == '6':
                    #modify_record()
                    fnRandomNumberGenerator()
                else:
                    print('\nInvalid input !!!')
                    break


        elif choice == '3':
            print('Thanks for using Switch Statements')
            break
        else:
            print('Invalid input!!!')
            print()

def write_lines_to_file(filename):
    lines =[]
    print("Enter multiple line of text (type 'DONE' on a new line to finish):")
    while True:
        line = input()
        if line.strip().upper()=="DONE":
            break
        lines.append(line)
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")
        print(f"File [{filename}] has been saved successfully!")


def fnEvenNumberSet():
    print("Print even number from 1 to N")
    n = int(input("Enter a number to set range:"))
    i = -1
    while i < n:
        i += 1
        if i % 2 == 1:
            continue
        print(i, end=" ")


def max_of_two(x, y):
    if x > y:
        return x
    return y


def fnRandomNumberGenerator():
    file = open("100Numbers.txt", "w")
    for i in range(100):
        number = random.randint(1, 100)
        file.write(str(number) + " ")
    file.close()

    file2 = open("100Numbers.txt", "r")
    print(file2.read())
    file2.close()



def max_of_three(x, y, z):
    return max_of_two( x, max_of_two( y, z ) )

def fnEmailValidation(email):
    if re.match(f"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


def createPyramid(n):
    for i in range(0, n):
        print("#" * i)

    for i in range(n, 0, -1):
        print("#" * i)

def fnFactorial(n):
    if n == 0 or n ==1:
        return 1
    elif n>1:
        return n * fnFactorial(n-1)


def fnReverseNumber():
    n = int(input("Enter a number: "))
    l = len(str(n))
    print("Reverse number is : ")
    for i in range(l):
        x = n % 10
        y = int(n / 10)
        print(x, end=' ')
        n = y


def fibo():
    n = int(input("\nEnter a number for series: "))
    a, b = 0, 1
    print(a, end=' ')
    x = 0
    while x <= n:
        c = a + b
        x = x + 1
        print(c, end=' ')
        a = b
        b = c

main()