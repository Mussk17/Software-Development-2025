"""
Task Manager GUI Application
A simple, user-friendly task management application demonstrating GUI development
and UX design principles.
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import functions


class TaskManagerApp:
    """Main application class for the Task Manager GUI."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize task list
        self.tasks = []
        
        # Create UI components
        self.create_widgets()
        
        # Load existing tasks
        functions.load_tasks(self)
    
    def create_widgets(self):
        """Create and layout all GUI widgets."""
        
        # Title
        title_label = tk.Label(
            self.root,
            text="📋 Task Manager",
            font=('Arial', 20, 'bold'),
            bg='#4a90e2',
            fg='white',
            pady=15
        )
        title_label.pack(fill=tk.X)
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input section
        input_frame = tk.LabelFrame(
            main_frame,
            text="Add New Task",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            padx=15,
            pady=15
        )
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Task title
        tk.Label(
            input_frame,
            text="Task Title:",
            font=('Arial', 10),
            bg='#f0f0f0'
        ).pack(anchor=tk.W)
        
        self.title_entry = tk.Entry(
            input_frame,
            font=('Arial', 11),
            width=50
        )
        self.title_entry.pack(fill=tk.X, pady=(5, 10))
        self.title_entry.bind('<Return>', lambda e: self.add_task())
        
        # Priority selection
        priority_frame = tk.Frame(input_frame, bg='#f0f0f0')
        priority_frame.pack(fill=tk.X)
        
        tk.Label(
            priority_frame,
            text="Priority:",
            font=('Arial', 10),
            bg='#f0f0f0'
        ).pack(side=tk.LEFT)
        
        self.priority_var = tk.StringVar(value="Medium")
        
        tk.Radiobutton(
            priority_frame,
            text="Low",
            variable=self.priority_var,
            value="Low",
            bg='#f0f0f0',
            font=('Arial', 10)
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(
            priority_frame,
            text="Medium",
            variable=self.priority_var,
            value="Medium",
            bg='#f0f0f0',
            font=('Arial', 10)
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(
            priority_frame,
            text="High",
            variable=self.priority_var,
            value="High",
            bg='#f0f0f0',
            font=('Arial', 10)
        ).pack(side=tk.LEFT, padx=10)
        
        # Add button
        add_button = tk.Button(
            input_frame,
            text="Add Task",
            font=('Arial', 11, 'bold'),
            bg='#50c878',
            fg='white',
            command=self.add_task,
            padx=20,
            pady=8
        )
        add_button.pack(pady=(10, 0))
        
        # Task list section
        list_frame = tk.LabelFrame(
            main_frame,
            text="Your Tasks",
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            padx=15,
            pady=15
        )
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Task count
        self.task_count_label = tk.Label(
            list_frame,
            text="Total: 0 tasks",
            font=('Arial', 10),
            bg='#f0f0f0'
        )
        self.task_count_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Scrollable listbox for tasks
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(
            list_frame,
            font=('Arial', 11),
            height=15,
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE
        )
        self.task_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Action buttons frame
        button_frame = tk.Frame(list_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        complete_button = tk.Button(
            button_frame,
            text="Mark Complete",
            font=('Arial', 10),
            bg='#4a90e2',
            fg='white',
            command=self.mark_complete,
            padx=15,
            pady=5
        )
        complete_button.pack(side=tk.LEFT, padx=(0, 10))
        
        delete_button = tk.Button(
            button_frame,
            text="Delete Task",
            font=('Arial', 10),
            bg='#e74c3c',
            fg='white',
            command=self.delete_task,
            padx=15,
            pady=5
        )
        delete_button.pack(side=tk.LEFT)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            font=('Arial', 9),
            bg='#e0e0e0',
            anchor=tk.W,
            padx=10,
            pady=5
        )
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)
    
    def add_task(self):
        """Add a new task to the list."""
        title = self.title_entry.get().strip()
        priority = self.priority_var.get()
        
        if not title:
            messagebox.showwarning("Error", "Please enter a task title.")
            self.title_entry.focus()
            return
        
        # Create task
        task = functions.create_task(title, "", priority)
        self.tasks.append(task)
        
        # Clear input
        self.title_entry.delete(0, tk.END)
        self.priority_var.set("Medium")
        
        # Refresh display
        self.refresh_task_list()
        self.update_status(f"Task '{title}' added!")
        self.title_entry.focus()
    
    def refresh_task_list(self):
        """Refresh the task list display."""
        # Clear listbox
        self.task_listbox.delete(0, tk.END)
        
        # Add tasks to listbox
        for task in self.tasks:
            status = "✓" if task['completed'] else "☐"
            priority_symbol = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(task['priority'], "•")
            display_text = f"{status} {priority_symbol} {task['title']}"
            self.task_listbox.insert(tk.END, display_text)
        
        # Update count
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t['completed'])
        self.task_count_label.config(text=f"Total: {total} tasks ({completed} completed)")
        
        # Save tasks
        functions.save_tasks(self.tasks)
    
    def mark_complete(self):
        """Mark selected task as complete."""
        selection = self.task_listbox.curselection()
        
        if not selection:
            messagebox.showinfo("Info", "Please select a task first.")
            return
        
        index = selection[0]
        task = self.tasks[index]
        
        # Toggle completion
        task['completed'] = not task['completed']
        if task['completed']:
            task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.refresh_task_list()
        status = "completed" if task['completed'] else "marked as active"
        self.update_status(f"Task '{task['title']}' {status}!")
    
    def delete_task(self):
        """Delete selected task."""
        selection = self.task_listbox.curselection()
        
        if not selection:
            messagebox.showinfo("Info", "Please select a task first.")
            return
        
        index = selection[0]
        task = self.tasks[index]
        
        # Confirm deletion
        if messagebox.askyesno("Confirm", f"Delete task '{task['title']}'?"):
            self.tasks.pop(index)
            self.refresh_task_list()
            self.update_status(f"Task '{task['title']}' deleted.")
    
    def update_status(self, message):
        """Update status bar message."""
        self.status_label.config(text=message)
        # Clear after 3 seconds
        self.root.after(3000, lambda: self.status_label.config(text="Ready"))


def main():
    """Main entry point for the application."""
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
