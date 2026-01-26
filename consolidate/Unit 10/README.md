# Project Management System - Unit 10 Consolidation

## Overview

A clean, concise project management application that demonstrates integration of concepts from all course units (4-9) in a single, well-organized file.

## How to Run

```bash
cd "Unit 10"
python main.py
```

## Features

- ✅ Create and manage multiple projects
- ✅ Add tasks with priorities (High, Medium, Low)
- ✅ Mark tasks as completed
- ✅ View project statistics (completed/total tasks)
- ✅ Automatic data persistence (JSON)
- ✅ Recursive task counting

## Course Concepts Demonstrated

### Unit 4: Data Types & File Handling
- **Dictionaries**: Storing projects and tasks as dictionary structures
- **File I/O**: JSON file operations for data persistence
- **Data Structures**: Lists and dictionaries for organizing data

### Unit 5: Built-in Packages
- **json**: Data serialization and deserialization
- **os**: File existence checking
- **datetime**: Timestamp generation for project creation
- **Code Comments**: Clear documentation throughout

### Unit 6: Functions & Modular Design
- **Modular Functions**: Each feature in separate function
- **Function Organization**: Logical grouping of related functions
- **Code Reusability**: Functions designed for reuse

### Unit 7: Loop Structures
- **For Loops**: Iterating through projects and tasks
- **List Comprehensions**: Used in recursive counting functions
- **Data Processing**: Loops for displaying and updating data

### Unit 8: Recursion
- **Recursive Counting**: `count_tasks()` recursively counts all tasks including subtasks
- **Recursive Completion**: `count_done()` recursively counts completed tasks
- **Base Cases**: Proper termination conditions
- **Recursive Cases**: Functions calling themselves with smaller problems

### Unit 9: GUI Development
- **Tkinter Interface**: Complete graphical user interface
- **Event Handling**: Button clicks and listbox selections
- **Layout Management**: Two-panel design (projects left, tasks right)
- **User Interaction**: Input fields, buttons, and displays

## Code Structure

The application is organized into clear sections:

1. **File Handling**: Load and save data functions
2. **Recursion**: Recursive counting functions
3. **Project Logic**: Project creation and selection
4. **Task Logic**: Task creation and completion
5. **Display**: Functions to refresh UI
6. **GUI**: Interface setup and initialization

## Usage

1. **Create Project**: Enter project name and press Enter or click "Add Project"
2. **Select Project**: Click on a project in the left list
3. **Add Task**: Select a project, enter task name, choose priority, click "Add Task"
4. **Mark Complete**: Select a task and click "Toggle Complete"
5. **View Statistics**: Project list shows completed/total task counts

## Data Storage

Projects are automatically saved to `projects.json` in the same directory. The file is created automatically on first save.

## Requirements

- Python 3.6+
- Tkinter (included with Python)

No external packages required!

## Key Features

### Recursive Task Counting
The application uses recursion to count tasks at any nesting level:
- Main tasks are counted
- Subtasks are recursively counted
- Completed tasks are tracked recursively

### Clean Code Design
- Single file for easy sharing
- Clear function organization
- Concise and readable code
- Professional structure

## Software Development Life Cycle

This project demonstrates:

1. **Requirements Analysis**: Identified need for project management tool
2. **Design**: Simple, functional interface design
3. **Implementation**: Clean, modular code structure
4. **Testing**: Manual testing of all features
5. **Deployment**: Single-file distribution
6. **Maintenance**: Well-documented for future updates

## Project Highlights

- **Single File**: Everything in one `main.py` file
- **All Units Covered**: Demonstrates concepts from Units 4-9
- **Recursion**: Advanced recursive algorithms for task counting
- **Clean Code**: Professional, readable structure
- **Functional**: Complete working application

## Example Usage

```
1. Run: python main.py
2. Enter "My Project" and press Enter
3. Click on "My Project" in the list
4. Enter "Complete assignment" and click "Add Task"
5. Select the task and click "Toggle Complete"
6. See statistics update: "My Project (1/1)"
```

## Conclusion

This consolidation project successfully demonstrates:
- Integration of all course units (4-9)
- Software development best practices
- Clean, maintainable code
- Functional GUI application
- Recursive programming concepts

