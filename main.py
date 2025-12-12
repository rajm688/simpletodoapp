#!/usr/bin/env python3
"""Simple Todo App - Command Line Interface"""

from models import TodoManager

def display_menu():
    print("\n=== Simple Todo App ===")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")
    print("=" * 23)

def get_user_choice():
    try:
        return int(input("Enter your choice (1-5): "))
    except ValueError:
        return 0

def add_task_flow(todo_manager):
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty!")
        return
    
    print("Priority levels: 1=High, 2=Medium, 3=Low")
    try:
        priority = int(input("Enter priority (1-3): "))
        if priority not in [1, 2, 3]:
            priority = 2
    except ValueError:
        priority = 2
    
    task = todo_manager.add_task(description, priority)
    print(f"Task added successfully! ID: {task['id']}")

def view_tasks_flow(todo_manager):
    tasks = todo_manager.get_all_tasks()
    if not tasks:
        print("No tasks found!")
        return
    
    print("\n--- Your Tasks ---")
    priority_map = {1: "High", 2: "Medium", 3: "Low"}
    for task in tasks:
        status = "✓ Completed" if task['completed'] else "○ Pending"
        priority = priority_map[task['priority']]
        print(f"ID: {task['id']} | {status} | Priority: {priority}")
        print(f"    {task['description']}")
        print()

def complete_task_flow(todo_manager):
    try:
        task_id = int(input("Enter task ID to mark as completed: "))
        if todo_manager.mark_completed(task_id):
            print("Task marked as completed!")
        else:
            print("Task not found!")
    except ValueError:
        print("Please enter a valid task ID!")

def delete_task_flow(todo_manager):
    try:
        task_id = int(input("Enter task ID to delete: "))
        if todo_manager.delete_task(task_id):
            print("Task deleted successfully!")
        else:
            print("Task not found!")
    except ValueError:
        print("Please enter a valid task ID!")

def main():
    todo_manager = TodoManager()
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            add_task_flow(todo_manager)
        elif choice == 2:
            view_tasks_flow(todo_manager)
        elif choice == 3:
            complete_task_flow(todo_manager)
        elif choice == 4:
            delete_task_flow(todo_manager)
        elif choice == 5:
            print("Thank you for using Simple Todo App!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()