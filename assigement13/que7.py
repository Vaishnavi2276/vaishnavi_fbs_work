student = {
    "name": "Vaishnavi",
    "age": 20,
    "course": "Computer Science",
    "grade": "A"
}

print("Original Dictionary:", student)


key = input("Enter the key to remove: ")
if key in student:
    student.pop(key)
    print(f"Updated Dictionary (after removing '{key}'):", student)
else:
    print(f"Key '{key}' not found in the dictionary.")