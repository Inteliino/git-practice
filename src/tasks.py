
tasks = []

def add_task(title):
    tasks.append({"title": title, "completed": False})
    print(f"Task added: {title}")

def list_tasks():
    print("\nTask list:")
    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")

def delete_task(number):
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Task deleted: {removed['title']}")
    else:
        print("Invalid task number")

def edit_task(number, new_title):
    if 1 <= number <= len(tasks):
        old_title = tasks[number - 1]["title"]
        tasks[number - 1]["title"] = new_title
        print(f"Task updated: {old_title} -> {new_title}")
    else:
        print("Invalid task number")

def complete_task(number):
    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        print(f"Task completed: {tasks[number - 1]['title']}")
    else:
        print("Invalid task number")

if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Create Python project")
    add_task("Write automated tests")

    edit_task(2, "Build Python application")
    complete_task(1)
    list_tasks()
