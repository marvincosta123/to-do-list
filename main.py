import os

tasks = []

print(tasks)

def show_tasks():
     for i,value in enumerate(tasks, start=1):
          print(f"Task number {i}: {value}")

def clean_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_options():
    print("""
           1 - Create Tasks
           2 - Remove Tasks
           3 - Show All Tasks
           4 - Change a Task
           5 - Exit App
           """)
    print("What option do you want to do?")

def create_tasks():
    print("What do you want to do?")
    activity = input('Write here?\n').lower()
    tasks.append(activity)

def remove_tasks():
    print("Maybe you don't know what task you wanna remove, I'll show you all the options")
    for i,value in enumerate(tasks,start =1):
        print(f"{i} is {value}")
        print("Type the number of the task you want to remove")

    try:
        number = int(input()) - 1
    except ValueError:
            print("Type a correct value please")

    if 0 <= number < len(tasks):
            taskToBeRemovedPosition = tasks[number]
            print(f'Are you right you want to remove {tasks[number]} Y/N')
            choice = input('Y/N\n').lower()
            if choice == "y":
                tasks.remove(taskToBeRemovedPosition)
            else:
                print("Not action take, be easy")
            print(tasks)
    else:
        print("Out of range")

while True:
    show_options()
    try:
        choice = int(input())
    except ValueError:
        print("Type a valid value please")
    match choice:
        case 1:
            create_tasks()
            clean_screen()
        case 2:
              remove_tasks()
              clean_screen
        case 3:
              show_tasks()
        case 4:
              print("In procss")
        case 5:
              print("Thank You, break")
              break

# def change_task():

