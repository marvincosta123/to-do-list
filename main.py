import os,random

tasks = []

print(tasks)
def clean_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def create_tasks():
    print("What do you want to do?")
    activity = input('Write here?\n').lower()
    tasks.append(activity)

def remove_tasks(task):
    print("May be you don't know what task you wanna remove, I'll show you all the options")
    for i in tasks:
        position = tasks.index(i)
        print(f"{position + 1} is {i}")
        print("Type the number of the task you want to remove")
    try:
        number = int(input())
        numberTaskToBeRemoved = number - 1
        taskToBeRemovedPosition = tasks[numberTaskToBeRemoved]
        print(f'Are you right you want to remove {tasks[numberTaskToBeRemoved]} Y/N')
        choice = input('Y/N\n').lower()
        if choice == "y":
            tasks.remove(taskToBeRemovedPosition)
        else:
            print("Not action take, be easy")
        print(tasks)

    except ValueError:
        print("Type a correct value please")

create_tasks()
result = create_tasks
remove_tasks(result)
# def show_tasks():

# def change_task():

