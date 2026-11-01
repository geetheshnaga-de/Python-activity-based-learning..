
students = [
    ("abc@gmail.com", "22CSE101"),
    ("xyz@yahoo.com", "23ECE102"),
    ("studentgmail.com", "22CSE103"),
    ("hello@gmail.com", "2ACSE101"),
    ("test@gmail.com", "24ITC105")
]

for email, roll in students:
    email_valid = (
        "@" in email and "." in email
        and email.index("@") > 0
        and email.rfind(".") > email.index("@") + 1
        and email.rfind(".") < len(email) - 1
    )

    roll_valid = (
        len(roll) == 8
        and roll[:2].isdigit()
        and roll[2:5].isalpha()
        and roll[5:].isdigit()
    )

    print("\nEmail:", email)
    print("Email:", "Valid" if email_valid else "Invalid")
    print("Roll:", roll)
    print("Roll:", "Valid" if roll_valid else "Invalid")
