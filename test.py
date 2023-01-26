def check_try( temp_tries, help_tries, max_tries ):
    match temp_tries:
        case num if num in range( 1, help_tries ):
            print( "1-" + str( help_tries ) )
        case num if num in range( help_tries + 1, max_tries ):
            print( str( help_tries + 1 ) + "-" + str( max_tries ) )
        case other:
            print( "uups" )

ask_game = check_try( 2, 4, 9 )

ask_game