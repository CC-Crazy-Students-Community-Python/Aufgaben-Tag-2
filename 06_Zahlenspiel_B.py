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
def check_input( user_num ):
    if user_num.isdigit():
        return int( user_num )
    else:
        user_num = user_num.lower()
        match user_num:
            case "hilfe" | "help" | "h" | "?" | "??" | "/?":
                return 0
            case "stop" | "halt" | "quit" | "exit" | "aus" | "/q":
                return 1
        return 2

#
# check the tries
def check_try( temp_tries ):

    return False

#
# set help text
def help_text():
    clear()
    print( "In diesem Spiel wird eine zufällige Zahl generiert zwischen " + str( start_range ) + " und " + str( end_range ) + "." )
    print( "Sie als Spieler müssen eine Zahl wählen und haben " + str( max_tries ) + " Versuche, um die richtige Zahl zu erraten." )
    print( "Als Hinweis bekommen Sie nach jeder Zahl gesagt, ob Sie über oder unter der Zahl liegen." )
    print( "Als Erleichterung bekommen Sie ab dem " + str( help_tries ) + ". Versuch auch gesagm, wie weit Sie neben der Zahl liegen." )
    print( "\nAlso viel Spass am Spielen.\n" )

#
# output if wrong numbers
def wrong_out_default( a, random_num, user_num ):
    clear()
    print( "\nWeiter viel Spass am Spielen.\nDebug: " + str( random_num ) + "\n" )
    print( "Zahl ist nicht richtig, Sie liegen " + ( "darüber" if random_num < user_num else "darunter" ) )
    print( "Sie haben noch " + str( a ) + " Versuche" )

def wrong_out_with_help( a, random_num, user_num ):
    clear()
    print( "\nWeiter viel Spass am Spielen.\nDebug: " + str( random_num ) + "\n" )
    print( "Zahl ist nicht richtig, Sie liegen " + str( abs( random_num - user_num ) ) + " daneben" )
    print( "Sie haben noch " + str( a ) + " Versuche" )

#
# output if right numbers
def right_out( random_num ):
    clear()
    print( "\nBravo, Sie haben die Zahl " + str( random_num ) + " erraten" )

#
# output if no tries left
def tries_out( tmp_tries ):
    clear()
    print( "\nLeider keine Versuche mehr.\nDas Spiel wird beendet" )

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
    help_text()

    #
    # get random number
    random_num = random_number( start_range, end_range )
    print( "Debug: " + str( random_num ) + "\n" )

    #
    # set tries as temporary
    tmp_tries = max_tries

    #
    # loop for tries and answers
    while True:
        # user input
        user_num = users_input( start_range, end_range )

        # check user input
        check_input( user_num )

        # check tries
        tries_out( tmp_tries )
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
