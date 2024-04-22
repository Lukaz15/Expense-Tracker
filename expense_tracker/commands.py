import csv
import os
import inspect
import sys
import re


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
                print(f"${re.sub(r'[\[\]]', ''," - ".join(row))}")
            if os.path.exists('budget.txt'):
                    with open('budget.txt', mode='r') as file:
                        for line in file:
                            print(f"Your budget is ${line}")
    else:
        print('There are no saved expenses yet.')
                       
def cmd_write():
    while True:
        try:
            number = float(input('> Enter your expenses:  $'))
            break
        except:
            print('Please enter a valid number')
    while True:
        description = input('> Describe your expense:  ')
        if len(description) >= 50 or len(description) < 3:
            print('Out of range! Minimum 3 and maximum 50 characters')
        else: break
    data = {"expenses": number,"description": description} 
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data)
        writer.writerow(data)
    print('Expenses saved successfully.')

def cmd_clear():
    if os.path.exists('data.csv'):
        confirm = input('Are you sure you want to remove all your saved data? y / n ')
        match confirm:
            case "y":
                os.remove('data.csv')
                print('Cleared all saved data')
            case "n":
                print('Cancelled data clear')
            case _:
                print('Please use "y" to delete data or "n" to cancel')
    else:
        print("There's no data to clear")


def cmd_help():
    cmds = [cmd.replace("cmd_", "") for cmd in [name for name, obj in inspect.getmembers(sys.modules[__name__]) 
                if inspect.isfunction(obj) and name.startswith('cmd_')]]
    print(", ".join(cmds))

def cmd_exit():
    print('Exiting...')
    exit()