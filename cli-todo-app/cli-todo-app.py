from re import match

task = {}
tasks = []

def add_task(day, title):
    task[day] = title
    tasks.append(task)

def view_tasks():
    print("Scheduled Tasks: \n")
    print(f"Day {"||":<5} Title")
    for task_ in tasks:
        for day, title in task_.items():
            print(f"{day:>20} {title:>10}")
    return None

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
            print(view_tasks())
            main_menu()

        case 3:
            response = input("Enter the title of the task you would like to delete")
            delete_task(response)
            print("Task has been deleted successfully")
            main_menu()

        case 4:
            print("App closed")

print("Welcome to your ToDo App\nPlease choose from the options below: ")
main_menu()






