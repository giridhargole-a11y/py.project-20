tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == "3":
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = input("Enter updated task: ")
            print("Task updated.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List.")
        break

    else:
        print("Invalid choice. Try again.")
