tasks = ["Task 1", "Task 2"]

def view_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

view_tasks()
