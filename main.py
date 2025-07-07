from input_module import load_tasks
from scheduler import create_schedule

def print_schedule(schedule):
    for day, tasks in schedule.items():
        print(f"\n{day}:")
        for task in tasks:
            print(f"  - {task['task_name']} ({task['effort_hours']} hrs, Priority {task['priority']}, Deadline {task['deadline']})")

if __name__ == "__main__":
    tasks = load_tasks()
    schedule = create_schedule(tasks)
    print_schedule(schedule)
