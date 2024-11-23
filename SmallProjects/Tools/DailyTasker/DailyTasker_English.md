## Simple Task Manager Using Python and JSON File Storage
The provided code is a simple task management program that uses a JSON file to store and retrieve task information. It includes features such as adding, viewing, marking tasks as completed, and deleting tasks. Here's a detailed explanation of the code:

1. Importing Modules:
   - json: To handle reading and writing data in JSON format.
   - datetime: Imported but not used. It can be helpful for validating or comparing dates in future enhancements.
2. TASKS_FILE Variable:
   - Defines the name of the file where tasks will be stored. This file will be created in the program's directory.
3. load_tasks Function:
   - Attempts to open the task file and load tasks from it.
   - If the file doesn’t exist, it returns an empty list.
4. save_tasks Function:
   - Saves the list of tasks into the JSON file.
   - Data is stored with proper indentation for better readability.
5. add_task Function:
   - Prompts the user to enter the task name and due date.
   - Creates a dictionary containing task details (name, due date, and completion status) and adds it to the task list.
   - Updates the JSON file and displays a success message.
6. view_tasks Function:
   - Displays all the tasks in the list.
   - Each task is shown with its number, name, due date, and completion status (✓ for completed, ✗ for not completed).
   - If there are no tasks, an appropriate message is displayed.
7. complete_task Function:
   - First, displays all tasks for the user.
   - Prompts the user to input the task number to mark it as completed.
   - Updates the completion status of the selected task to True and saves the changes to the file.
8. delete_task Function:
   - Similar to complete_task, it displays the tasks first.
   - Prompts the user for the task number to delete.
   - Removes the specified task from the list and updates the JSON file.
9. main Function:
    - The main loop of the program displays the task management menu.
    - Options include adding, viewing, marking, deleting tasks, and exiting.
    - Depending on the user’s choice, the corresponding function is called
10. How It Works:
    - The program starts by executing the main function.
    - The user interacts with the program by selecting numbered options to manage tasks.
    - Choosing the exit option ends the program.
   
## Key Features:
- Tasks are saved persistently in a JSON file.
- Tasks can be added with a due date and completion status.
- The user can view, complete, or delete tasks.

## Limitations and Possible Enhancements:
- The program doesn’t validate due dates or sort tasks by them.
- Features like filtering tasks by completion status or due date can be added.
- Input handling could be improved to prevent errors (e.g., invalid task numbers or empty inputs).

This simple task manager is easy to use and serves as a foundation for more complex task management applications.

## Python Code
```python
import json
import datetime

TASKS_FILE = "tasks.json"

# Load tasks from a file if it exists
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)  # Load the tasks from the file
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

# Save tasks to a file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)  # Save tasks to the JSON file with proper indentation

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task: ")  # Prompt the user to enter the task name
    due_date = input("Enter due date (YYYY-MM-DD): ")  # Prompt the user to enter the due date
    task = {
        'name': task_name,  # Task name
        'due_date': due_date,  # Due date
        'completed': False  # Completion status (default: not completed)
    }
    tasks.append(task)  # Add the new task to the list
    save_tasks(tasks)  # Save the updated tasks list to the file
    print(f"Task '{task_name}' added successfully!")  # Success message

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")  # If no tasks exist
        return
    
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"  # Display completion status of each task
        print(f"{idx + 1}. {task['name']} | Due: {task['due_date']} | Completed: {status}")
    print("\n")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)  # Display all tasks
    task_number = int(input("Enter the task number to mark as completed: "))  # Prompt for task number
    
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True  # Mark the selected task as completed
        save_tasks(tasks)  # Save the updated tasks list
        print(f"Task '{tasks[task_number - 1]['name']}' marked as completed!")  # Success message
    else:
        print("Invalid task number.")  # If the task number is invalid

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)  # Display all tasks
    task_number = int(input("Enter the task number to delete: "))  # Prompt for task number to delete

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)  # Remove the selected task from the list
        save_tasks(tasks)  # Save the updated tasks list
        print(f"Task '{removed_task['name']}' deleted successfully!")  # Success message
    else:
        print("Invalid task number.")  # If the task number is invalid

# Main program loop
def main():
    tasks = load_tasks()  # Load tasks from the file
    while True:
        print("\nTask Manager")  # Display task manager menu
        print("1. Add a Task")  # Option to add a new task
        print("2. View Tasks")  # Option to view existing tasks
        print("3. Mark Task as Completed")  # Option to mark a task as completed
        print("4. Delete Task")  # Option to delete a task
        print("5. Exit")  # Option to exit the program

        choice = input("Choose an option: ")  # Prompt the user to choose an option
        
        if choice == "1":
            add_task(tasks)  # Add a new task
        elif choice == "2":
            view_tasks(tasks)  # View all tasks
        elif choice == "3":
            complete_task(tasks)  # Mark a task as completed
        elif choice == "4":
            delete_task(tasks)  # Delete a task
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")  # Exit message
            break
        else:
            print("Invalid option. Please try again.")  # If the option is invalid

if __name__ == "__main__":
    main()  # Run the main function

```
