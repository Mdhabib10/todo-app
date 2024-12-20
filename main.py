from functions import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)
while(True):
    user_action = input("Type add, show, edit, complete or exit: --> ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") +" \n"

            todos = get_todos('todos.tx')
            todos.append(todo)
            write_todos('todos.tx', todos)


        case 'show':
            todos = get_todos('todos.tx')

            for index, item in enumerate(todos, start = 1):
                item = item.capitalize().strip('\n')
                print(f"{index}. {item}")
        case 'edit':
            try:
                number = int(input("Enter Number of the todo to edit: "))
                number -= 1
                todos = get_todos('todos.tx')
                new_todo = input("Enter new todo: ") +"\n"
                todos[number] = new_todo
                write_todos('todos.tx', todos)
            except ValueError:
                print("That is not valid command!")
            except IndexError:
                print("That number is not in the list")
                continue

        case 'complete':
            try:
                number = int(input("Enter number of the todo completed: "))
                todos = get_todos('todos.tx')
                todos.pop(number -1)
                write_todos('todos.tx', todos)
            except IndexError:
                print("There is no itme with that number!")
                continue

        case 'exit':
            break
        case _:
            print("That is a invalid command, please select one from the list below!")

print("Good bye!")



