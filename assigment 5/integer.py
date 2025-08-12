amount = int(input("Enter the amount: "))


denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]


note_counter = {}
for note in denominations:
    if amount >= note:
        count = amount // note
        amount = amount % note
        note_counter[note] = count
print("\nMinimum number of notes needed:")
for note, count in note_counter.items():
    print(f"₹{note} x {count}")
