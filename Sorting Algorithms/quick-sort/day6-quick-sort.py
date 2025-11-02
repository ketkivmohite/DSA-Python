#quick sort 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr #Base case 
    
    pivot = arr[-1] #choose the last element as pivot 
    left = [] #elements less than pivot 
    right = [] #elements greater than pivot

    for x in arr[:-1]: #all elements except pivot
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    #recursively sort left and right then combine 
    return quick_sort(left) + [pivot] + quick_sort(right)

#example usage 
numbers = [34, 7, 23, 32, 5, 62]
sorted_numbers = quick_sort(numbers)
print("Sorted numbers: ", sorted_numbers)