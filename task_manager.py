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
