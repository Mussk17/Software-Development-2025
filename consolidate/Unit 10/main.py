"""
Project Management System – Unit 10 Consolidation

Demonstrates:
• Data & file handling (Unit 4)
• Built-in modules: json, os, datetime (Unit 5)
• Functions & modular design (Unit 6)
• Loops (Unit 7)
• Recursion for subtasks (Unit 8)
• GUI with Tkinter (Unit 9)
"""

import tkinter as tk
from tkinter import messagebox
import json, os
from datetime import datetime

FILE = "projects.json"
projects = []
current = -1


# ---------- FILE HANDLING ----------
def load_data():
    global projects
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                projects = json.load(f)
        except json.JSONDecodeError:
            projects = []


def save_data():
    with open(FILE, "w") as f:
        json.dump(projects, f, indent=4)


# ---------- RECURSION ----------
def count_tasks(tasks):
    if not tasks:
        return 0
    return sum(1 + count_tasks(t.get("subtasks", [])) for t in tasks)


def count_done(tasks):
    if not tasks:
        return 0
    return sum((1 if t["completed"] else 0) + count_done(t.get("subtasks", [])) for t in tasks)


# ---------- PROJECT LOGIC ----------
def add_project():
    name = proj_entry.get().strip()
    if not name:
        return
    projects.append({"name": name, "tasks": [], "created": datetime.now().isoformat()})
    proj_entry.delete(0, tk.END)
    refresh_projects()
    save_data()


def select_project(_=None):
    global current
    sel = proj_list.curselection()
    if sel:
        current = sel[0]
        refresh_tasks()


# ---------- TASK LOGIC ----------
def add_task():
    if current == -1:
        return
    name = task_entry.get().strip()
    if not name:
        return
    projects[current]["tasks"].append({
        "name": name,
        "priority": priority.get(),
        "completed": False,
        "subtasks": []
    })
    task_entry.delete(0, tk.END)
    refresh_tasks()
    save_data()


def toggle_task():
    if current == -1:
        return
    sel = task_list.curselection()
    if sel:
        t = projects[current]["tasks"][sel[0]]
        t["completed"] = not t["completed"]
        refresh_tasks()
        save_data()


# ---------- DISPLAY ----------
def refresh_projects():
    proj_list.delete(0, tk.END)
    for p in projects:
        total = count_tasks(p["tasks"])
        done = count_done(p["tasks"])
        proj_list.insert(tk.END, f"{p['name']} ({done}/{total})")


def refresh_tasks():
    task_list.delete(0, tk.END)
    if current == -1:
        return
    for t in projects[current]["tasks"]:
        mark = "[DONE] " if t["completed"] else ""
        task_list.insert(tk.END, f"{mark}{t['name']} [{t['priority']}]")
    refresh_projects()


# ---------- GUI ----------
root = tk.Tk()
root.title("Project Manager")

left = tk.Frame(root)
left.pack(side=tk.LEFT, padx=10)

right = tk.Frame(root)
right.pack(side=tk.RIGHT, padx=10)

tk.Label(left, text="Projects").pack()
proj_entry = tk.Entry(left)
proj_entry.pack()
tk.Button(left, text="Add Project", command=add_project).pack()
proj_list = tk.Listbox(left, height=10)
proj_list.pack()
proj_list.bind("<<ListboxSelect>>", select_project)

tk.Label(right, text="Tasks").pack()
task_entry = tk.Entry(right)
task_entry.pack()
priority = tk.StringVar(value="Medium")
tk.OptionMenu(right, priority, "High", "Medium", "Low").pack()
tk.Button(right, text="Add Task", command=add_task).pack()
tk.Button(right, text="Toggle Complete", command=toggle_task).pack()
task_list = tk.Listbox(right, height=10)
task_list.pack()

load_data()
refresh_projects()
root.mainloop()
