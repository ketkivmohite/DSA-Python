# Bubble Sort
def bubble_sort(lst):
    size = len(lst)

    # Outer loop to access each element
    for i in range(size):

        # Inner loop to compare adjacent elements
        for j in range(size - i - 1):

            # Swap elements if necessary
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

data_list = [15, 16, 6, 8, 5]

print(f"Unsorted List: {data_list}")

sorted_list = bubble_sort(data_list)

print(f"Sorted List: {sorted_list}")

#Bubble Sort
# Can you write the bubble sort program on your own?
# Create a function named bubble_sort() that takes a list as its argument.
# Sort the list in ascending order within the function and return the sorted list.
# Print the sorted list from outside the function.

# Replace ___ with your code

# Bubble Sort
# Can you write the bubble sort program on your own?
# Create a function named bubble_sort() that takes a list as its argument.
# Sort the list in ascending order within the function and return the sorted list.
# Print the sorted list from outside the function.

def bubble_sort(lst):
    size = len(lst)
    for i in range(size):
        for j in range(size - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# take inputs and convert them to a list
data_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

# call the bubble sort function
sorted_list = bubble_sort(data_list)

# print the sorted list
print("Sorted List:", sorted_list)

#Bubble Sort in Descending Order
# Write a program to sort the list items in descending order using bubble sort.

# Create a function named bubble_sort() that takes a list as its argument.
# Sort the list in descending order within the function and return the sorted list.
# Print the sorted list from outside the function.
# Tip: In this case, you need to swap elements if the current element is smaller than the next element.
# Replace ___ with your code

def bubble_sort(lst):
    size = len(lst)
    for i in range(size):
        for j in range(size - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
    # write your code here
    ___


# take integer inputs and convert it to a list    
data_list = list(map(int, input("Enter your list: ").split()))

sorted_list = bubble_sort(data_list)
print(sorted_list)

# Bubble sort in ascending order
def bubble_sort(lst):

    size = len(lst)

    for i in range(size):
        
        swapped = False
        
        for j in range(size - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        
        # This part executes if the list is sorted        
        if not swapped:
            break

    return lst

data_list = [1, 2, 4, 9, 6]

sorted_list = bubble_sort(data_list)
print(sorted_list)

#Optimized Bubble Sort
# Write a program to sort the list items in descending order using optimized bubble sort.

# Create a function named bubble_sort() that takes a list as an argument.
# Inside the function, sort the list in descending order using optimized bubble sort.
# Print the sorted list outside the function.
# Replace ___ with your code

def bubble_sort(lst):
    size = len(lst)

    for i in range(size):
        swapped = False

        for j in range(size - 1 - i):
            # Swap for descending order
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True

        # If no elements were swapped, list is already sorted
        if not swapped:
            break

    return lst


# take integer inputs and convert it to a list
data_list = list(map(int, input("Enter your list: ").split()))

sorted_list = bubble_sort(data_list)
print(sorted_list)
