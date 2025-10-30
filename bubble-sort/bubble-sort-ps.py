#Imagine you have a small list of your daily temperatures for a week
#Your goal is to sort this list in ascending order to easily see the temperature trend over the week.​
#Write a program to do this using Bubble Sort, which compares neighboring temperatures and swaps 
#them if they are in the wrong order, repeating until the entire list is sorted.

def bubble_sort(temperatures):
    n = len(temperatures)
    #traverse through all elements in the list 
    for i in range(n):
        #last i elements are already sorted 
        for j in range(0, n-i-1):
            #travers the list from 0 to n-i-1
            #swap if the element found is greater than the next element 
            if temperatures[j] > temperatures[j+1]:
                temperatures[j], temperatures[j+1] = temperatures[j+1], temperatures[j]
    return temperatures

temperatures = [72, 68, 75, 70, 69, 74, 73]
print("Original temperatures: ",temperatures)
print("Sorted temperatures: ", bubble_sort(temperatures))