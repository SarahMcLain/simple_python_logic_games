import re

email = input("What is your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("valid")
# else:
#     print("invalid")

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.", email):
#     print("valid")
# else:
#     print("Invalid")

if re.search(r"^\w.+@\w.+\.(com|edu|net|org|gov)$", email, flags=re.IGNORECASE):
    print("valid")
else:
    print("Invalid")