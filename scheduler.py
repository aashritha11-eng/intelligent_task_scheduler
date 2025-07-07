from utils import days_until_deadline

def calculate_score(task):
    priority_score = (4 - task['priority']) * 10  # 1 = high → 30 pts
    deadline_urgency = max(0, 20 - days_until_deadline(task['deadline']))  # closer deadlines = higher
    effort_penalty = -task['effort_hours']  # more effort = less score
    return priority_score + deadline_urgency + effort_penalty

def create_schedule(tasks, hours_per_day=6):
    for task in tasks:
        task['score'] = calculate_score(task)

    sorted_tasks = sorted(tasks, key=lambda x: x['score'], reverse=True)

    schedule = {}
    current_day = "Day 1"
    hours_used = 0
    schedule[current_day] = []

    for task in sorted_tasks:
        if hours_used + task['effort_hours'] > hours_per_day:
            hours_used = 0
            current_day = f"Day {int(current_day.split()[1]) + 1}"
            schedule[current_day] = []

        schedule[current_day].append(task)
        hours_used += task['effort_hours']

    return schedule
