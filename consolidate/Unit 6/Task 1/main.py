import functions
import time


# Show current date/time when the program starts
current_time = time.strftime('%B %d, %Y %H:%M:%S %p')
print("It is", current_time)


# Main loop: keeps asking the user for commands until they type "exit"
while True:
    user_action = input("\nType add, show, complete, or exit: ")
    user_action = user_action.strip()

    # ADD COMMAND - Add a new task
    if user_action.startswith('add'):
        todo = user_action[4:].strip()

        if todo == "":
            print("Please write a task after 'add'. Example: add go for walk")
            continue

        functions.add_task(todo)
        print("Task added.")
        
    # SHOW COMMAND - Display all tasks
    elif user_action.startswith('show'):
        functions.display_tasks()

    # COMPLETE COMMAND - Mark a task as completed
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            functions.mark_completed(number)
        except ValueError:
            print("Please use: complete NUMBER (example: complete 1)")
            continue
        except IndexError:
            print("That task number does not exist.")
            continue

    # EXIT COMMAND
    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid. Try: add/show/complete/exit")

print("Bye!")
