# #!/usr/bin/python
# def test_range(n):
#     print('Enter a value:')
#     x = input()
#
#     print('Enter Second value:')
#     y = input()
#
#     if n in range(x,y):
#         print( " %s is in the range "%str(n))
#     else :
#         print("The number is outside the given range.")
# test_range(20)
# import sys
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
# print("Version")
# print(sys.version_info())
# print(sys.version)
def write_lines_to_file(filename):
    lines = []
    print("Enter your lines of text (type 'DONE' on a new line to finish):")
    while True:
        line = input()
        if line.strip().upper() =='DONE':
            break
        lines.append(line)
    with open(filename,"w") as file:
        for line in lines:
            file.write(line + "\n")
    print(f"Text Successfully written to file name: {filename}")


filename = "output1.txt"  # Specify the file name
write_lines_to_file(filename)

