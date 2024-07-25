def schedule_tasks(task_hierarchy):
    def schedule(task, scheduled_tasks):
        # Add the task to the schedule
        scheduled_tasks.append(task['id'])

        # Sort subtasks by priority (higher priority comes first)
        subtasks = sorted(task.get('subtasks', []), key=lambda x: x.get('priority', 0), reverse=True)

        # Recursively schedule subtasks
        for subtask in subtasks:
            schedule(subtask, scheduled_tasks)

    scheduled_tasks = []
    # Start scheduling from the top-level tasks
    for task in sorted(task_hierarchy, key=lambda x: x.get('priority', 0), reverse=True):
        schedule(task, scheduled_tasks)

    return scheduled_tasks

# Test case
task_hierarchy = [
    {
        'id': '1',
        'name': 'Task 1',
        'priority': 2,
        'subtasks': [
            {
                'id': '2',
                'name': 'Task 1.1',
                'priority': 1,
                'subtasks': []
            },
            {
                'id': '3',
                'name': 'Task 1.2',
                'priority': 3,
                'subtasks': []
            }
        ]
    },
    {
        'id': '4',
        'name': 'Task 2',
        'priority': 4,
        'subtasks': [
            {
                'id': '5',
                'name': 'Task 2.1',
                'priority': 2,
                'subtasks': []
            }
        ]
    }
]

# Running the test
print("Scheduled Tasks:", schedule_tasks(task_hierarchy))

# Analyze:

# Time complexity: O(n log n)
# Space complexity: O(n)