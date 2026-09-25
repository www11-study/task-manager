class Task:

    def __init__(self,title,priority,due_date):
        self.title = title
        self.completed = False
        self.priority = priority
        self.due_date = due_date

    def complete(self):
        self.completed = True





