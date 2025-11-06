#You are given a sorted list of integers and a target integer value. Write a function that uses
#  the binary search algorithm to determine if the target exists in the list.

# If the target value is found in the list, return True.

# If the target value is not present in the list, return False.

# Example:
# Input: arr = [1][3][5][7][9], target = 5
# Output: True

# Input: arr = [1][3][5][7][9], target = 6
# Output: False

def binary_search(arr, target):
    low = 0 
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return True  # Found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False  # Not found
# example usage :
my_list = [1, 3, 5, 7, 9]
target_value = 3

result = binary_search(my_list, target_value)
if result:
    print("Element found in the list.")
else:
    print("Element not found in the list.")
target_value = 6
result = binary_search(my_list, target_value)
if result:
    print("Element found in the list.")
else:
    print("Element not found in the list.")
        



