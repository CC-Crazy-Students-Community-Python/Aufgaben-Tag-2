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
end_range = 401
os.system( "cls" )

#
# start game
def game( start_range, end_range ):
    max_tries = 9
    rnd_num = random.randint( start_range, end_range )

    while max_tries != 0:
        print( "Debug: " + str( rnd_num ) + "\n" )
        users_input = input( "Bitte geben Sie eine Zahl zwischen " + str( start_range ) + " und " + str( end_range ) + " ein:" ).lower()
        match users_input:
            case num if ( num.isdigit() and int( num ) in range( start_range, end_range ) ):
                num = int( num )
                match num:
                    case num if num == rnd_num:
                        os.system( "cls" )
                        print( str( num ) + " ist die gesuchte Nummer\n Du hast gewonnen :-)\n" )
                        play_again = input( "Wollen Sie noch einmal spielen? [ j/n | y/n ]" ).lower()
                        match play_again:
                            case "y" | "yes" | "j" | "ja":
                                os.system( "cls" )
                                game( start_range, end_range )
                                break
                            case other:
                                os.system( "cls" )
                                print( "Danke, Das Spiel wird beendet\n" )
                        break
                    case num if num < rnd_num:
                        max_tries -= 1
                        os.system( "cls" )
                        print( str( num ) + " ist kleiner als die gesuchte Zahl\nDu hast noch " + str( max_tries ) + " Versuche\n" )
                        continue
                    case num if num > rnd_num:
                        max_tries -= 1
                        os.system( "cls" )
                        print( str( num ) + " ist größer als die gesuchte Zahl\nDu hast noch " + str( max_tries ) + " Versuche\n" )
                        continue
            case "stop" | "quit" | "end" | "ende" | "aus" | "beenden":
                os.system( "cls" )
                print( "Danke, Das Spiel wird beendet\n" )
                break
            case other:
                os.system( "cls" )
                continue
    else:
        os.system( "cls" )
        print( "Alle Versuche aufgebraucht\nSie haben verloren :-)\n" )
        play_again = input( "Wollen Sie noch einmal spielen? [ j/n | y/n ]" ).lower()
        match play_again:
            case "y" | "yes" | "j" | "ja":
                os.system( "cls" )
                game( start_range, end_range )
            case other:
                os.system( "cls" )
                print( "Danke, Das Spiel wird beendet\n" )

game( start_range, end_range )