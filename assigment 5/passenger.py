num_passengers = int(input("Enter the number of passengers: "))
ticket_cost = float(input("Enter the cost per ticket: "))



for i in range(1, num_passengers + 1):




    age = int(input(f"Enter age of passenger {i}: "))
    
    if age < 12:
        discount = 0.30  
    elif age > 59:
        discount = 0.50  
    else:
        discount = 0.0  
    
    cost_for_passenger = ticket_cost * (1 - discount)
    total_cost += cost_for_passenger
    print(f"\nTotal ticket cost for all passengers: {total_cost:}")
