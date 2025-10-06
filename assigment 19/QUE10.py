def my_range(start, stop=None, step=1):
    """
    Generator function that mimics the behavior of built-in range().
    
    Parameters:
    - start: starting value (or stop if stop is None)
    - stop: stopping value (exclusive)
    - step: step increment (default 1)
    """

    if stop is None:
        stop = start
        start = 0

    
    if step == 0:
        raise ValueError("step argument must not be zero")

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step



print("Custom range examples:")
for num in my_range(5):  
    print(num, end=" ")
print()

for num in my_range(2, 10, 2):  
    print(num, end=" ")
print()

for num in my_range(10, 2, -2):  
    print(num, end=" ")
