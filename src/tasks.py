
tasks = []

def add_task(title):
    tasks.append(title)
    print(f"Task added: {title}")

def list_tasks():
    print("\nTask list:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

def delete_task(number):
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Task deleted: {removed}")
    else:
        print("Invalid task number")

def edit_task(number, new_title):
    if 1 <= number <= len(tasks):
        old_title = tasks[number - 1]
        tasks[number - 1] = new_title
        print(f"Task updated: {old_title} -> {new_title}")
    else:
        print("Invalid task number")

if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Create Python project")
    add_task("Write automated tests")

    list_tasks()

    edit_task(2, "Build Python application")
    list_tasks()

    delete_task(1)
    list_tasks()
