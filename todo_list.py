import json

todo = []
def add_todo(name, completion = False):
    todo.append({'title':name, 'completed':False})
    with open('todo.txt', 'w') as todoJSON:
        json.dump(todo, todoJSON)
    print('Todo "' + name + '" has been added.')
 
def print_todo():
    print('Todo List:')
    for item in todo:
            if item['completed']:
                index = todo.index(item)
                print('  ☑ ' + str(index) + '. ' + item['title'])
            else:
                index = todo.index(item)
                print('  ☐ ' + str(index) + '. ' + item['title'])

def complete_todo(index):
    complete_item = todo[index]
    complete_item['completed'] = True
    with open('todo.txt', 'w') as todoJSON:
        json.dump(todo, todoJSON)
    print('Todo "' + complete_item['title'] + '" has been completed.')

# def save_to_json():
#     with open('todo.txt', 'w') as todoJSON:
#         json.dump(todo, todoJSON)

