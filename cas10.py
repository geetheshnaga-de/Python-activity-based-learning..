
records = [
    "22-CSE-101",
    "23-ECE-205",
    "2A-CSE-110",
    "24-MECH-305",
    "22-CSE-101"
]

seen = []

for record in records:
    parts = record.split("-")

    valid = (
        len(parts) == 3
        and len(parts[0]) == 2
        and parts[0].isdigit()
        and parts[1].isalpha()
        and len(parts[1]) >= 2
        and len(parts[2]) == 3
        and parts[2].isdigit()
    )

    print("\nRegistration:", record)

    if not valid:
        print("Invalid Format")
    elif record in seen:
        print("Duplicate Record")
    else:
        seen.append(record)
        print("Valid Record")
        print("Year:", parts[0])
        print("Branch:", parts[1])
        print("Student Number:", parts[2])
