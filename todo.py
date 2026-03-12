"""This file contains the todo list functionality."""

# list to store the tasks
todo_list = []


def add_task():
    """Add a task to the todo list."""
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added  successfully to the list.")


def view_tasks():
    """View the tasks in the todo list."""
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Todo List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")


def delete_task():
    """Delete a task from the todo list."""
    if not todo_list:
        print("No tasks to delete.")
        return view_tasks()
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(todo_list):
        deleted_task = todo_list.pop(task_num - 1)
        return print(f"Task '{deleted_task}' deleted successfully.")
    return print("Invalid task number.")


# main loop to display the menu and handle user input
print("""Todo System Menu :
    1. Add Task
    2. View Tasks
    3. Delete Task
    4. Exit""")

while True:
    option = input("Choose an option (1-4): ")
    # use match-case to handle the user's choice
    match option:
        case "1":
            add_task()
        case "2":
            view_tasks()
        case "3":
            delete_task()
        case "4":
            print("Exiting Todo System. Goodbye!")
            break
        case _:
            print("Invalid option. Please choose a number between 1 and 4.")
