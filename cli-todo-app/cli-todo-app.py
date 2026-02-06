import json
from json import JSONDecodeError
import re


def load_tasks(path = "tasks-directory.json"):
    try:
        with open(path, "r") as file:
            return json.load(file)
    except (JSONDecodeError, FileNotFoundError):
        return {}

def save_tasks(tasks, path = "tasks-directory.json"):
    with open(path, "w") as file:
        json.dump(tasks, file, indent=4)
    return

def add_task(day, task):
    day = day.strip().capitalize()
    task = task.strip()

    tasks = load_tasks()
    tasks.setdefault(day, [])
    tasks[day].append(task)
    save_tasks(tasks)
    return

def view_all_tasks():

    tasks = load_tasks()
    if tasks == {}:
        print("No tasks scheduled\n")
        return
    else:
        print("Scheduled Tasks: \n")
        print(f"{"Day":>9} || Title")
        print(f'     {"*" * 14} ')
        for day, task in tasks.items():
            print(f"{day:>9} || {str(task).strip('[]')}")
        return



def delete_task(day:str, task_id:int):
    tasks = load_tasks()
    day = day.strip().capitalize()
    if task_id < 1 or task_id > len(tasks[day]):
        print("Invalid task number")
        return
    tasks[day].pop(task_id - 1)
    save_tasks(tasks)
    return

def view_tasks_by_day(day):
    tasks = load_tasks()
    day = day.strip().capitalize()
    if day not in tasks:
        print("No tasks scheduled for this day")
        return
    else:
        task_by_day = tasks[day]
        print(f"Tasks for {day}: \n")
        for index, task in enumerate(task_by_day, start=1):
            print(f"{index}. {task}")
        return


def main_menu():
        while True:
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
                    task_format = r"[^aA-zZ]"
                    while not re.match(task_format, task):
                        print("Invalid task format!")
                        task = input("Enter task: ")
                    add_task(day, task)
                    print("Task has been added successfully")

                case 2:
                    view_all_tasks()


                case 3:
                    day = input("Enter day : ").casefold()
                    if not view_tasks_by_day(day):
                        task_index = int(input("Enter task number: "))
                        if not delete_task(day, task_index):
                            print("Task has been deleted successfully")


                case 4:
                    print("App closed")

         except ValueError:
            print("Invalid input!")


print("Welcome to your ToDo App")
main_menu()






