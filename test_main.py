"""Comprehensive tests for Simple Todo App"""

import pytest
from models import TodoManager

@pytest.fixture
def todo_manager():
    """Create a fresh TodoManager instance for each test"""
    manager = TodoManager()
    manager.clear_all_tasks()
    return manager

def test_add_task(todo_manager):
    """Test adding a new task"""
    task = todo_manager.add_task("Buy groceries", 1)
    
    assert task['id'] == 1
    assert task['description'] == "Buy groceries"
    assert task['priority'] == 1
    assert task['completed'] is False
    assert todo_manager.get_task_count() == 1

def test_add_multiple_tasks(todo_manager):
    """Test adding multiple tasks"""
    task1 = todo_manager.add_task("Task 1", 1)
    task2 = todo_manager.add_task("Task 2", 2)
    task3 = todo_manager.add_task("Task 3", 3)
    
    assert task1['id'] == 1
    assert task2['id'] == 2
    assert task3['id'] == 3
    assert todo_manager.get_task_count() == 3

def test_get_all_tasks_sorted(todo_manager):
    """Test getting all tasks sorted by priority"""
    todo_manager.add_task("Low priority", 3)
    todo_manager.add_task("High priority", 1)
    todo_manager.add_task("Medium priority", 2)
    
    tasks = todo_manager.get_all_tasks()
    assert len(tasks) == 3
    assert tasks[0]['priority'] == 1  # High priority first
    assert tasks[1]['priority'] == 2  # Medium priority second
    assert tasks[2]['priority'] == 3  # Low priority last

def test_mark_task_completed(todo_manager):
    """Test marking a task as completed"""
    task = todo_manager.add_task("Complete this task")
    assert task['completed'] is False
    
    result = todo_manager.mark_completed(task['id'])
    assert result is True
    
    updated_task = todo_manager.get_task_by_id(task['id'])
    assert updated_task['completed'] is True

def test_mark_nonexistent_task_completed(todo_manager):
    """Test marking a nonexistent task as completed"""
    result = todo_manager.mark_completed(999)
    assert result is False

def test_delete_task(todo_manager):
    """Test deleting a task"""
    task = todo_manager.add_task("Delete me")
    assert todo_manager.get_task_count() == 1
    
    result = todo_manager.delete_task(task['id'])
    assert result is True
    assert todo_manager.get_task_count() == 0
    
    deleted_task = todo_manager.get_task_by_id(task['id'])
    assert deleted_task is None

def test_delete_nonexistent_task(todo_manager):
    """Test deleting a nonexistent task"""
    result = todo_manager.delete_task(999)
    assert result is False

def test_get_pending_and_completed_tasks(todo_manager):
    """Test filtering tasks by completion status"""
    task1 = todo_manager.add_task("Pending task")
    task2 = todo_manager.add_task("Completed task")
    
    todo_manager.mark_completed(task2['id'])
    
    pending = todo_manager.get_pending_tasks()
    completed = todo_manager.get_completed_tasks()
    
    assert len(pending) == 1
    assert len(completed) == 1
    assert pending[0]['id'] == task1['id']
    assert completed[0]['id'] == task2['id']

def test_task_stats(todo_manager):
    """Test getting task statistics"""
    todo_manager.add_task("Task 1")
    todo_manager.add_task("Task 2")
    task3 = todo_manager.add_task("Task 3")
    
    todo_manager.mark_completed(task3['id'])
    
    stats = todo_manager.get_task_stats()
    assert stats['total'] == 3
    assert stats['pending'] == 2
    assert stats['completed'] == 1

def test_clear_all_tasks(todo_manager):
    """Test clearing all tasks"""
    todo_manager.add_task("Task 1")
    todo_manager.add_task("Task 2")
    assert todo_manager.get_task_count() == 2
    
    todo_manager.clear_all_tasks()
    assert todo_manager.get_task_count() == 0
    
    # Test that next task gets ID 1 after clearing
    new_task = todo_manager.add_task("New task")
    assert new_task['id'] == 1