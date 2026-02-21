def password_validity(password):
    if len(password) >=8:
        if password.haslower():
            if password():
                return "strong"
            else:
                return "weak"

pwd = "Yusie76445234"
response = password_validity(pwd)
print(response)
if response == "strong":
    print("password accepted")
else:
    print("password must contain atleast 8 characters")

