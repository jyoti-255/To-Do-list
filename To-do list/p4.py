import tkinter as tk
from tkinter import messagebox


entry_task = None

def add_task():
    global entry_task  
    task = entry_task.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_tasks_display()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def mark_completed():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        update_tasks_display()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        del tasks[selected_index]
        update_tasks_display()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")

def update_tasks_display():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Not Completed"
        tasks_listbox.insert(tk.END, f"{task['task']} - {status}")

def main():
    global entry_task  
    global tasks  
    global tasks_listbox

    # Create main window
    root = tk.Tk()
    root.title("Todo List")

    # Task entry
    frame_entry = tk.Frame(root)
    frame_entry.pack(pady=10)
    label_task = tk.Label(frame_entry, text="Task:")
    label_task.pack(side=tk.LEFT)
    entry_task = tk.Entry(frame_entry, width=50)
    entry_task.pack(side=tk.LEFT)

    # Buttons
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=5)
    button_add = tk.Button(frame_buttons, text="Add Task", command=add_task)
    button_add.pack(side=tk.LEFT, padx=5)
    button_complete = tk.Button(frame_buttons, text="Mark Completed", command=mark_completed)
    button_complete.pack(side=tk.LEFT, padx=5)
    button_delete = tk.Button(frame_buttons, text="Delete Task", command=delete_task)
    button_delete.pack(side=tk.LEFT, padx=5)

    # Tasks list
    tasks_listbox = tk.Listbox(root, width=50)
    tasks_listbox.pack()

    # Initialize tasks list
    tasks = []

    root.mainloop()

if __name__ == "__main__":
    main()

