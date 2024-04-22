import expense_tracker.commands as cmd


while True:
    cmd = input('> Enter a cmd:  ').lower()
    match cmd:
        case "exit":
            cmd.cmd_exit()
        case "read":
            cmd.cmd_read()
        case "write":
            cmd.cmd_write()
        case "budget":
            cmd.cmd_budget()
        case "clear":
            cmd.cmd_clear()
        case "help":
            cmd.cmd_help()
        case _:
            print('Type "help" for a list of commands.')
