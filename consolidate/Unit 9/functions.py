"""
Task Manager Functions
Business logic and data management for the Task Manager application.
"""

import json
import os
from datetime import datetime


def create_task(title, description, priority):
    """
    Create a new task dictionary.
    
    Args:
        title (str): Task title
        description (str): Task description (optional)
        priority (str): Task priority (Low, Medium, High)
    
    Returns:
        dict: Task dictionary with all properties
    """
    return {
        'title': title,
        'description': description,
        'priority': priority,
        'completed': False,
        'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def save_tasks(tasks):
    """
    Save tasks to a JSON file for persistence.
    
    Args:
        tasks (list): List of task dictionaries
    """
    try:
        filepath = get_data_filepath()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving tasks: {e}")


def load_tasks(app):
    """
    Load tasks from JSON file.
    
    Args:
        app: The main application instance
    """
    try:
        filepath = get_data_filepath()
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                app.tasks = json.load(f)
            app.refresh_task_list()
            app.update_status(f"Loaded {len(app.tasks)} task(s).")
        else:
            app.tasks = []
            app.refresh_task_list()
    except Exception as e:
        print(f"Error loading tasks: {e}")
        app.tasks = []
        app.refresh_task_list()


def get_data_filepath():
    """
    Get the filepath for storing task data.
    
    Returns:
        str: Path to the tasks.json file
    """
    # Store in the same directory as the application
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'tasks.json')

