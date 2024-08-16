import re
email = input("Enter Your Email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]
print(f"Your username is {username} & domain is {domain}")

def validate_email(email):
    if re.match(f"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

# email = input("Enter your email address: ")
# length = len(email)
# loc = email.find("@")
#
#
# username = email[:loc]
# domain = email[loc+1:]
# print("User name is:", username)
# print("Domain name is:", domain)

if validate_email(email):
    print(email, "is a valid address")
else:
    print(email, "is not a valid address")

