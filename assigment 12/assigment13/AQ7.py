my_dict = {
    "name": "Vaishnavi",
    "age": 20,
    "city": "Nagpur",
    "college": "ABC University"
}

print("Original Dictionary:", my_dict)

key_to_remove = input("Enter the key to remove: ")


if key_to_remove in my_dict:
    removed_value = my_dict.pop(key_to_remove)
    print(f"Key  removed with value: {removed_value}")
else:
    print(f"Key not found in the dictionary.")

print("Updated Dictionary:", my_dict)