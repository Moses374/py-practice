class TasksInputError(Exception):
    """Raise an error if one is found"""
    pass
tasks=[]
def add_task():

    task=input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        """Adding a task"""
        save_tasks_to_file()
    else:
        print("Enter a Task.\n")

def save_tasks_to_file():

    try:
        with open("tasks.txt","w")as file:
            for task in tasks:
                file.write(f"{task}")
        print("Tasks Saved")
    except Exception as e:
        print(f"An error occurred while saving a task {e}")

def view_tasks():
    if tasks:
        print("\n---To-Do List---")
        for i,task in enumerate(tasks,start=1):
            print(f"{i}.{task}")
    else:
        print("Your to-do list is empty.")
def remove_tasks():
    if not tasks:

        print("Your task list is empty")
        return


    view_tasks()
    try:
        task_num=int(input("\nEnter the task number to remove: "))
        if 1<=task_num<=len(tasks):
            removed_task=tasks.pop(task_num-1)
            print(f"task {task_num} has been removed")
        else:
            print("Enter a valid task number")
    except ValueError:
        print("Enter a valid number")

def load_tasks_from_file():
    try:
        with open("tasks.txt","r")as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        print("the file has not been found")

def clear_all_tasks():
    if tasks:
        tasks.clear()
        print("All task removed")
    else:
        print("No tasks to remove")



def menu():

        while True:
            print("\n--- To-Do List Menu ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Clear All Tasks")
            print("5. Exit")
            try:
                choice=int(input("Enter choice(1-5):"))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if (choice==1):
                add_task()
            elif  (choice==2):
                view_tasks()
            elif (choice==3):
                remove_tasks()
            elif (choice==4):
                clear_all_tasks()
            elif (choice==5):
                print("Goodbye!!")
                break
            else:
                print("Enter valid choice:")

if __name__=="__main__":
    load_tasks_from_file()
    menu()