import os
import inspect
import sys
import json

DIR = os.path.expanduser('~/Documents/Expense Tracker')
SAVE_PATH = os.path.join(DIR, 'data.json')
BUDGET_PATH = os.path.join(DIR,'budget.txt')
if not os.path.exists(DIR): os.makedirs(DIR)

def cmd_budget():
    while True:
        try:
            rem_budget = float(input('> Enter your budget:  $'))
            break
        except:
            print('Please enter a valid number')
    with open(BUDGET_PATH, mode='w') as file:
        file.write(str(rem_budget))
    
def cmd_expenses():
    if os.path.exists(SAVE_PATH):
        with open(SAVE_PATH, mode='r') as file:
            expenses = json.load(file)
            for expense in expenses:
                print(f'${expense["expenses"]} - {expense["description"]}')
            if os.path.exists(BUDGET_PATH):
                    with open(BUDGET_PATH, mode='r') as file:
                        for line in file:
                            total_expense = float(line) - sum(float(expense['expenses']) for expense in expenses)
                            print(f"Your remaining budget would be of ${total_expense}")
    else:
        print('There are no saved expenses yet.')
                       
def cmd_spend():
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
    if os.path.exists(SAVE_PATH) and os.path.getsize(SAVE_PATH) > 0:
        with open(SAVE_PATH, mode='r') as file:
            data_list = json.load(file)
    else: data_list = []
    data_list.append(data)
    with open(SAVE_PATH, 'w') as file:
        json.dump(data_list, file, indent=4)

def cmd_clear():
    if os.path.exists(SAVE_PATH):
        confirm = input('> Are you sure you want to remove all your saved data? y/n ')
        match confirm:
            case "y":
                os.remove(SAVE_PATH)
                print('Cleared all saved data')
            case "n":
                print('Cancelled data clear')
            case _:
                print('Please use "y" to delete data or "n" to cancel')
    else:
        print('There is no data to clear')


def cmd_help():
    cmds = [cmd.replace("cmd_", "") for cmd in [name for name, obj in inspect.getmembers(sys.modules[__name__]) 
                if inspect.isfunction(obj)]]
    print(", ".join(cmds))

def cmd_exit():
    print('Exiting...')
    sys.exit()