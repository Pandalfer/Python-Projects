import time

print("Welcome to the To Do List App!")
print("You can 'add', 'finish' or 'clear' tasks")
print("Type 'quit' to exit!")

task_list_file = "tasks.txt"
def get_tasks(file):
    with open(file, mode="r") as task_file:
        for i in task_file:
            if i == "\n":
                continue
            else:
                time.sleep(0.5)
                print(f"    => {i.strip()}")

def show_tasks():
    print("")
    print("Your current To Do Activities are: ")
    get_tasks(task_list_file)
    time.sleep(0.5)
    print("")

show_tasks()

def add_task(file, newTask):
    with open(file, mode="r") as task_file:
        for line in task_file:
            if newTask in line:
                print("Error: Task already exists")
                return

    with open(file, mode="a") as task_file:
        task_file.write('\n' + newTask)


def finish_task(file, removeTask):
    removeTask = removeTask.lower().replace(" ", "")
    with open(file, mode="r") as task_file:
        tasks = task_file.readlines()
        contains_task = False
        for line in range(len(tasks)):
            if removeTask in tasks[line].lower().replace(" ", ""):
                contains_task = True
        if(not(contains_task)):
            print("Error, task does not exist")
            return
    with open(file, mode="w") as task_file:
        for line in tasks:
            if removeTask != line.lower().replace(" ", "").strip():
                task_file.write(line)


def clear_tasks(file):
    with open(file, mode="w") as task_file:
        task_file.close()



while True:
    action = input("Would you like to add or finish a task: ")
    if action == "quit":
        quit()
    elif action.lower() == "clear":
        clear_tasks(task_list_file)
        print("Your tasks have been cleared")
    elif action.lower() == "add":
        task_to_add = input("What task would you like to add: ")
        add_task(task_list_file, task_to_add)
        show_tasks()
    elif action.lower() == "finish":
        task_to_finish = input("What task would you like to finish: ")
        finish_task(task_list_file, task_to_finish)
        show_tasks()
    else:
        print("Invalid input, please either type 'add', 'finish', 'clear' or 'quit'")

