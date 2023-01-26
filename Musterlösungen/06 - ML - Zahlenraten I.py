# ML - Zahlenraten I
import random

# Methode zur Zufallszahlengeneration
def zufallszahl(start, ende):
    # Sollte der erste Wert größer als der zweite Wert sein, so werden die Werte vertauscht
    if start > ende:
        start, ende = ende, start
    return random.randint(start, ende)
    # Alternativ return random.randrange(start, ende+1)
    

# Methode zum Testen ob ein übergebener Text eine Zahl in einem bestimmten Bereich ist
def zahltesten(zahl, start, ende):
    # Test, ob es sich um eine Zahl handelt. Handelt es sich nicht um eine Zahl, so wird
    # False zurückgegeben.
    try:
        zahl = int(zahl)
    except ValueError:
            return False
            
    # Test, ob der Bereich passt
    return (start <= zahl) and (zahl <= ende)
    
    
# Methode zur Erhebung der Benutzereingabe inkl Überprüfung auf Gültigkeit der Zahl
def benutzereingabe(start, ende):
    ok = False
    
    while not(ok):
        zahl = input('\nBitte geben Sie eine Zahl im Bereich von ' + str(start) + ' bis ' + str(ende) + ' ein: ')
        
        # Prüfung der Zahl auf Gültigkeit
        ok = zahltesten(zahl, start, ende)
        
    # Zahl zurückgeben - Wichtig: Rückgabedatentyp muss 'int' sein
    return int(zahl)
    
    
# Spielmethode
def spiel(start, ende, max_versuche):
    # 1. Zufallszahl generieren
    zz = zufallszahl(start, ende)
    
    # Augabe der Zufallszahl zu Testzwecken
    # print('Die gesuchte Zahl lautet: ' + str(zz))
    
    # 2. Rateversuche protokollieren
    anzahl_versuche = 0
    
    # 3. Spielschleife für die Anzahl der Versuche
    while anzahl_versuche < max_versuche:
        # 4. Benutzer nach seiner Schätzung fragen
        bz = benutzereingabe(start, ende)
        
        # 5. Versuch zählen
        anzahl_versuche += 1
        
        # 6. Benutzerhinweis ausgeben - Testen, ob die Zahl richtig geraten war. Wenn nicht, entsprechenden Tipp ausgeben
        if bz < zz:
            print('Ihre Zahl ist KLEINER als die gesuchte Zahl.')
        elif bz > zz:
            print('Ihre Zahl ist GRÖSSER als die gesuchte Zahl.')
        else:
            print('Herzlichen Glückwunsch! Sie haben die gesuchte Zahl ' + str(zz) + ' in ' + str(anzahl_versuche) + ' Versuche(n) erraten.')
            break
    else:
        print('Ihre Versuche sind aufgebraucht. Sie haben die gesuchte Zahl ' + str(zz) + ' leider nicht erraten.')
    

# Spiel starten
START = 100
ENDE = 400
MAX_VERSUCHE = 9

neues_spiel = 'ja'

while neues_spiel == 'ja':
    spiel(START, ENDE, MAX_VERSUCHE)
    neues_spiel = input('\n------------\n\nIch möchte ein Spiel spielen - Sie auch?').lower()