import random

# Get user inputs
tasks = []
for i in range(12):
    task = input(f"Enter task {i+1}: ")
    tasks.append(task)

# Randomize the task list
random.shuffle(tasks)

# Create a list to track completed tasks
completed_tasks = [False] * len(tasks)

# Add random USD values to each task
task_values = [random.randint(1, 15) for i in range(len(tasks))]

# Keep track of the total USD value of completed tasks
total_value = 0

# Keep prompting the user to complete tasks until all are completed
while not all(completed_tasks):
    # Print the task list with checkboxes and USD values
    print("Task list:")
    for i, task in enumerate(tasks):
        checkbox = "[X]" if completed_tasks[i] else "[ ]"
        value = task_values[i] if completed_tasks[i] else 0
        print(f"{i+1}. {checkbox} {task} (${value})")
    
    # Prompt the user to select a task to complete
    task_number_str = input("Enter the number of the task you completed, or 00 to exit: ")
    
    if task_number_str == '00':
        break  # Exit the loop if the user enters 0
    
    # Check that the task number is valid
    try:
        task_number = int(task_number_str)
        if task_number < 1 or task_number > len(tasks):
            raise ValueError("Invalid task number.")
    except ValueError:
        print("Invalid input. Please try again.")
        continue
    
    # Mark the selected task as completed
    completed_tasks[task_number - 1] = True
    
    # Add the value of the completed task to the total value
    total_value += task_values[task_number - 1]
    
    # Print a message confirming the task completion and the updated total value
    print(f"Task {task_number} completed! Total value: ${total_value}")
    
# Print a message indicating that all tasks have been completed and the total value earned
print(f"Congratulations! You have completed all tasks. Total value earned: ${total_value}")
