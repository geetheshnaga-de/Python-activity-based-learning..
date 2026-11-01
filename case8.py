
test_cases = [
    ("P101", 100, 20),
    ("P102", 250, 5),
    ("P103", -50, 10),
    ("P104", 500, 0),
    ("P105", 300, 15)
]

for pid, price, stock in test_cases:
    print("\nProduct:", pid)

    if price <= 0 or stock < 0:
        print("Invalid Product")
    else:
        value = price * stock
        print("Price:", price)
        print("Stock:", stock)
        print("Total Value:", value)

        if stock < 10:
            print("Replenishment Required")
        else:
            print("Stock Available")
