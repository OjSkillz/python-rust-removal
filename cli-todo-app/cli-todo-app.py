import json
from json import JSONDecodeError
from re import match



def add_task(day, title):
    with open("tasks-directory.json", "a") as file:
        json.dump({day: title}, file, indent=4)

def view_tasks():
    try:
        with open("tasks-directory.json", "r") as file:
            tasks = json.load(file)
    except JSONDecodeError:
        print("No tasks scheduled\n")
    else:
        print("Scheduled Tasks: \n")
        print(f"{"Day":>9} || Title")
        print(f"{'-' * 30}")

        for day, title in tasks.items():
            print(f"{day:>9} || {title}")
            print(f"{'*' * 30}")

def delete_task(title):

    for task_ in tasks:
        for keys, values in task_.items():
            if values == title:
                tasks.remove(task_)

def main_menu():
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

print("Welcome to your ToDo App\nPlease choose from the options below: ")
main_menu()






