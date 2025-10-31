#Imagine you have a list of student test scores in random order. You want to arrange these
#  scores in ascending order to easily see the progression from lowest to highest.
# Write a program to sort the list using Selection Sort.
# The algorithm should repeatedly select the smallest unsorted element and swap it with the element at the beginning
#  of the unsorted portion, continuing until the entire list is sorted.
def selection_sort(marks):
    n = len(marks)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted portion
        min_index = i
        # Iterate through the unsorted elements
        for j in range(i+1, n):
            # Update min_index if current element is less
            if marks[j] < marks[min_index]:
                min_index = j
        # Swap minimum with the first element of unsorted part
        marks[i], marks[min_index] = marks[min_index], marks[i]
    return marks

marks = [88, 72, 95, 63, 85, 78, 91]
print("Original marks:", marks)
print("Sorted marks: ", selection_sort(marks))
