from storage import save_tasks
from storage import load_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def save(self):
        save_tasks(self.tasks)

    def add_task(self,task):
        self.tasks.append(task)

    def delete_task(self,index):
        self.tasks.pop(index)

    def complete_task(self,index):
        self.tasks[index].complete()

    def edit_task(self,index,title,priority,due_date):
        task = self.tasks[index]

        task.title = title
        task.priority = priority
        task.due_date = due_date
        
        self.save()

    def search_tasks(self,keyword):
        result = []
        for task in self.tasks:
            if keyword in task.title:
                result.append(task)

        return result

    def sort_tasks(self):
        priority_level = {
            "高" : 1, 
            "中" : 2, 
            "低" : 3
        }

        self.tasks = sorted(self.tasks,key=lambda task:priority_level[task.priority])


