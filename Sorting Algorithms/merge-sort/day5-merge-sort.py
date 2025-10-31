def merge_sort(arr):
    if len(arr) <= 1: #Base case: an array of zero or one element is sorted
        return arr
    mid = len(arr) // 2 #find the midpoint of the array 
    left_half = merge_sort(arr[:mid]) #recursively sort the left hand side 
    right_half = merge_sort(arr[mid:]) #recursively sort the right hand side 

    return merge(left_half, right_half) #merge the sorted hands to get the final sorted array

def merge(left,right):
    result = []
    i = j = 0 

    #merge in sorted order 
    while i <len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            #append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print("Sorted list:", sorted_list)