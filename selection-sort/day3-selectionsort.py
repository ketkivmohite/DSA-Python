#classic selection sort with swaps 
def selection_sort(lst):
    size = len(lst) #get the size of the list

    #outer loop : iterate over the entire list
    for i in range(size):
        min_index = i #assume the current position is the minimum

        #inner loop : find the smallest element in the remaining unsorted part 
        for j in range(i + 1, size):
            if lst[j] < lst[min_index]: #compare elements
                min_index = j #update min_index if smaller element not found 

                #swap the smallest found element with the current position i  
                lst[i],lst[min_index] = lst[min_index], lst[i]

                #print the list after each swap to see the sorting progress
                print(f"Step {i + 1}: {lst}")

            return lst
        
#taking input from the user as space-separated numbers 
data_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

#calling the selection sort function 
sorted_list = selection_sort(data_list)

#printing the sorted list 
print("Sorted List: ", sorted_list)

#Stable Selection Sort
# The classic Selection Sort is not stable because swapping might reorder equal elements.
# A stable version shifts elements instead of swapping directly.
def stable_selection_sort(lst):
    size = len(lst) #get the size of the list 

    #traverse through all elements in the list one by one 
    for i in range(size):

        #assume the minimum element is at the current position i
        min_index = i 

        #look for a smaller element in the unsorted part (from i+1 to end)
        for j in range(i + 1, size):
            if lst[j] < lst[min_index]: #compare elements
                #update min_index if a smaller element is found 
                min_index = j 

        #store the smallest element found in key 
        key = lst[min_index]

        #shift all elements between i and min_index one position to the right
        #this makes space to insert the smallest element at position i 
        while min_index > i:
            lst[min_index] = lst[min_index - 1]
            min_index -= 1

        #insert the smallest element at its correct sorted position i 
        lst[i] = key 

        #print list after each iteration to show progress of sorting 
        print(f"Step {i + 1}: {lst}")

    #return the fully sorted list after all the passes 
    return lst 

# Take input as space-separated numbers from the user
data_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Call the stable_selection_sort function with user input
sorted_list = stable_selection_sort(data_list)

print("Sorted List:", sorted_list)


