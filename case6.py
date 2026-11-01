
appliances = ["Fan", "Light", "TV"]

test_cases = [
    [2, 1, 3],
    [3, 2, 4],
    [1, 1, 2],
    [4, 2, 3],
    [2, 3, 5]
]

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday"]

for i in range(5):
    total = sum(test_cases[i])

    print("\nDay:", days[i])
    print("Fan:", test_cases[i][0])
    print("Light:", test_cases[i][1])
    print("TV:", test_cases[i][2])
    print("Total Units:", total)

    if total > 6:
        print("High Consumption")
    else:
        print("Normal Consumption")
