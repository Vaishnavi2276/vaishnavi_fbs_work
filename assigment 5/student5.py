num_students = int(input("Enter number of students: "))

percentages = []


for i in range(num_students):
    print(f"Enter marks for Student {i+1}:")
    
    total_marks = 0
    
   
    for j in range(1, 6):
        mark = float(input(f"  Enter mark for subject {j}: "))
        total_marks += mark

    
    percentage = (total_marks / 500) * 100
    percentages.append(percentage)


print("\n--- Student Percentages ---")
for i, pct in enumerate(percentages, start=1):
    print(f"Student {i}: {pct:.2f}%")


average_percentage = sum(percentages) / num_students
print(f"\nAverage Percentage: {average_percentage:.2f}%")
