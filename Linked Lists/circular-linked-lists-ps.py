class Node:
    def __init__(self, task):
        self.data = task
        self.next = None


#create nodes for tasks 
task1 = Node("Word Processor")
task2 = Node("Web Browser")
task3 = Node("Email Client")
task4 = Node("Music Player")


#link tasks in a circular manner 
task1.next = task2
task2.next = task3
task3.next = task4
task4.next = task1  # circular link


#simulate the round-robin scheduling
current_task = task1
turna = 0
max_turns = 2 * 4 #two full cycles for 4 tasks
while turna < max_turns:
    print(f"Running Task: {current_task.data}")
    current_task = current_task.next
    turna += 1
print("-- End of scheduler simulation --")
