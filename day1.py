# list, access its elements one by one using a for loop, and access 
# elements using an index (including negative indexing).
fruits = ["apple", "banana", "cherry", "date", "strawberry"]
#simple iteration (element only)
for fruit in fruits:
    print(fruit)
#iteration with index using enumerate(index and element)
for index, fruit in enumerate(fruits):
    print(index, fruit)

#access elements by positive index 
fruits=["apple", "banana", "cherry", "date", "strawberry"]
print(fruits[0])
print(fruits[1])

i = 4
if 0 <= i < len(fruits):
    print(fruits[i])
else:
    print("Index out of range")

#access elements by negative index
print(fruits[-1])
print(fruits[-2])

#slicing a list 
numbers = [10, 20, 30, 40, 50, 60]

#slicing from index 2 to 5 
new_numbers = numbers[2:5]
print(new_numbers)

# in slicing the start index is inclusive but the end index is exclusive 
#list slicing example 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[0:4])
print(numbers[3:5])

#using negative indices in slicing
#items from the fourth item (3rd index) to the second -last item
print(numbers[3:-1])

#omit start and end index in slicing 
#if we omit the start index, the slicing starts from the first index

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[:4])

#if we omit the end index, the slicing goes upto the last item
print(numbers[3: ])

#if we omit both the start and the end indexes we get a new list that contains all the items from the original list (from the first item to the last item).
print(numbers[: ])

#repitition with list 
#creating a list with five elements all having the value 0 we can achieve this by usng the * operator
lst = [0] * 5
print(lst)

#list methods 
#append() add an element to the end of the list
#extend() add elements of sn iterable(list,tuple,etc.)to the end of the list
#insert() insert an element at the specified index
#pop() remove an element from the list and return it 
#reverse() reverse the elements of the list 

currencies = ["Dollar", "Euro","Pound"]
currencies.append("Yen")
print(currencies)

prime_numbers = [2,3,5,7]

#remove the element at index 2
removed_element = prime_numbers.pop(2)

print(f"Updated list: {prime_numbers}")
print(f"Removed Element: {removed_element}")

#create a list of words 
vowel = ["a","e","i","u"]

#insert "o" at index 3 (4th position)
vowel.insert(3, "o")

print(vowel)

prime_numbers = [2,3,5,7]
#reverse the order of the list elements
prime_numbers.reverse()
print(prime_numbers)

#enumerate the for loop in python doesnt automatically use indexes
languages = ["python","java","javascript"]
for language in languages :
    print(language)

#however if we need to access the index during each iteration of a for loop we can use enumerate() function along with the loop 

enumerate_languages = enumerate(languages)
#convert enumerate object to list
print(list(enumerate_languages))
#enumerate adds a counter to our list and returns it 

#enumerate in a for loop 
for index, language in enumerate(languages):
    print(index, language)

#if we need to work with indexes inside a for loop we can utilize the enumerate() function 


animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']

# perform list operations
animals.append("Raccoon")
animals.extend(wild_animals)
animals.pop(2)
animals.pop()
animals.insert(2,"Moose")
print(animals)



