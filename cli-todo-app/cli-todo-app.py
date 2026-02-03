from re import match

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


print("Welcome to your ToDo App\nPlease choose from the options below: ")
choice = int(input("1. Add Task"
                   "2. View Tasks"
                   "3. Delete Task"))

match choice:
    case 1:
        day = input("Enter day: ")
        title = input("Enter title")
        add_task(day, title)
        print("Task has been added successfully")

    case 2:
        view_tasks()

    case 3:
        response = input("Enter the title of the task you would like to delete")
        delete_task(response)
        print("Task has been deleted successfully")



