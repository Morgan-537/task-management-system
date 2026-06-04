"""
task_utils.py - Task management utility functions
"""

from validation import validate_task_title, validate_task_description, validate_due_date

# Global task list - stores all tasks
tasks = []
task_id_counter = 1


def add_task(title, description, due_date):
    """
    Add a new task to the task list with validation.
    
    Args:
        title (str): The task title
        description (str): The task description
        due_date (str): The task due date in format YYYY-MM-DD
        
    Returns:
        bool: True if task was added successfully, False otherwise
    """
    global task_id_counter
    
    # Validate all inputs
    if not validate_task_title(title):
        return False
    
    if not validate_task_description(description):
        return False
    
    if not validate_due_date(due_date):
        return False
    
    # Create task dictionary
    task = {
        'id': task_id_counter,
        'title': title,
        'description': description,
        'due_date': due_date,
        'completed': False
    }
    
    # Add task to list
    tasks.append(task)
    task_id_counter += 1
    
    return True


def mark_task_as_complete(task_id):
    """
    Mark a task as complete by its ID.
    
    Args:
        task_id (int): The ID of the task to mark complete
        
    Returns:
        bool: True if task was marked complete, False if task not found
    """
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return True
    
    return False


def view_pending_tasks():
    """
    Get a list of all pending (incomplete) tasks.
    
    Returns:
        list: List of pending tasks (dictionaries)
    """
    pending = []
    for task in tasks:
        if not task['completed']:
            pending.append(task)
    
    return pending


def calculate_progress():
    """
    Calculate the progress of task completion.
    
    Returns:
        dict: Dictionary with 'total', 'completed', and 'percentage' keys
    """
    if len(tasks) == 0:
        return {
            'total': 0,
            'completed': 0,
            'percentage': 0
        }
    
    total = len(tasks)
    completed = sum(1 for task in tasks if task['completed'])
    percentage = (completed / total) * 100
    
    return {
        'total': total,
        'completed': completed,
        'percentage': round(percentage, 2)
    }


def get_all_tasks():
    """
    Get all tasks.
    
    Returns:
        list: List of all tasks
    """
    return tasks


def delete_task(task_id):
    """
    Delete a task by its ID.
    
    Args:
        task_id (int): The ID of the task to delete
        
    Returns:
        bool: True if task was deleted, False if task not found
    """
    global tasks
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            return True
    
    return False