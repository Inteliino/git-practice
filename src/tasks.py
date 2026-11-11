tasks = []

def add_task(title):
    tasks.append(title)
    print(f"Task added: {title}")

def list_tasks():
    print("\nTask list:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Create Python project")
    list_tasks()