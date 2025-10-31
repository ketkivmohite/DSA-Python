#You have two photo albums, each sorted by date. You want to combine all photos into one big album sorted 
# by date from oldest to newest without changing the order within each album.

# Write a program that uses Merge Sort to combine these
# two sorted albums into one sorted album by recursively splitting and merging the photo lists.

def merge_sort(arr):
    if len(arr) <= 1: #Base case: an array of zero or one element is sorted
        return arr
    mid = len(arr) // 2 #find the midpoint of the array 
    left_half = merge_sort(arr[:mid]) #recursively sort the left hand side 
    right_half = merge_sort(arr[mid:]) #recursively sort the right hand side 

    return merge(left_half, right_half) #merge the sorted hands to get the final sorted array

def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any remaining elements from either half
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Example photo albums sorted by date (represented as integers for simplicity)
album1 = [1, 4, 7, 10]  # Album 1
album2 = [2, 3, 5, 8, 9]  # Album 2 

all_photos = album1 + album2
sorted_photos = merge_sort(all_photos)
print("Sorted photo album by date:", sorted_photos)
