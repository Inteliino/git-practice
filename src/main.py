
from database import run_migrations
from tasks import (
    add_task,
    list_tasks,
    edit_task,
    delete_task,
    complete_task,
    filter_tasks,
)
from statistics import show_statistics


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
    print("6. Filter tasks")
    print("7. Task statistics")
    print("8. Exit")


def main():
    run_migrations()

    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()

            if title:
                priority = input(
                    "Priority (Low/Medium/High) [Medium]: "
                ).strip().title()

                if not priority:
                    priority = "Medium"

                if priority in ("Low", "Medium", "High"):
                    add_task(title, priority)
                else:
                    print("Invalid priority.")
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
            status = input(
                "Status (Pending/Completed/All) [All]: "
            ).strip().title()

            priority = input(
                "Priority (Low/Medium/High/All) [All]: "
            ).strip().title()

            if status in ("", "All"):
                status = None
            elif status not in ("Pending", "Completed"):
                print("Invalid status.")
                continue

            if priority in ("", "All"):
                priority = None
            elif priority not in ("Low", "Medium", "High"):
                print("Invalid priority.")
                continue

            filter_tasks(status, priority)

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-8.")


if __name__ == "__main__":
    main()
