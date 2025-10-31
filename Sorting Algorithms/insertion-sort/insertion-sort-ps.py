#You have a collection of coins with different diameters scattered randomly on a table.
# You want to arrange the coins in ascending order of their diameter to see them from the 
# smallest to the largest side by side.
# Write a program to sort the list of coin diameters using Insertion Sort by inserting each
# coin into its correct position one by one.

def insertion_sort(coin_diameters):
    for i in range(1, len(coin_diameters)):
        current_diameter = coin_diameters[i]
        position = i
        while position > 0 and coin_diameters[position - 1] > current_diameter:
            coin_diameters[position] = coin_diameters[position - 1]
            position -= 1
        coin_diameters[position] = current_diameter
    return coin_diameters

coin_diameters = [25, 10, 5, 50, 20]
print("Before sorting:", coin_diameters)
print("After sorting:", insertion_sort(coin_diameters))