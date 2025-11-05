#linear search algorithm 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i # Found , return index
    return -1 #not found 
    
# example usage :
my_list = [10, 23, 45, 70, 11, 15]
target_value = 70

result = linear_search(my_list, target_value)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")