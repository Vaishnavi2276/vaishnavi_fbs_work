dict1 = {
    "name": "Vaishnavi",
    "age": 20
}


dict2 = {
    "city": "Nagpur",
    "college": "ABC University"
}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)


dict3 = dict1.copy()  
dict3.update(dict2)    

print("Concatenated Dictionary:", dict3)