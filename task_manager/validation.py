from datetime import datetime

def validate_task_title(title):
    """Validate task title is not empty and has reasonable length"""
    if not isinstance(title, str):
        return False
    if len(title) == 0:
        return False
    if len(title) > 100:
        return False
    return True


def validate_task_description(description):
    """Validate task description is not empty and has reasonable length"""
    if not isinstance(description, str):
        return False
    if len(description) == 0:
        return False
    if len(description) > 500:
        return False
    return True


def validate_due_date(due_date):
    """Validate due date is in format YYYY-MM-DD"""
    if not isinstance(due_date, str):
        return False
    
    try:
        datetime.strptime(due_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False