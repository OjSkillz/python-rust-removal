from re import match


tasks = []

def add_task(day, title):
    task = {day: title}
    tasks.append(task)

def view_tasks():
    if len(tasks) == 0:
        print("No tasks scheduled")
    else:
        print("Scheduled Tasks: \n")
        print(f"{"Day":>9} || Title")
        print(f"{'-' * 30}")
        for task_ in tasks:
            for day, title in task_.items():
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






