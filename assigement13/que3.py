
student = {
    "name": "Vaishnavi",
    "age": 20,
    "course": "Computer Science"
}

key = input("Enter the key to check: ")


if key in student:
    print(f"YES Key '{key}' exists with value: {student[key]}")
else:

    print(f" NO Key '{key}' does not exist in the dictionary.")


