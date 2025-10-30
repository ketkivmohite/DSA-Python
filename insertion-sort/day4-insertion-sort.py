def insertion_sort(arr):
    #traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        current = arr[i] #current element to be positioned 
        position = i 

        while  position > 0 and arr[position - 1] > current:
            arr[position] = arr[position - 1] #shift larger element to the right 
            position -= 1

            arr[position] = current #place current element at its correct position 

    return arr

numbers = [5,3,8,4,2]
print("Before sorting:", numbers)
print("After sorting:", insertion_sort(numbers))