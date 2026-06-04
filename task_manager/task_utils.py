from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):

    if not validate_task_title(title):
        return False

    if not validate_task_description(description):
        return False

    if not validate_due_date(due_date):
        return False

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")
    return True


def mark_task_as_complete(index, tasks=tasks):

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
        return True

    return False


def view_pending_tasks(tasks=tasks):

    pending_tasks = []

    for task in tasks:
        if task["completed"] is False:
            pending_tasks.append(task)

    for i, task in enumerate(pending_tasks):
        print(f"{i + 1}. {task['title']}")

    return pending_tasks


def calculate_progress(tasks=tasks):

    if len(tasks) == 0:
        progress = 0.0

    else:
        completed_tasks = 0

        for task in tasks:
            if task["completed"]:
                completed_tasks += 1

        progress = (completed_tasks / len(tasks)) * 100

    return progress