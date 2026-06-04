from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []


def add_task(title, description, due_date):
    """Add a new task to the task list"""
    # Validate inputs
    if not validate_task_title(title):
        return False
    if not validate_task_description(description):
        return False
    if not validate_due_date(due_date):
        return False
    
    # Create task dictionary
    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'completed': False
    }
    
    tasks.append(task)
    print("Task added successfully!")
    return True


def mark_task_as_complete(index, tasks=tasks):
    """Mark a task as complete by index"""
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print("Task marked as complete!")
        return True
    return False


def view_pending_tasks(tasks=tasks):
    """View all pending (incomplete) tasks"""
    pending = [task for task in tasks if not task['completed']]
    
    if not pending:
        print("No pending tasks.")
        return pending
    
    print("\nPending Tasks:")
    for i, task in enumerate(pending):
        print(f"{i + 1}. {task['title']} - Due: {task['due_date']}")
    
    return pending


def calculate_progress(tasks=tasks):
    """Calculate completion progress"""
    if len(tasks) == 0:
        progress = 0.0
    else:
        completed = sum(1 for task in tasks if task['completed'])
        progress = (completed / len(tasks)) * 100
    
    return progress