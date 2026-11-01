
passwords = [
    "Python@123",
    "hello",
    "College123",
    "Abc@4567",
    "Student#456"
]

for password in passwords:
    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if len(password) >= 8 and upper and lower and digit and special:
        print(password, "- Valid Password")
    else:
        print(password, "- Invalid Password")
