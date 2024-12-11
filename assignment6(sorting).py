# Bubble Sort function with comparison count
def bubbleSort(l):
    swapped = False
    count = 0
    for x in range(len(l)):
        for i in range(0, len(l) - x - 1):
            count += 1
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True
        if not swapped:
            break
    print(f"Bubble Sort Comparisons: {count}")
    return l

# Insertion Sort function with comparison count
def insertionSort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        # To count comparisons for the last key insertion
        if j >= 0:
            count += 1
    print(f"Insertion Sort Comparisons: {count}")
    return arr

# Selection Sort function with comparison count
def selectionSort(l):
    count = 0
    for i in range(len(l)):
        min_index = i
        for j in range(i + 1, len(l)):
            count += 1
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    print(f"Selection Sort Comparisons: {count}")
    return l

# Shell Sort function with comparison count
def shellSort(arr):
    count = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                count += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
            if j >= gap:
                count += 1
        gap //= 2
    print(f"Shell Sort Comparisons: {count}")
    return arr

# Read and parse the list from user input safely
def get_list_from_input():
    while True:
        try:
            user_input = input("Enter your unsorted list (e.g., [3, 1, 4, 1, 5]): ")
            l = eval(user_input, {"__builtins__": None}, {})
            if isinstance(l, list) and all(isinstance(x, (int, float)) for x in l):
                return l
            else:
                print("Invalid input. Please enter a list of numbers.")
        except:
            print("Invalid input. Please try again.")

# Main function to execute sorting and print results
def main():
    l = get_list_from_input()
    l2 = l.copy()
    l3 = l.copy()
    l4 = l.copy()

    # Perform Bubble Sort and print the result
    print("Bubble Sort Result:")
    print(bubbleSort(l))

    print()

    # Perform Selection Sort and print the result
    print("Selection Sort Result:")
    print(selectionSort(l2))

    print()

    # Perform Insertion Sort and print the result
    print("Insertion Sort Result:")
    print(insertionSort(l3))

    print()

    # Perform Shell Sort and print the result
    print("Shell Sort Result:")
    print(shellSort(l4))

# Run the main function
if __name__ == "__main__":
    main()
