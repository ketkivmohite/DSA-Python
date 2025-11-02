#You are managing a line of people waiting to buy tickets. 
#Each person has a priority number representing how soon they want their ticket.

def quick_sort(people):
    if len(people) <= 1:
        return people #base case 
    
    pivot = people[-1] #choose the last person as pivot 
    left = [] #people with priority less than or equal to pivot 
    right = [] #people with priority greater than pivot 

    for person in people[:-1]: #all people except pivot 
        if person['priority'] <= pivot['priority']:
            left.append(person)
        else:
            right.append(person)

    #recursively sort left and right then combine 
    return quick_sort(left) + [pivot] + quick_sort(right)

#example usage
people = [
    {'name': 'Alice', 'priority': 3},
    {'name': 'Bob', 'priority': 1},
    {'name': 'Charlie', 'priority': 4},
    {'name': 'David', 'priority': 2}
]

sorted_people = quick_sort(people)
print("Sorted people by priority: ", sorted_people)