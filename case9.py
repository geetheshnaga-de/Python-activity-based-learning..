
test_cases = [
    [35, 40, 45],
    [80, 85, 90],
    [25, 30, 28],
    [55, 60, 65],
    [90, 95, 100]
]

locations = ["Area A", "Area B", "Area C",
             "Area D", "Area E"]

for i in range(5):
    readings = test_cases[i]
    average = sum(readings) / len(readings)

    print("\nLocation:", locations[i])
    print("Readings:", readings)
    print("Average:", average)
    print("Maximum:", max(readings))
    print("Minimum:", min(readings))

    if average > 60:
        print("Status: Above Safe Limit")
    else:
        print("Status: Normal")
