
students = [
    [85, 90, 80],
    [70, 65, 75],
    [95, 92, 98],
    [60, 55, 65],
    [80, 85, 90]
]

names = ["Anu", "Balu", "Charan", "Divya", "Esha"]

for i in range(5):
    total = sum(students[i])
    average = total / 3

    print("\nStudent:", names[i])
    print("Total:", total)
    print("Average:", average)

    if average >= 75:
        print("Result: Good")
    else:
        print("Result: Needs Improvement")

top = 0

for i in range(1, 5):
    if sum(students[i]) > sum(students[top]):
        top = i

print("\nTop Student:", names[top])
