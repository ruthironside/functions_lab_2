tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks(list):
    uncompleted = []
    for task in list:
        if task["completed"] == False:
            uncompleted.append(task) 

    return uncompleted

print(uncompleted_tasks(tasks))


def completed_tasks(list):
    completed = []
    for task in list:
        if task["completed"] == True:
            completed.append(task) 

    return completed

print(completed_tasks(tasks))


# def task_description(list):
#     task_descriptions = []
#     for task in list:
#         task_descriptions.append(task["description"]) 
    
#     return task_descriptions
            
# print(task_descriptions(tasks))


def get_tasks_longer_than(list, time):
    tasks = []
    for task in list:
        if task["time_taken"] > time:
            tasks.append(task)
    
    return tasks
            
print(get_tasks_longer_than(tasks, 20))


def get_task_by_description(list, description):
    for task in list:
        if task["description"] == description:
            return task
    return "task not found"

print(get_task_by_description(tasks, "Walk dog"))