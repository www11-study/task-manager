from task import Task
from datetime import datetime
from task_manager import TaskManager

manager = TaskManager()

def get_priority():
    while True:
        priority = input("请输入优先级(高/中/低):")
        if priority in ["高","中","低"]:
            return priority
        print("请输入:高/中/低 ~")

def get_due_date():
    while True:
        due_date = input("请输入截止日期(如 2026-10-01):") 
        try:
            datetime.strptime(due_date,"%Y-%m-%d")
            return due_date
        except ValueError:
            print("日期格式错误,请输入 YYYY-MM-DD")

def add_task():

    title = input("请输入任务:")

    due_date = get_due_date()
    priority = get_priority()

    task = Task(title,priority,due_date)
    manager.add_task(task)
    manager.save()

    print("添加成功~")

def show_tasks():

    print("=====任务列表=====")

    if len(manager.tasks) == 0:
        print("暂无任务")
        return

    for i in range(len(manager.tasks)):
        task = manager.tasks[i]
        if task.completed:
            status = "√"
        else:
            status = " "

        print(f"[{status}] {i+1}.{task.title}[{task.priority}] [截止:{task.due_date}]")

def delete_task():
    try:
        show_tasks()

        if len(manager.tasks) == 0:
            return

        index = int(input("请输入要删除的任务编码:"))
        manager.delete_task(index-1)

        manager.save()

        print("删除成功~")

    except ValueError:
        print("请输入数字")

    except IndexError:
        print("任务不存在")

def complete_task():
    try:
        show_tasks()
        index = int(input("请输入已完成的任务编码:"))
        manager.complete_task(index-1)

        manager.save()

        print("操作成功~")
    except ValueError:
        print("请输入数字")
    except IndexError:
        print("任务不存在")

def edit_task():
    try:
        show_tasks()

        if not manager.tasks:
            return

        index = int(input("请输入你要修改的任务编号:"))
        title = input("请输入新的任务标题:")
        priority = get_priority()
        due_date = get_due_date()

        manager.edit_task(index-1,title,priority,due_date)

        print("修改成功~")

    except ValueError:
        print("请输入数字")
    except IndexError:
        print("任务不存在")

def search_task():
    keyword = input("请输入搜索关键词:")
    result = manager.search_tasks(keyword)

    print("=====搜索结果======")

    if not result:
        print("没有找到相关任务")
        return

    for i,task in enumerate(result):
        if task.completed:
            status = "√"
        else:
            status = " "

        print(f"[{status}] {i+1}.{task.title}[{task.priority}] [截止:{task.due_date}]")

def sort_tasks():
    manager.sort_tasks()
    manager.save()
    print("任务已按照优先级排序!")

def main():   
    while True:

        print("=====任务管理系统=====")
        print("1.添加任务")
        print("2.查看任务")
        print("3.删除任务")
        print("4.完成任务")
        print("5.修改任务")
        print("6.搜索任务")
        print("7.排序任务")
        print("8.退出")

        choice = input("请选择:")

        if choice == "1":
            add_task()

        elif choice == "2" :
            show_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            complete_task()

        elif choice == "5" :
            edit_task()

        elif choice == "6":
            search_task()

        elif choice == "7":
            sort_tasks()

        elif choice == "8" :
            print("成功退出~")
            manager.save()
            break
        
        else:
            print("输入异常,请重新输入~")

if __name__ == "__main__":
    main()