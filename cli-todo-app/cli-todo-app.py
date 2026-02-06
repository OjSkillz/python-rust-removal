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
    day = day.strip().capitalize()
    task = task.strip()

    tasks = load_tasks()
    tasks.setdefault(day, [])
    tasks[day].append(task)
    save_tasks(tasks)

def view_all_tasks():

    tasks = load_tasks()
    if tasks == {}:
        print("No tasks scheduled\n")
    else:
        print("Scheduled Tasks: \n")
        print(f"{"Day":>9} || Title")
        print(f'     {"*" * 14} ')
        for day, task in tasks.items():
            print(f"{day:>9} || {str(task).strip('[]')}")




def delete_task(day:str, task_id:int):
    tasks = load_tasks()
    tasks[day].pop(task_id - 1)
    save_tasks(tasks)


def view_tasks_by_day(day):
    task_by_day= load_tasks()[day.capitalize()]
    print(f"Tasks for {day}: \n")
    for index, task in enumerate(task_by_day, start=1):
        print(f"{index}. {task}")


def main_menu():
     try:
        print("Please choose from the options below: ")
        choice = int(input("1.Add Task\n"
                           "2.View Tasks\n"
                           "3.Delete Task\n"
                           "4.Exit\n"))

        match choice:

            case 1:
                day = input("Enter day: ").casefold()
                days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

                while day not in days:
                    print("Invalid day!")
                    day = input("Enter day: ").casefold()

                task = input("Enter task: ")
                task_format = r"\w"
                while not match(task_format, task):
                    print("Invalid task format!")
                    task = input("Enter task: ")
                add_task(day, task)
                print("Task has been added successfully")
                main_menu()
            case 2:
                view_all_tasks()
                main_menu()

            case 3:
                day = input("Enter day : ")
                view_tasks_by_day(day)
                task_index = int(input("Enter task number: "))
                delete_task(day, task_index)
                print("Task has been deleted successfully")
                main_menu()

            case 4:
                print("App closed")
     except ValueError:
        print("Invalid input!")
        main_menu()

print("Welcome to your ToDo App")
main_menu()






