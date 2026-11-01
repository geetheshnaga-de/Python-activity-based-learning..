
test_cases = [
    [("T1", 500), ("T2", 1000), ("T1", 500)],
    [("T3", 200), ("T4", 300)],
    [("T5", 1500), ("T5", 1500)],
    [("T6", 700), ("T7", 2000), ("T7", 2000)],
    [("T8", 100), ("T9", 2500), ("T10", 400)]
]

for transactions in test_cases:
    seen = []
    duplicates = []

    for tid, amount in transactions:
        if tid in seen:
            duplicates.append(tid)
        else:
            seen.append(tid)

    print("\nTransactions:", transactions)
    print("Duplicates:", duplicates)

    for tid, amount in transactions:
        if amount > 1000:
            print("High transaction:", tid, amount)
