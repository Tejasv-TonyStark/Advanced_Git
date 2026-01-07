tasks = []

def add_task(task):
    if task.strip() == "":
        print("Task cannot be empty")
        return
    tasks.append(task)

add_task("Sample task")
print(tasks)
