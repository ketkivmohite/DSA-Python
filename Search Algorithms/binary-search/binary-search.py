def binary_search(arr, target):
    # set initial boundaries : low at the start , high at the end 
    low = 0 
    high = len(arr) - 1
    
    # loop as long as the search space is valid (low <= high)
    while low <= high:
        # find the middle index between low and high 
        mid = (low + high) // 2
        
        # if the target is found at mid, return mid index
        if arr[mid] == target:
            return mid  # Found, return index
        # if target is greater than mid value, search in the right half
        elif arr[mid] < target:
            low = mid + 1
        # if target is less than mid value, search in the left half
        else:
            high = mid - 1
    
    # if the loop ends with no result the target is not in the list return -1
    return -1  # Not found


# example usage :
my_list = [10, 23, 45, 70, 11, 15]

# binary search requires a sorted array  
my_list.sort()  # Sort the list first

target_value = 70

result = binary_search(my_list, target_value)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")

print("Sorted list:", my_list)
