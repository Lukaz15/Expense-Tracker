import csv
import os
import inspect
import sys


# When defining new commands, the prefix "cmd_" should be used to ensure it gets listed into the "help" command.

def cmd_budget():
    while True:
        try:
            rem_budget = float(input('> Enter your budget:  '))
            break
        except:
            print('Please enter a valid number')
    with open('budget.txt', mode='w') as file:
        file.write(str(rem_budget))
    
def cmd_read():
    if os.path.exists('data.csv'):
        with open('data.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
            if os.path.exists('budget.txt'):
                    with open('budget.txt', mode='r') as file:
                        for line in file:
                            print(line)
                       
def cmd_save():
    while True:
        try:
            number = float(input('> Enter your expenses:  '))
            break
        except:
            print('Please enter a valid number')
    data = {"expenses": number,"description": input('> Describe them:  ')} 

    with open('data.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data)
        writer.writerow(data)

def cmd_clear():
    confirm = input('Are you sure you want to remove all your saved data? y / n ')
    match confirm:
        case "y":
            os.remove('data.csv')
            print('Cleared all saved data')
        case "n":
            print('Cancelled data clear')
        case _:
            print('Please use "y" to delete data or "n" to cancel')


def cmd_help():
    cmds = [cmd.replace("cmd_", "") for cmd in [name for name, obj in inspect.getmembers(sys.modules[__name__]) 
                if inspect.isfunction(obj) and name.startswith('cmd_')]]
    print(", ".join(cmds))
    


while True:
    cmd = input('> Enter a cmd:  ').lower()
    match cmd:
        case "exit":
            break
        case "read":
            cmd_read()
        case "save":
            cmd_save()
        case "budget":
            cmd_budget()
        case "clear":
            cmd_clear()
        case "help":
            cmd_help()
        case _:
            print('Type "help" for a list of commands.')
