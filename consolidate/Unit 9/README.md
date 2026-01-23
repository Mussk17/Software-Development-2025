# Unit 9: GUI Application Development - Task Manager

A simple, user-friendly Task Manager application built with Python's Tkinter library. This project demonstrates GUI development principles and usability best practices in a beginner-friendly way.

## Overview

This Task Manager application is designed to be:
- **Simple**: Easy to understand code structure
- **Functional**: Complete task management features
- **Educational**: Demonstrates GUI development concepts
- **User-Friendly**: Clean interface with good UX principles

## Design Inspiration

Before developing this application, we examined popular software applications with well-designed interfaces:

### Key Observations from Modern Applications:

1. **Web Browsers (Chrome, Firefox)**
   - Clear header with title
   - Simple navigation
   - Status bar for feedback

2. **Office Suites (Microsoft Office)**
   - Organized sections with labels
   - Clear button placement
   - Consistent styling

3. **Task Management Tools (Todoist, Microsoft To-Do)**
   - Simple list-based interface
   - Priority indicators
   - Easy task completion

### Applied Design Principles:

- **Visual Hierarchy**: Title at top, organized sections
- **Consistency**: Uniform button styles and colors
- **Feedback**: Status messages and confirmations
- **Simplicity**: Clean interface without clutter
- **Accessibility**: Clear labels and intuitive controls

## Features

### Core Functionality

1. **Add Tasks**
   - Enter task title
   - Select priority (Low, Medium, High)
   - Click "Add Task" button
   - Tasks saved automatically

2. **View Tasks**
   - All tasks displayed in a scrollable list
   - Visual indicators:
     - ☐ = Not completed
     - ✓ = Completed
     - 🔴 = High priority
     - 🟡 = Medium priority
     - 🟢 = Low priority

3. **Manage Tasks**
   - Select a task from the list
   - Mark as complete/incomplete
   - Delete tasks with confirmation
   - Task count display

4. **Data Persistence**
   - Tasks automatically saved to JSON file
   - Tasks loaded when application starts
   - No data loss between sessions

## How to Run

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Running the Application

```bash
cd "Unit 9"
python main.py
```

The application will launch with a simple GUI window. If you have previously saved tasks, they will be automatically loaded.

## Application Structure

```
Unit 9/
├── main.py          # Main GUI application
├── functions.py     # Business logic and data persistence
├── tasks.json       # Task data storage (created automatically)
└── README.md        # This documentation
```

## GUI Layout

```
┌─────────────────────────────────────┐
│     📋 Task Manager (Header)       │
├─────────────────────────────────────┤
│                                     │
│  ┌─ Add New Task ───────────────┐  │
│  │ Task Title: [____________]   │  │
│  │ Priority: ○ Low ○ Medium ● High│ │
│  │         [ Add Task ]          │  │
│  └───────────────────────────────┘  │
│                                     │
│  ┌─ Your Tasks ─────────────────┐  │
│  │ Total: 3 tasks (1 completed) │  │
│  │ ┌──────────────────────────┐ │  │
│  │ │ ☐ 🟡 Buy groceries      │ │  │
│  │ │ ✓ 🔴 Finish assignment  │ │  │
│  │ │ ☐ 🟢 Call mom           │ │  │
│  │ └──────────────────────────┘ │  │
│  │ [Mark Complete] [Delete Task] │  │
│  └───────────────────────────────┘  │
│                                     │
│  Status: Ready                      │
└─────────────────────────────────────┘
```

## Code Structure

### main.py

The main application file contains:

- **TaskManagerApp Class**: Main application controller
  - `__init__()`: Initialize application and create UI
  - `create_widgets()`: Build all GUI components
  - `add_task()`: Handle task creation
  - `refresh_task_list()`: Update task display
  - `mark_complete()`: Toggle task completion
  - `delete_task()`: Handle task deletion
  - `update_status()`: Update status bar

### functions.py

Business logic module containing:

- **Data Management**
  - `create_task()`: Create new task objects
  - `save_tasks()`: Save tasks to JSON file
  - `load_tasks()`: Load tasks from JSON file
  - `get_data_filepath()`: Get file path for storage

## Data Storage

Tasks are stored in `tasks.json` in JSON format:

```json
[
  {
    "title": "Complete Unit 9 assignment",
    "description": "",
    "priority": "High",
    "completed": false,
    "created": "2024-01-15 14:30:00"
  }
]
```

The file is automatically created on first use and updated whenever tasks are modified.

## Color Scheme

Simple, clear color palette:

- **Blue** (`#4a90e2`): Primary actions, header
- **Green** (`#50c878`): Add button, low priority
- **Red** (`#e74c3c`): Delete button, high priority
- **Yellow** (`#f39c12`): Medium priority
- **Light Gray** (`#f0f0f0`): Background

## User Workflow

### Adding a Task

1. Type task title in the "Task Title" field
2. Select priority using radio buttons
3. Click "Add Task" button (or press Enter)
4. Task appears in the list immediately
5. Status bar confirms task creation

### Completing a Task

1. Click on a task in the list to select it
2. Click "Mark Complete" button
3. Task shows ✓ checkmark
4. Status bar confirms update

### Deleting a Task

1. Click on a task in the list to select it
2. Click "Delete Task" button
3. Confirm deletion in dialog
4. Task is removed from list
5. Status bar confirms deletion

## Learning Objectives

This project demonstrates:

1. **GUI Development Basics**
   - Creating windows and frames
   - Using labels, buttons, entries, listboxes
   - Layout management with pack()
   - Event handling

2. **UX Design Principles**
   - Visual hierarchy
   - Consistency
   - User feedback
   - Error handling

3. **Python Programming**
   - Object-oriented design
   - File I/O with JSON
   - GUI framework usage
   - Event-driven programming

4. **Software Engineering**
   - Separation of concerns (UI vs. logic)
   - Data persistence
   - Input validation
   - Error handling

## Key Concepts Explained

### GUI Components Used

1. **Label**: Display text (title, labels, status)
2. **Entry**: Single-line text input (task title)
3. **Radiobutton**: Priority selection
4. **Button**: Actions (Add, Mark Complete, Delete)
5. **Listbox**: Display list of tasks
6. **Scrollbar**: Scroll through long lists
7. **LabelFrame**: Group related widgets

### Event Handling

- Button clicks trigger functions
- Enter key in entry field adds task
- Listbox selection for task operations

### Data Persistence

- Tasks stored in JSON format
- Automatic save on changes
- Automatic load on startup

## Usability Principles Applied

1. **Simplicity**: Clean, uncluttered interface
2. **Feedback**: Status messages for all actions
3. **Error Prevention**: Input validation, confirmations
4. **Consistency**: Uniform styling throughout
5. **Recognition**: Clear labels and visual indicators

## Troubleshooting

### Common Issues

**Application won't start:**
- Ensure Python 3.6+ is installed
- Verify Tkinter: `python -m tkinter`

**Tasks not saving:**
- Check file permissions in Unit 9 directory
- Verify `tasks.json` is not read-only

**GUI looks different:**
- Tkinter appearance varies by operating system
- This is normal and expected

## Extensions (Optional)

If you want to extend this project:

1. Add task descriptions
2. Add due dates
3. Add task editing
4. Add search functionality
5. Add categories/tags
6. Add statistics display

## Conclusion

This Task Manager application demonstrates practical GUI development skills in a beginner-friendly way. The code is simple to understand while still showing important concepts like:

- GUI component creation
- Event handling
- Data persistence
- User feedback
- Error handling

The principles learned here apply to all GUI development, whether building desktop applications, web interfaces, or mobile apps.

---

*This unit demonstrates practical GUI development skills and UX design principles through a simple, educational application.*
