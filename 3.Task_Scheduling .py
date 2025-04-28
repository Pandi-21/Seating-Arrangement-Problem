# Problem:
# Given multiple tasks with a deadline and duration,
# find the maximum number of tasks that can be completed without missing deadlines.

# solution:
# - Sort tasks by deadline.
# - Try to complete tasks one by one.
# - Keep track of total time spent so far.
# - Only add a task if it can be finished before its deadline.

def tasks_(tasks):
    tasks.sort(key=lambda x: x['deadline'])  # Sort by deadline
    time_duration= 0
    completed_work= []
    
    for period in tasks:
        if time_duration + period['duration'] <= period['deadline']:
            completed_work.append(period['name'])
            time_duration += period['duration']
    
    return completed_work

# Example usage
tasks = [
    {'name': 'Task 1', 'deadline': 4, 'duration': 2},
    {'name': 'Task 2', 'deadline': 3, 'duration': 1},
    {'name': 'Task 3', 'deadline': 2, 'duration': 1},
    {'name': 'Task 4', 'deadline': 1, 'duration': 2},
]

final_output = tasks_(tasks)
print("Tasks that can be completed in period of time:", final_output)
