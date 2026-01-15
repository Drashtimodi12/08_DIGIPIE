import time

print("\n=========WELCOME=========")

remaning_tasks = []
completed_tasks = []

# -------------------------------add-----------------------------------
def add_task():
    try:
        print("===ADD TASK===")
        add = input("Enter your today's task: ").title()

        remaning_tasks.append(add)
        print("Task added successfully!")
    except Exception as e:
        print(e)

# -------------------------------view-----------------------------------
def view_list():
    print("===VIEW REMANING AND COMPLETED TASK===")

    print("\n*Remaning Tasks is:")
    if len(remaning_tasks) == 0:
        print(" List is empty!")
    else:
        for index, task in enumerate(remaning_tasks):
            print(f"    {index+1}. {task}")

    print("\n*Completed Tasks is:")
    if len(completed_tasks) == 0:
        print(" List is empty!")
    else:
        for id, ctask in enumerate(completed_tasks):
            print(f"    {id+1}. {ctask}")


# -------------------------------edit-----------------------------------
def edit_task():
    while True: 
        print("===EDIT TASK===")
        print("1. Remaning List change.")
        print("2. Completed list change.")
        print("3. Exit \n")

        ch = int(input("Enter choice to edit task: "))
        if ch == 1:
            if len(remaning_tasks) == 0:
                print(" List is empty!")
            else:
                
                for index, task in enumerate(remaning_tasks):
                    print(f"    {index+1}. {task}")
            
                task_id = int(input("Enter task index to edit: "))-1

                if 0 <= task_id < len(remaning_tasks):
                    new_task = input("Enter new task: ").title()
                    remaning_tasks[task_id] = new_task
                    print("Reamning Task edited successfully!")
                else:
                    print("Invalid task id.")
                    return

        elif ch == 2:     
            if len(completed_tasks) == 0:
                print(" List is empty!")
            else:
                for index, task in enumerate(completed_tasks):
                    print(f"    {index+1}. {task}")
            
                com_task_id = int(input("Enter task index to edit: "))-1

                if 0 <= com_task_id < len(completed_tasks):
                    new_task = input("Enter new task: ").title()
                    completed_tasks[com_task_id] = new_task
                    print("Completed Task edited successfully!")
                else:
                    print("Invalid task id.")
            
        else:
            print("Invalid choice!")
            return


# -------------------------------Delete-----------------------------------
def delete_task():
    while True: 
        print("===DELETE TASK===")
        print("1. Remaning List change.")
        print("2. Completed list change.")
        print("3. Exit \n")

        ch = int(input("Enter choice to delete task: "))
        if ch == 1:
            if len(remaning_tasks)== 0:
                print("Task list is empty!")
            else:
           
                view_list()

                task_id = int(input("Enter task index to delete: "))-1

                if 0 <= task_id < len(remaning_tasks):
                    remaning_tasks.pop(task_id)
                    print("Task deleted successfully!")
                else: 
                    print("Invalid task id.")

        elif ch == 2:     
            if len(completed_tasks)== 0:
                print("Task list is empty!")
            else:
                view_list()

                task_id = int(input("Enter task index to delete: "))-1

                if 0 <= task_id < len(completed_tasks):
                    completed_tasks.pop(task_id)
                    print("Task deleted successfully!")
                else: 
                    print("Invalid task id.")
        else:
            print("Invalid choice!")
            return

# -------------------------------transfer task in completed list-----------------------------------
def remaning_task_to_completed_task():
    while True: 
        print("===Transfer TASK===")
        print("1. Remaning List -> Completed list.")
        print("2. Completed list -> Remaning List.")
        print("3. Exit \n")

        ch = int(input("Enter choice to delete task: "))
        if ch == 1:
            if len(remaning_tasks) == 0:
                print("Task list is empty!")
            else:
                view_list()
                
                complete_id = int(input("Enter remaning task index to transfer in completed task: "))-1

                if 0 <= complete_id < len(remaning_tasks):
                    completed_tasks.append(remaning_tasks.pop(complete_id))
                    print("Thank you for Complete task.")
                else:
                    print("Invalid task id.")

        elif ch == 2:     
            if len(completed_tasks) == 0:
                print("Task list is empty!")
            else:
                view_list()
                
                remaning_id = int(input("Enter completed task index to trasfer in remaning task: "))-1

                if 0 <= remaning_id < len(completed_tasks):
                    remaning_tasks.append(completed_tasks.pop(remaning_id))
                    print("Thank you for Complete task.")
                else:
                    print("Invalid task id.")
        else:
            print("Invalid choice!")
            return












while True:

    print("\n============Task Meanu============")
    print("1. Add Task.")
    print("2. View all Taask")
    print("3. Edit Task.")
    print("4. Delete Task.")
    print("5. Completed Task")
    print("6. Exit.")

    choice = int(input("Select option to do task: "))

    
    if choice == 1:
        add_task()
    elif choice == 2:
        view_list()
    elif choice == 3:
        edit_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        remaning_task_to_completed_task()
    elif choice == 6:
        print("Exiting the application!")
        break
    else:
        print("Invalid choice. Please Enter a valid option.")



    