import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, IntVar
from datetime import datetime


class Task:
    def __init__(self, task_name, project_name, hours) -> None:
        self.task_name = task_name
        self.created_date = datetime.now()
        self.last_updated = self.created_date
        self.owner = project_name
        self.hours = hours

    def set_task_name(self, new_task_name: str) -> None:
        self.task_name = new_task_name

    def set_last_modified(self):
        self.last_updated = datetime.now()


class Project:
    def __init__(self, project_name, tasks=None) -> None:
        self.project_name = project_name
        self.tasks = tasks or []
        self.created_date = datetime.now()
        self.last_updated = self.created_date

    def set_project_name(self, new_project_name):
        self.project_name = new_project_name

    def set_last_modified(self):
        self.last_updated = datetime.now()

    def add_task(self, task_name, hours):
        new_task = Task(task_name, self.project_name, hours)
        self.tasks.append(new_task)


class TimeTrackingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Tracking App")
        self.style = ttk.Style("lumen")

        # Project variables
        self.project_name = StringVar()
        self.task_name = StringVar()
        self.task_hours = IntVar()
        self.projects = []
        self.selected_project = StringVar()

        # Project creation frame
        project_frame = ttk.Frame(self.root, padding=10)
        project_frame.pack(fill=BOTH, padx=10, pady=10)

        ttk.Label(project_frame, text="Project Name:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(project_frame, textvariable=self.project_name).grid(row=0, column=1, padx=5, pady=5)

        self.add_project_btn = ttk.Button(project_frame, text="Add Project", command=self.add_project)
        self.add_project_btn.grid(row=1, column=0, columnspan=2, pady=10)

        # Task creation frame
        task_frame = ttk.Frame(self.root, padding=10)
        task_frame.pack(fill=BOTH, padx=10, pady=10)

        ttk.Label(task_frame, text="Task Name:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(task_frame, textvariable=self.task_name).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(task_frame, text="Hours:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(task_frame, textvariable=self.task_hours).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(task_frame, text="Select Project:").grid(row=2, column=0, padx=5, pady=5)
        self.project_combobox = ttk.Combobox(task_frame, textvariable=self.selected_project)
        self.project_combobox.grid(row=2, column=1, padx=5, pady=5)

        self.add_task_btn = ttk.Button(task_frame, text="Add Task", command=self.add_task)
        self.add_task_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Project list frame
        self.project_list_frame = ttk.Frame(self.root, padding=10)
        self.project_list_frame.pack(fill=BOTH, padx=10, pady=10)
        self.update_project_list()

    def add_project(self):
        project_name = self.project_name.get()
        if project_name:
            new_project = Project(project_name)
            self.projects.append(new_project)
            self.update_project_list()
            self.update_project_combobox()

    def add_task(self):
        task_name = self.task_name.get()
        hours = self.task_hours.get()
        selected_project_name = self.selected_project.get()
        if selected_project_name and task_name and hours:
            project = next((p for p in self.projects if p.project_name == selected_project_name), None)
            if project:
                project.add_task(task_name, hours)
                self.update_project_list()

    def update_project_combobox(self):
        """Update the combobox with the list of project names."""
        project_names = [project.project_name for project in self.projects]
        self.project_combobox["values"] = project_names
        if project_names:
            self.selected_project.set(project_names[0])

    def update_project_list(self):
        """Update the display of projects and their tasks."""
        for widget in self.project_list_frame.winfo_children():
            widget.destroy()

        for project in self.projects:
            ttk.Label(self.project_list_frame, text=f"Project: {project.project_name}").pack(anchor=W)
            for task in project.tasks:
                ttk.Label(self.project_list_frame, text=f"  Task: {task.task_name}, Hours: {task.hours}, Last Updated: {task.last_updated}").pack(anchor=W)


if __name__ == "__main__":
    root = ttk.Window(themename="solar")
    app = TimeTrackingApp(root)
    root.mainloop()
