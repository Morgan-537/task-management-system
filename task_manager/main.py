"""
main.py - Task Management System Main Program
"""

from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress, get_all_tasks, delete_task


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("TASK MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. View pending tasks")
    print("4. Mark task as complete")
    print("5. View progress")
    print("6. Delete a task")
    print("7. Exit")
    print("="*50)


def display_tasks(task_list):
    """Display a list of tasks in a formatted way."""
    if not task_list:
        print("\nNo tasks to display.")
        return
    
    print("\n" + "-"*70)
    for task in task_list:
        status = "✓ COMPLETE" if task['completed'] else "✗ PENDING"
        print(f"ID: {task['id']} | {status}")
        print(f"  Title: {task['title']}")
        print(f"  Description: {task['description']}")
        print(f"  Due Date: {task['due_date']}")
        print("-"*70)


def add_task_menu():
    """Handle adding a new task from user input."""
    print("\n--- ADD NEW TASK ---")
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    
    if add_task(title, description, due_date):
        print("✓ Task added successfully!")
    else:
        print("✗ Failed to add task. Please check your input:")
        print("  - Title: 1-100 characters")
        print("  - Description: 1-500 characters")
        print("  - Due Date: Format YYYY-MM-DD")


def view_all_tasks_menu():
    """Display all tasks."""
    print("\n--- ALL TASKS ---")
    all_tasks = get_all_tasks()
    display_tasks(all_tasks)


def view_pending_tasks_menu():
    """Display only pending tasks."""
    print("\n--- PENDING TASKS ---")
    pending = view_pending_tasks()
    display_tasks(pending)


def mark_complete_menu():
    """Handle marking a task as complete."""
    print("\n--- MARK TASK COMPLETE ---")
    all_tasks = get_all_tasks()
    
    if not all_tasks:
        print("No tasks available.")
        return
    
    display_tasks(all_tasks)
    
    try:
        task_id = int(input("\nEnter task ID to mark complete: "))
        if mark_task_as_complete(task_id):
            print("✓ Task marked as complete!")
        else:
            print("✗ Task not found.")
    except ValueError:
        print("✗ Invalid input. Please enter a valid task ID.")


def view_progress_menu():
    """Display progress statistics."""
    print("\n--- PROGRESS ---")
    progress = calculate_progress()
    
    print(f"Total Tasks: {progress['total']}")
    print(f"Completed: {progress['completed']}")
    print(f"Completion Percentage: {progress['percentage']}%")
    
    # Visual progress bar
    if progress['total'] > 0:
        bar_length = 30
        filled = int(bar_length * progress['completed'] / progress['total'])
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"Progress: [{bar}]")


def delete_task_menu():
    """Handle deleting a task."""
    print("\n--- DELETE TASK ---")
    all_tasks = get_all_tasks()
    
    if not all_tasks:
        print("No tasks available.")
        return
    
    display_tasks(all_tasks)
    
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        if delete_task(task_id):
            print("✓ Task deleted successfully!")
        else:
            print("✗ Task not found.")
    except ValueError:
        print("✗ Invalid input. Please enter a valid task ID.")


def main():
    """Main program loop."""
    print("\nWelcome to the Task Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            add_task_menu()
        elif choice == '2':
            view_all_tasks_menu()
        elif choice == '3':
            view_pending_tasks_menu()
        elif choice == '4':
            mark_complete_menu()
        elif choice == '5':
            view_progress_menu()
        elif choice == '6':
            delete_task_menu()
        elif choice == '7':
            print("\nThank you for using Task Management System. Goodbye!")
            break
        else:
            print("✗ Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()