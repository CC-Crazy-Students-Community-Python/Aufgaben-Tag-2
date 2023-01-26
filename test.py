def check_input( input_value ):
    if input_value.isdigit():
        return int( input_value )
    else:
        input_value = input_value.lower()
        match input_value:
            case "hilfe" | "help" | "h" | "?" | "??" | "/?":
                return 0
            case "stop" | "halt" | "quit" | "exit" | "aus" | "/q":
                return 1
        return 2
print( check_input( 1 ) )