#Imagine a teacher needs to sort the exam scores of 200 students,
#where the scores range from 0 to 100, quickly and efficiently without comparing each score — 
# Counting Sort can be used to count
#how many students scored each mark and then build the sorted list of scores by frequency.

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
marks = [88, 95, 70, 100, 65, 85, 90, 75, 80, 95, 100, 60, 70]

#call the counting_sort function with example data
sorted_marks = counting_sort(marks)
print("Sorted exam scores: ", sorted_marks)