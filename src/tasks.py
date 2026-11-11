tasks = []

def add_task(title):
    tasks.append(title)
    print(f"Task added: {title}")

if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Create Python project")