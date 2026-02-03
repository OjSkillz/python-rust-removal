task = {}
tasks = []

def add_task(day, title):
    task[day] = title
    tasks.append(task)

def view_tasks():
    for task_ in tasks:
        return task_
    return None

def delete_task(title):
    for task_ in tasks:
        for keys, values in task_.items():
            if values == title:
                tasks.remove(task_)

