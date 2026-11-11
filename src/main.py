
from database import run_migrations
from tasks import (
    add_task,
    list_tasks,
    edit_task,
    delete_task,
    complete_task,
)


def get_task_id():
    try:
        return int(input("Enter task ID: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return None


def show_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add task")
    print("2. List tasks")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Complete task")
    print("6. Exit")


def main():
    run_migrations()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            if title:
                add_task(title)
            else:
                print("Task title cannot be empty.")

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            task_id = get_task_id()
            if task_id is not None:
                new_title = input("Enter new title: ").strip()
                if new_title:
                    edit_task(task_id, new_title)
                else:
                    print("Task title cannot be empty.")

        elif choice == "4":
            task_id = get_task_id()
            if task_id is not None:
                delete_task(task_id)

        elif choice == "5":
            task_id = get_task_id()
            if task_id is not None:
                complete_task(task_id)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
