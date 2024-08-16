# for i in range(1,10):
#   for j in range(i,10):
#     print(" ", end=' ')
#
#   for j in range (i):
#     print("*", end=" ")
#
#   print("")
#
# for i in range(10, 0, -1):
#     for j in range(10, i, -1):
#       print(" ", end=' ')
#
#     for j in range(i):
#       print("*", end=" ")
#
#     print("")

#
# import re
# def validate_email(email):
#     if re.match(f"[^@]+@[^@]+\.[^@]+", email):
#         return True
#     return False
#
#
# #email = "example@domain.com"
# email = input("Enter email address: ")
# if validate_email(email):
#     print(email, "Valid email address")
# else:
#     print(email, "Invalid email address")


from validate_email import validate_email

email = input("Enter email address: ")
is_valid = validate_email(email)

if is_valid:
    print(email, "Valid email address")
else:
    print(email, "Invalid email address")
