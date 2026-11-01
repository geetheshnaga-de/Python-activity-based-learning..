
test_cases = [
    [("Ravi", 9, 13), ("Ravi", 12, 16)],
    [("Anu", 9, 12), ("Anu", 13, 17)],
    [("Balu", 8, 12), ("Balu", 10, 14)],
    [("Kiran", 9, 11), ("Kiran", 11, 15)],
    [("Divya", 10, 14), ("Divya", 12, 16)]
]

for shifts in test_cases:
    print("\nShifts:", shifts)
    found = False

    for i in range(len(shifts)):
        for j in range(i+1, len(shifts)):
            name1, start1, end1 = shifts[i]
            name2, start2, end2 = shifts[j]

            if name1 == name2 and start1 < end2 and start2 < end1:
                print(name1, "- Shift Conflict")
                found = True

    if not found:
        print("No Shift Conflict")
