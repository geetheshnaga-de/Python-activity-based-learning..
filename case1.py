
test_cases = [3, 4, 5, 6, 7]

for n in test_cases:
    print("\nPattern for n =", n)

    for i in range(n):
        print(" " * (n-i-1), end="")
        for j in range(2*i+1):
            if j == 0 or j == 2*i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for i in range(n-2, -1, -1):
        print(" " * (n-i-1), end="")
        for j in range(2*i+1):
            if j == 0 or j == 2*i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
