#counting sort algorithm implementation in python
#counting means tallying the frequency of each number in the input list

def counting_sort(arr):

    #handle empty list input case 
    if not arr:
        return arr
    
    #find the maximum value in the list to know the range for counting 
    max_val = max(arr)

    #Create a list (count array) of zeros with length mx_val + 1 
    #Each index represents a number in the range 0 to max_val
    count = [0] * (max_val + 1)

    #count how many times each number appears in the original list
    for num in arr:
        count[num] += 1 #increment count at the index of the number  

    #prepare an empty list to store the sorted result 
    sorted_arr = []

    #loop over all possible values from 0 to max_val
    for num, freq in enumerate(count):

        #add the number 'num' to the sorted list freq times
        #if frq is 0, it addds nothing , if freq > 0 , adds that many copies
        sorted_arr.extend([num] * freq)

    #return the sorted list
    return sorted_arr

#example usage 
numbers = [4, 2, 2, 8, 3, 3, 1]

#call the counting_sort function with example data
print("Sorted numbers: ", counting_sort(numbers))