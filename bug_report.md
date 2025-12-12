# Bug Injection Report

## Project: SimpleTodoApp

### Bug Summary
- Total Bugs Injected: 3
- Bug Types: Logic error, Off-by-one error, Missing state reset

---

### BUG-001: Logic error - incorrect condition
**File:** models.py:40
**Type:** Logic error - incorrect condition

**Description:**
Mark completed only works if task is not already completed, preventing re-marking

**Original Code:**
```python
if task:
```

**Buggy Code:**
```python
if task and not task['completed']:
```

**Reason:**
Developer added unnecessary condition thinking it prevents duplicate completion

**Expected Impact:**
Tests trying to mark already completed tasks will fail

---

### BUG-002: Off-by-one error in loop
**File:** models.py:46
**Type:** Off-by-one error in loop

**Description:**
Loop range excludes last element, preventing deletion of last task

**Original Code:**
```python
for i in range(len(self.tasks)):
```

**Buggy Code:**
```python
for i in range(len(self.tasks) - 1):
```

**Reason:**
Common mistake when trying to avoid index out of bounds but going too far

**Expected Impact:**
Deleting the last task in the list will fail

---

### BUG-003: Missing state reset
**File:** models.py:58
**Type:** Missing state reset

**Description:**
Clear tasks doesn't reset next_id counter, causing ID gaps

**Original Code:**
```python
self.tasks.clear()
next_id = 1
```

**Buggy Code:**
```python
self.tasks.clear()
```

**Reason:**
Forgot to reset the ID counter when clearing all tasks

**Expected Impact:**
Tests expecting ID to restart at 1 after clearing will fail
