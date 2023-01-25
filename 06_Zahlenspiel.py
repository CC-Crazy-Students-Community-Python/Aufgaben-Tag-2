# Spiel Aufgabe

# import libs
import random
import os

# set vars
s = 100
e = 400
t = 9
r = t - 4

# clearing the output
def clear():
    os.system( "cls" )

# set random nnuber
def random_number( s, e ):
    return random.randint( s, e )

# get users input between the correct range
def users_input( s, e ):
    return input( "\nBitte geben Sie eine Zahl zwischen " + str( s ) + " und " + str( e ) + " ein:" )

# wrong_out
def wrong_out( a, x, y ):
    print( "Zahl ist nicht richtig, Sie liegen " + int( abs( x - y ) ) + " daneben" )
    print( "Sie haben noch " + str( a ) + " Versuche" )

# try again
def try_again( s, e, t, r ):
    c = input( "Wollen Sie nocheinmal spielen? [ j/n | y/n ]" )
    if c == "y" or c == "yes" or c == "j" or c == "ja":
        start_game( s, e, t, r )
    else:
        clear()
        print( "Danke, Das Spiel wird beendet\n" )

# start the game
def start_game( s, e, t, r ):
    # get informations
    clear()
    print( "In diesem Spiel wird eine zufällige Zahl generiert zwischen " + str( s ) + " und " + str( s ) + "." )
    print( "Sie als Spieler müssen eine Zahl wählen und haben " + str( t ) + " Versuche, um die richtige Zahl zu erraten." )
    print( "Als Hinweis bekommen Sie nach jeder Zahl gesagt, ob Sie nah dran sind oder nicht." )
    print( "Als Erleichterung bekommen Sie ab dem " + str( r ) + ". Versuch auch gesagt, ob Sie über oder unter der Zahl liegen." )
    print( "\nAlso viel Spass am Spielen." )

    # get random number
    x = random_number( s, e )
    print( x )

    # set tries as a
    a = t

    # loop for tries and answers
    while True:
        y = users_input( s, e )

        # check if input is int or char
        if y.isdigit():
            y = int( y )
        else:
            if y == "hilfe" or y == "help" or y == "?" or y == "??" or y == "/?":
                start_game( s, e, a, r )
            elif y == "stop" or y == "quit" or y == "aus" or y == "/Q" or y == "exit":
                clear()
                print( "Danke, Das Spiel wird beendet" )
                break
            else:
                continue

        # if no other tries left
        if a == 0:
            clear()
            print( "Leider keine Versuche mehr.\nDas Spiel wird beendet" )
            try_again( s, e, t, r )
            break
        # if only (tries - 4) tries left
        elif a <= r:
            # if number is inbetween the range
            if int( y ) and int( y ) < s or int( y ) > e:
                continue
            # if number does not fits the random number
            if y != x:
                clear()
                print( "Weiter viel Spass am Spielen.\nDebug: " + str( x ) + "\n" )
                print( "Zahl ist nicht richtig, Sie liegen " + str( abs( x - y ) ) + " daneben" )
                print( "Sie haben noch " + str( a ) + " Versuche" )
                a -= 1
                continue
            # if number fits the random number
            else:
                print( "Bravo, Sie haben die Zahl " + str( x ) + " erraten" )
                try_again( s, e, t, r )
                break
        # normal state, until only (tries - 4) tries left
        else:
            # if number is inbetween the range
            if int( y ) and int( y ) < s or int( y ) > e:
                continue
            # if number is +/- 50
            if y != x and abs( x - y ) > 50:
                clear()
                print( "Weiter viel Spass am Spielen.\nDebug: " + str( x ) + "\n" )
                print( "Zahl ist nicht richtig, Sie liegen aber auch nicht nah dran" )
                print( "Sie haben noch " + str( a ) + " Versuche" )
                a -= 1
                continue
            # if number is between +/- 20 and +/- 50
            elif y != x and abs( x - y ) < 50 and abs( x - y ) > 20:
                clear()
                print( "Weiter viel Spass am Spielen.\nDebug: " + str( x ) + "\n" )
                print( "Zahl ist nicht richtig, sind aber schon recht nah dran" )
                print( "Sie haben noch " + str( a ) + " Versuche" )
                a -= 1
                continue
            # if number is +/- 10
            elif y != x and abs( x - y ) < 20:
                clear()
                print( "Weiter viel Spass am Spielen.\nDebug: " + str( x ) + "\n" )
                print( "Zahl ist nicht richtig, sind aber sehr nah dran" )
                print( "Sie haben noch " + str( a ) + " Versuche" )
                a -= 1
                continue
            # if number fits the random number
            elif y == x:
                clear()
                print( "Bravo, Sie haben die Zahl " + str( x ) + " erraten" )
                try_again( s, e, t, r )
                break
        break

start_game( s, e, t, r)
