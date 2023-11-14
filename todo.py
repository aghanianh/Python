uniq = 1
tasks = []

def add_task(desc, priv='low'):
    global uniq
    global tasks
    if not desc:
        raise ValueError("The description must be completed!!")
    task = {'ids': uniq, 'desc': desc, 'priv': priv, 'completed': False}
    tasks.append(task)
    print(f'Your Task with id: {task["ids"]}, description: {task["desc"]} and privilege: {task["priv"]} was successfully added to the To-Do list')
    uniq += 1

def remove_task(task_id):
    global tasks
    for task in tasks:
        if task['ids'] == task_id:
            tasks.remove(task)
            print(f"Task with id {task_id} removed successfully.")
            return
    print("Task not found.")

def list_tasks(is_completed=False):
    global tasks
    if not tasks:
        print("Empty to-do list")
        return

    if not is_completed:
        for task in tasks:
            if not task['completed']:
                print(f'Task id: {task["ids"]} Description: {task["desc"]}')
    else:
        for task in tasks:
            if task['completed']:
                print(f'Completed tasks: Task id: {task["ids"]} Description: {task["desc"]}')

def mark_completed(task_id):
    global tasks
    for task in tasks:
        if task['ids'] == task_id:
            print(f'Task with id: {task_id} marked as completed')
            task['completed'] = True
            return
    print(f'There is no task with id: {task_id}')

def list_tasks_with_priority():
    global tasks
    if not tasks:
        print('Task list is empty')
        return
    sorted_tasks = sorted(tasks, key=lambda x: x['priv'])
    for task in sorted_tasks:
        print(f"Task {task['ids']}: Description: {task['desc']} Priority: {task['priv']} Status: {'Completed' if task['completed'] else 'Not Completed'}")

# Example Usage:
add_task('buy something', priv='high')
add_task('finish Mark-Lutz book', priv='high')
add_task('swimming')
add_task('something')

list_tasks()

mark_completed(1)

list_tasks(is_completed=True)

list_tasks_with_priority()

remove_task(1)

list_tasks()
