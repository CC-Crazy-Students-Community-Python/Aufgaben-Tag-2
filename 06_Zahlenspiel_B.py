#
# Spiel Aufgabe
#

#
# import libs
import random
import os

#
# set vars
start_range = 100
end_range = 400
max_tries = 9
help_tries = max_tries - 5

#
# clearing the output
def clear():
    os.system( "cls" )

#
# set random nnuber
def random_number( start_range, end_range ):
    return random.randint( start_range, end_range )

#
# get users input between the correct range
def users_input( start_range, end_range ):
    return input( "\nBitte geben Sie eine Zahl zwischen " + str( start_range ) + " und " + str( end_range ) + " ein:" )

#
# check users input for int or char
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
print( check_input( "stop" ) )
#
# set help text
def help_text():
    clear()
    print( "In diesem Spiel wird eine zufällige Zahl generiert zwischen " + str( start_range ) + " und " + str( end_range ) + "." )
    print( "Sie als Spieler müssen eine Zahl wählen und haben " + str( max_tries ) + " Versuche, um die richtige Zahl zu erraten." )
    print( "Als Hinweis bekommen Sie nach jeder Zahl gesagmax_tries, ob Sie nah dran sind oder nicht." )
    print( "Als Erleichterung bekommen Sie ab dem " + str( help_tries ) + ". Versuch auch gesagmax_tries, ob Sie über oder unter der Zahl liegen." )
    print( "\nAlso viel Spass am Spielen." )
    start_a_game( start_range, end_range, max_tries, help_tries )

#
# output if wrong numbers
def wrong_out_1( a, x, y ):
    clear()
    print( "Weiter viel Spass am Spielen.\nDebug: " + str( x ) + "\n" )
    print( "Zahl ist nicht richtig, Sie liegen " + str( abs( x - y ) ) + " daneben" )
    print( "Sie haben noch " + str( a ) + " Versuche" )

def wrong_out_2( a, x, y ):
    clear()
    print( "Weiter viel Spass am Spielen.\nDebug: " + str( x ) + "\n" )
    print( "Zahl ist nicht richtig, Sie liegen " + ( "darüber" if x < y else "darunter" ) )
    print( "Sie haben noch " + str( a ) + " Versuche" )

#
# check the tries
def check_try():
    return False

#
# start a new game
def start_a_game( start_range, end_range, max_tries, help_tries ):
    c = input( "Wollen Sie das Spiel spielen? [ j/n | y/n ]" )
    if c == "y" or c == "yes" or c == "j" or c == "ja":
        start_game( start_range, end_range, max_tries, help_tries )
    else:
        clear()
        print( "Danke, Das Spiel wird beendet\n" )

#####do while schleife mit try again als gamestart
# try again
def try_again( start_range, end_range, max_tries, help_tries ):
    c = input( "Wollen Sie nocheinmal spielen? [ j/n | y/n ]" )
    if c == "y" or c == "yes" or c == "j" or c == "ja":
        start_game( start_range, end_range, max_tries, help_tries )
    else:
        clear()
        print( "Danke, Das Spiel wird beendet\n" )

#
# start the game
def start_game( start_range, end_range, max_tries, help_tries ):
    #
    # get informations
    clear()
    print( "In diesem Spiel wird eine zufällige Zahl generiert zwischen " + str( s ) + " und " + str( s ) + "." )
    print( "Sie als Spieler müssen eine Zahl wählen und haben " + str( t ) + " Versuche, um die richtige Zahl zu erraten." )
    print( "Als Hinweis bekommen Sie nach jeder Zahl gesagmax_tries, ob Sie nah dran sind oder nicht." )
    print( "Als Erleichterung bekommen Sie ab dem " + str( r ) + ". Versuch auch gesagmax_tries, ob Sie über oder unter der Zahl liegen." )
    print( "\nAlso viel Spass am Spielen." )

    #
    # get random number
    x = random_number( start_range, end_range )
    print( "Debug: " + str( x ) + "\n" )

    #
    # set tries as a
    a = t

    #
    # loop for tries and answers
    while True:
        y = users_input( start_range, end_range )

        #
        # check if input is int or char
        # ##### KLEIN SCHREIBWEISE für befehle
       # check_input( start_range, end_range, a, help_tries )
        if y.isdigit():
            y = int( y )
        else:
            if y == "hilfe" or y == "help" or y == "?" or y == "??" or y == "/?":
                start_game( start_range, end_range, a, help_tries )
            elif y == "stop" or y == "quit" or y == "aus" or y == "/Q" or y == "exit":
                clear()
                print( "Danke, Das Spiel wird beendet" )
                break
            else:
                continue

        #
        # if no other tries left
        if a == 0:
            clear()
            print( "Leider keine Versuche mehr.\nDas Spiel wird beendet" )
            try_again( start_range, end_range, max_tries, help_tries )
            break
        # if only (tries - 4) tries left
        else:
            # if number is inbetween the range
            if int( y ) and int( y ) < s or int( y ) > e:
                continue
            # if number does not fits the random number
            if y != x:
                if a <= r:
                    wrong_out_1( a, x, y )
                else:
                    wrong_out_2( a, x, y )
                a -= 1
                continue
            # if number fits the random number
            else:
                clear()
                print( "Bravo, Sie haben die Zahl " + str( x ) + " erraten" )
                try_again( start_range, end_range, max_tries, help_tries )
                break
        break
#
# start the game
start_game( start_range, end_range, max_tries, help_tries)
