# 🧠 Intelligent Task Scheduler

## 🚀 Problem Statement

Design and implement a smart scheduling system that optimally assigns tasks based on **deadlines**, **priorities**, and **estimated effort**.

This system should process a list of task metadata and generate an optimized **daily or weekly schedule**, helping users manage time efficiently based on intelligent prioritization.

---

## 🧩 Skills Demonstrated

- **AI/Logic-Based Task Scoring**: Implements a custom priority scoring system that factors in urgency, priority level, and required effort.
- **Critical Thinking**: Balances competing tasks, deadlines, and constraints with logical day-by-day planning.
- **Problem Solving**: Handles tasks with conflicting deadlines or high effort using score-based decision making.
- **Modular Code Design**: Organized with clear modules:
  - `input_module.py` → Input handling
  - `scheduler.py` → Scoring + scheduling logic
  - `utils.py` → Helper functions
  - `main.py` → Entry point
- **Clear Architecture**: Input → Scoring → Scheduling → Output, with easy extension capability.

---

## 📦 Project Structure

intelligent-task-scheduler/
├── main.py
├── scheduler.py
├── input_module.py
├── utils.py
├── tasks.json
└── README.md


---

## 📥 Input Format (`tasks.json`)

Each task object contains:
- `task_name` (str)
- `deadline` (YYYY-MM-DD)
- `priority` (1 = High, 2 = Medium, 3 = Low)
- `effort_hours` (int)

Example:

```json
[
  {
    "task_name": "Write Report",
    "deadline": "2025-07-10",
    "priority": 1,
    "effort_hours": 3
  }
]
