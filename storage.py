import json
from task import Task

def save_tasks(tasks):
    data = []

    for task in tasks:
        data.append(
            {
                "title" : task.title,
                "priority" : task.priority,
                "completed" : task.completed,
                "due_date" : task.due_date
            }
        )

    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        tasks = []

        for item in data:
            task = Task(item["title"],item["priority"],item["due_date"])
            task.completed = item["completed"]
            tasks.append(task)

        return tasks

    except FileNotFoundError:
        return []

