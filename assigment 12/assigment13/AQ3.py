my_dict = {
    "name": "Vaishnavi",
    "age": 20,
    "city": "Nagpur"
}


key = input("Enter the key to check: ")


if key in my_dict:
    print(f"Yes, the key '{key}' exists in the dictionary with value: {my_dict[key]}")
else:
    print(f"No, the key '{key}' does not exist in the dictionary.")