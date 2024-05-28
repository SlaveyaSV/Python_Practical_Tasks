def main_menu():
    print("===== To-Do List Menu =====")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Mark a task as not completed")
    print("5. Delete task")
    print("6. Quit the program)")
    print()
    print("Enter your choice (1-6): ")


def add_task(list_to_do):
    print("Enter a task description: ")
    new_task = input()
    print()
    task_in_list = False
    for task in range(len(list_to_do)):
        if new_task == list_to_do[task][0]:
            task_in_list = True
    if not task_in_list:
        list_to_do.append([new_task, " "])
        print(f'Task "{new_task}" added successfully!')
        print()
    else:
        print(f'Task "{new_task}" already exist!')
        print()


def view_tasks(list_to_do):
    print("===== Tasks =====")
    for task in range(len(list_to_do)):
        print(f"{task+1}. [{list_to_do[task][1]}] {list_to_do[task][0]}")
    print()


def mark_completed(list_to_do):
    print("Enter the index of the task to mark as completed: ")
    task_index = int(input())
    print()
    if 0 < task_index <= len(list_to_do):
        list_to_do[task_index-1][1] = "X"
        print("Task marked as completed!")
        print()
    else:
        print("Invalid task index!")
        print(f"Task index must be between 1 and {len(list_to_do)}")
        print()


def mark_not_completed(list_to_do):
    print("Enter the index of the task to mark as not completed: ")
    task_index = int(input())
    print()
    if 0 < task_index <= len(list_to_do):
        list_to_do[task_index-1][1] = " "
        print("Task marked as not completed!")
        print()
    else:
        print("Invalid task index!")
        print(f"Task index must be between 1 and {len(list_to_do)}")
        print()


def delete_task(list_to_do):
    print("Enter the index of the task to delete: ")
    task_index = int(input())
    print()
    if 0 < task_index <= len(list_to_do):
        del list_to_do[task_index-1]
        print("Task deleted successfully.")
        print()
    else:
        print("Invalid task index!")
        print(f"Task index must be between 1 and {len(list_to_do)}")
        print()


to_do_list = []

while True:
    main_menu()
    command = int(input())
    print()

    if command == 6:
        print("Exiting the program. Goodbye!")
        break
    elif command == 1:
        add_task(to_do_list)
    elif command == 2:
        view_tasks(to_do_list)
    elif command == 3:
        view_tasks(to_do_list)
        mark_completed(to_do_list)
    elif command == 4:
        view_tasks(to_do_list)
        mark_not_completed(to_do_list)
    elif command == 5:
        view_tasks(to_do_list)
        delete_task(to_do_list)
    else:
        print("Invalid choice!")
        print("Choose a number between 1 and 4")
        print()
