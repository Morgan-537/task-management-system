"""
validation.py - Validation functions for task input
"""

def validate_task_title(title):
    """
    Validate that the task title is not empty and has reasonable length.
    
    Args:
        title (str): The task title to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(title, str):
        return False
    if len(title) == 0:
        return False
    if len(title) > 100:
        return False
    return True


def validate_task_description(description):
    """
    Validate that the task description is not empty and has reasonable length.
    
    Args:
        description (str): The task description to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(description, str):
        return False
    if len(description) == 0:
        return False
    if len(description) > 500:
        return False
    return True


def validate_due_date(due_date):
    """
    Validate that the due date is in the correct format (YYYY-MM-DD).
    
    Args:
        due_date (str): The due date to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(due_date, str):
        return False
    
    # Check format YYYY-MM-DD
    if len(due_date) != 10:
        return False
    
    parts = due_date.split('-')
    if len(parts) != 3:
        return False
    
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        
        # Basic validation
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if year < 2000 or year > 2100:
            return False
        
        return True
    except ValueError:
        return False