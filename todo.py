# todo.py — A Friendly CLI To-Do List App 

TODO_FILE = "todo.txt"


def load_tasks():
    """Loads tasks from the todo.txt file and returns them as a list."""
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Saves the current list of tasks to the todo.txt file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    """Displays all tasks with numbering."""
    if not tasks:
        print("\nYour to-do list is currently empty!\n")
        return

    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
    """Adds a new task entered by the user."""
    task = input("What task would you like to add? ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task added: '{task}'\n")
    else:
        print("You can't add an empty task!\n")


def remove_task(tasks):
    """Removes a task by its number as chosen by the user."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑 Task removed: '{removed}'\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def show_menu():
    """Displays the main menu options."""
    print("====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    print("===============================")


def main():
    """Main function to run the to-do list app."""
    print("Welcome to your personal To-Do List!")
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting... Stay productive!")
            break
        else:
            print("Please select a valid option (1-4).\n")


main()