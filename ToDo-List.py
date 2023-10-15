# Makes an empty list to store the to-do items
todo_list = []

# This Function is used to add a task in the to-do list
def add_task(task):
    todo_list.append(task)
    print(f"Added task: {task}")

# This Function is used to remove a task from the to-do list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Removed task: {task}")
    else:
        print(f"Task not found: {task}")

# This Function is used to display the current to-do list
def display_tasks():
    print("To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

# Main loop for the to-do list program
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Display tasks")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
