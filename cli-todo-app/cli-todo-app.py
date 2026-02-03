task = {}
tasks = []

def add_task(day, title):
    task[day] = title
    tasks.append(task)

def view_tasks():
    for task_ in tasks:
        return task_
    return None

