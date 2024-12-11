def fibonacci_search(arr, target):
    n = len(arr)
    
    # Initialize Fibonacci numbers
    m2 = 0
    m1 = 1
    m0 = m2 + m1
    
    # Find the smallest Fibonacci number greater than or equal to the length of the array
    while m0 < n:
        m2 = m1
        m1 = m0
        m0 = m1 + m2
    
    # Initialize offset
    offset = -1
    
    # Perform the Fibonacci search
    while m0 > 1:
        i = min(offset + m2, n - 1)
        
        if arr[i] < target:
            m0 = m1
            m1 = m2
            m2 = m0 - m1
            offset = i
        
        elif arr[i] > target:
            m0 = m2
            m1 = m1 - m2
            m2 = m0 - m1
        
        else:
            return i  # Return the index if the element is found
    
    # Check the last position
    if m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1  # Return the index if the element is found
    
    return -1  # Return -1 if the element is not found

# Input handling
l = eval(input("Enter your ordered list (e.g., [1, 2, 3, 4, 5]): "))
k = int(input("Element to search: "))

if not all(l[i] <= l[i+1] for i in range(len(l)-1)):
    print("Error: The list is not ordered.")
else:
    # Perform Fibonacci search and print result
    index = fibonacci_search(l, k)
    if index != -1:
        print(f"Element {k} found at index {index}.")
    else:
        print(f"Element {k} not found in the list.")
