import json
from json import JSONDecodeError
from re import match

def load_tasks(path = "tasks-directory.json"):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except JSONDecodeError:
        return {}

def save_tasks(tasks, path = "tasks-directory.json"):
    with open(path, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(day, task):
    day = day.strip()
    task = task.strip()

    tasks = load_tasks()
    tasks.setdefault(day, [])
    tasks[day].append(task)
    save_tasks(tasks)

def view_tasks():

    tasks = load_tasks()
    if tasks == {}:
        print("No tasks scheduled\n")
    else:
        max_tasks_len = max(len(character) for character in [task for task in tasks.values()])
        print("Scheduled Tasks: \n")
        print(f"{"Day":>9} || Title")
        print(f"{'-' * max_tasks_len}")

        for day, task in tasks.items():
            print(f"{day:>9} || {task}")
            print(f"{'*' * max_tasks_len}")

def delete_task(title):
    tasks = load_tasks()
    with open("tasks-directory.json", "w") as file:
        json.dump(tasks, file, indent=4)

def main_menu():
  #   try:
        print("Please choose from the options below: ")
        choice = int(input("1.Add Task\n"
                           "2.View Tasks\n"
                           "3.Delete Task\n"
                           "4.Exit\n"))

        match choice:

            case 1:
                day = input("Enter day: ")
                title = input("Enter title: ")
                add_task(day, title)
                print("Task has been added successfully")
                main_menu()
            case 2:
                view_tasks()
                main_menu()

            case 3:
                response = input("Enter the title of the task you would like to delete: ")
                delete_task(response)
                print("Task has been deleted successfully")
                main_menu()

            case 4:
                print("App closed")
#    except ValueError:
 #       print("Invalid input!")
  #      main_menu()

print("Welcome to your ToDo App")
main_menu()






