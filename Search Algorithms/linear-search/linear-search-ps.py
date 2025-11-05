#"You are searching for a friend's phone number in your unsorted phone contact list. 
# The list is not sorted in any order, so you check each contact one by one from the top until you find
#  your friend's name. If the name is found, you read the phone number;
#  otherwise, you reach the end of the list and conclude the contact isn't there."

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found, return index
    return -1  # Not found

# Example usage:
my_list = [10, 23, 45, 70, 11, 15]
target_value = 70
result = linear_search(my_list, target_value)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")
 