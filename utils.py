from datetime import datetime

def days_until_deadline(deadline_str):
    today = datetime.today()
    deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
    return max((deadline - today).days, 0)
