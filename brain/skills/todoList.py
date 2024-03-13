""" This file Desiciption can be found in the comment below """
# Author: Marissa Langham
# Date: 03/13/2023
# Description: Todo list skill file for Ellie
# File Name: todoList.py

todoList = []

def addTodoItem(item, priority):
    """Adds an item with a priority level to the to-do list."""
    todoList.append((item, priority))
    return f"Added '{item}' with priority level {priority} to the to-do list."

def removeTodoItem(item):
    """Removes an item from the to-do list if it exists."""
    for todo in todoList[:]:  # Iterate over a copy of the list
        if todo[0] == item:
            todoList.remove(todo)
            return f"Removed '{item}' from the to-do list."
    return f"Item '{item}' not found in the to-do list."

def displayTodoList():
    """Returns a string representation of the to-do list."""
    if not todoList:
        return "Your to-do list is empty."
    todoListStr = "Here's your to-do list:\n"
    for item in todoList:
        todoListStr += f"- {item[0]} (Priority {item[1]})\n"
    return todoListStr.strip()  # Remove the trailing newline character