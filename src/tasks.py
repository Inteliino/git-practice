
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

if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Create Python project")
    add_task("Write automated tests")

    list_tasks()
    delete_task(2)
    list_tasks()
