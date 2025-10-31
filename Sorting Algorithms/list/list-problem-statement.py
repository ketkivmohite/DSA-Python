task_list = []

def add_task(task):
    task_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task():
    if not task_list:
        print("Your to-do list is empty. Nothing to remove.")
        return
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(task_list):
            removed = task_list.pop(task_num - 1)
            print(f"Task '{removed}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    if task_list:
        print("Your To-Do List:")
        for idx, task in enumerate(task_list, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")

def main():
    while True:
        print("\nChoose an action:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 4.")

# Run the program
if __name__ == "__main__":
    main()

