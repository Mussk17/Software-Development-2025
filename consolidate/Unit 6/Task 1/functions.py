FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    try:
        with open(filepath, 'r') as file_local:
            return file_local.readlines()
    except FileNotFoundError:
        # If file doesn't exist yet, start with an empty list
        return []


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def add_task(task_description):
    """Add a new task to the to-do list."""
    todos = get_todos()
    todos.append(task_description.capitalize() + '\n')
    write_todos(todos)


def display_tasks():
    """Display all tasks in the to-do list."""
    todos = get_todos()
    
    if not todos:
        print("No tasks yet.")
        return
    
    for index, item in enumerate(todos):
        item = item.strip('\n')
        print(f"{index + 1}. {item}")


def mark_completed(task_number):
    """Mark a task as completed by adding [x] prefix."""
    todos = get_todos()
    index = task_number - 1
    todo_line = todos[index].strip('\n')
    
    # Check if already completed
    if todo_line.startswith("[x]"):
        print("This task is already completed.")
        return
    
    # Remove existing markers if any
    todo_line = todo_line.replace("[ ] ", "").replace("[x] ", "")
    
    # Add completion marker
    todos[index] = "[x] " + todo_line + '\n'
    write_todos(todos)
    print(f"Task {task_number} marked as completed.")


if __name__ == "__main__":
    print(get_todos())
