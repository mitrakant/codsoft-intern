# todo_list.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def update_task(task_id, new_task):
    try:
        tasks[task_id - 1] = new_task
        print(f"Task {task_id} updated to '{new_task}'!")
    except IndexError:
        print("Invalid task ID!")

def delete_task(task_id):
    try:
        del tasks[task_id - 1]
        print(f"Task {task_id} deleted!")
    except IndexError:
        print("Invalid task ID!")

def list_tasks():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    while True:
        user_input = input("Enter a command (add, update, delete, list, quit): ")
        if user_input.startswith("add"):
            _, task = user_input.split(" ", 1)
            add_task(task)
        elif user_input.startswith("update"):
            _, task_id, new_task = user_input.split(" ", 2)
            update_task(int(task_id), new_task)
        elif user_input.startswith("delete"):
            _, task_id = user_input.split(" ", 1)
            delete_task(int(task_id))
        elif user_input == "list":
            list_tasks()
        elif user_input == "quit":
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()