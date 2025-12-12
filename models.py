"""Todo App Data Models and Business Logic"""

# In-memory storage
tasks = []
next_id = 1

class TodoManager:
    """Manages todo tasks with in-memory storage"""
    
    def __init__(self):
        global tasks, next_id
        self.tasks = tasks
        self.next_id = next_id
    
    def add_task(self, description, priority=2):
        """Add a new task with description and priority"""
        global next_id
        
        task = {
            'id': next_id,
            'description': description,
            'priority': priority,
            'completed': False
        }
        
        self.tasks.append(task)
        next_id += 1
        return task
    
    def get_all_tasks(self):
        """Get all tasks sorted by priority then by ID"""
        return sorted(self.tasks, key=lambda x: (x['priority'], x['id']))
    
    def get_task_by_id(self, task_id):
        """Get a specific task by ID"""
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def mark_completed(self, task_id):
        """Mark a task as completed"""
        task = self.get_task_by_id(task_id)
        if task:
            task['completed'] = True
            return True
        return False
    
    def delete_task(self, task_id):
        """Delete a task by ID"""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
    
    def get_pending_tasks(self):
        """Get all pending (not completed) tasks"""
        return [task for task in self.tasks if not task['completed']]
    
    def get_completed_tasks(self):
        """Get all completed tasks"""
        return [task for task in self.tasks if task['completed']]
    
    def clear_all_tasks(self):
        """Clear all tasks (useful for testing)"""
        global next_id
        self.tasks.clear()
        next_id = 1
    
    def get_task_count(self):
        """Get total number of tasks"""
        return len(self.tasks)
    
    def get_task_stats(self):
        """Get task statistics"""
        total = len(self.tasks)
        completed = len(self.get_completed_tasks())
        pending = len(self.get_pending_tasks())
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending
        }