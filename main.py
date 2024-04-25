import expense_tracker.commands as command

print('Welcome back! This is a simple expense tracker. Type "help" for a list of commands.')
while True:
    commands = input('> Enter a command:  ').lower()
    match commands:
        case "exit":
            command.cmd_exit()
        case "expenses":
            command.cmd_expenses()
        case "spend":
            command.cmd_spend()
        case "budget":
            command.cmd_budget()
        case "clear":
            command.cmd_clear()
        case "help":
            command.cmd_help()
        case _:
            print('Type "help" for a list of commands.')
