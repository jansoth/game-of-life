import os
import time
import copy
import random

"""
alte (umständliche) Art Startformationen zu erstellen - deswegen auskommentiert
# 
# zu beginn alle Zellen tot
# Zeilen / Spaltennummerierung fängt bei 0 an!
# äußeren Elemente sind immer tot

anzahl_zeilen = 7
anzahl_spalten = 15

gitter = []
for zeilen_nummer in range(0,anzahl_zeilen):
    gitter.append([' ']*anzahl_spalten)         # erzeugt ein array mit anzahl_spalten einträgen 
    
# Startkonstellation herstellen
for zeilen_nummer in range(2,5):
    gitter[zeilen_nummer][2] = 'x'

for spalten_nummer in range(8,11):
    gitter[3][spalten_nummer] = 'x'
"""

# neue einfachere möglichkeit Startwelten zu erzeugen
gitter1= [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ','x',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' '],\
          [' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

gitter2= [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ','x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' '],\
          [' ',' ','x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' '],\
          [' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

# Gleiter
gitter3= [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

# Light-Weight Spaceship
gitter4= [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ','x','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ','x',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ','x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],\
          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]


# Random-Gitter
def erzeuge_random_gitter(anzahl_zeilen:int, anzahl_spalten:int) -> list:
    """Erzeugt ein zufaellig erzeugtes Gitter.

    Args:
        anzahl_zeilen (int): Bestimmt die Anzahl der Zeilen des Gitters
        anzahl_spalten (int): Bestimmt die Anzahl der Spalten des Gitters

    Returns:
        list: zufaellig erzeugtes Gitter
    """

    # leeres Gitter erzeugen
    gitter = []
    for zeilen_nummer in range(0,anzahl_zeilen):
        gitter.append([' ']*anzahl_spalten)

    # Gitter mit zufallszellen füllen
    for zeilen_nummer in range(0, anzahl_zeilen):
        for spalten_nummer in range(0, anzahl_spalten):
            if 0 == random.randint(0, 1):
                gitter[zeilen_nummer][spalten_nummer] = ' '
            else:
                gitter[zeilen_nummer][spalten_nummer] = 'x'

    return gitter

anzahl_zeilen = 20
anzahl_spalten = 30
random_gitter = erzeuge_random_gitter(anzahl_zeilen, anzahl_spalten)



def anzahl_lebende_nachbarn(zeilen_nummer_input:int, spalten_nummer_input:int, gitter_input: list) -> int:
    """Gibt die Anzahl der lebenden Nachbarn zurück.

    Randzellen müssen nicht abgefangen werden, weil diese per Definition immer tot sind.
    An anderer Stelle im Programm wird sichergestellt, dass keine Randzellen überprüft werden

    Args:
        zeilen_nummer_input (int): Zeilennummer der zu prüfenden Zelle
        spalten_nummer_input (int): Spaltennummer der zu prüfenden Zelle
        gitter_input (list): Gitter das überprüft wird

    Returns:
        int: Anzahl der lebenden Nachbarn
    """
    rueckgabe_anzahl = 0

    # zeile über aktueller Zelle überprüfen
    for spalten_nummer in range(spalten_nummer_input-1, spalten_nummer_input+2):
        if gitter_input[zeilen_nummer_input-1][spalten_nummer] == 'x':
            rueckgabe_anzahl += 1    
    
    # nachbern links und rechts der aktuellen Zelle checken (step=2)
    for spalten_nummer in range(spalten_nummer_input-1, spalten_nummer_input+2, 2):
        if gitter_input[zeilen_nummer_input][spalten_nummer] == 'x':
            rueckgabe_anzahl += 1
    
    # zeile unter aktueller Zelle überprüfen
    for spalten_nummer in range(spalten_nummer_input-1, spalten_nummer_input+2):
        if gitter_input[zeilen_nummer_input+1][spalten_nummer] == 'x':
            rueckgabe_anzahl += 1
    
    return rueckgabe_anzahl


def naechste_generation(gitter_input: list) -> list:
    """Berechnet die nächste Generation des Gitters.

    Args:
        gitter_input (list): Gitter mit der aktuellen Generation

    Returns:
        list: Gitter mit der nächsten Generation
    """
    alte_welt = copy.deepcopy(gitter_input)
    neue_welt = copy.deepcopy(gitter_input)

    # über alte welt iterieren. äußere Elemte auslassen, weil per Definition immer Tot
    index_letzte_zeile = len(gitter_input)-1
    index_letzte_spalte = len(gitter_input[0])-1
    for zeilen_nummer in range(1, index_letzte_zeile):
        for spalten_nummer in range(1, index_letzte_spalte):
            lebende_nachbarn = anzahl_lebende_nachbarn(zeilen_nummer, spalten_nummer, alte_welt)
            if alte_welt[zeilen_nummer][spalten_nummer] == ' ':             #tote zelle
                if lebende_nachbarn == 3:
                    neue_welt[zeilen_nummer][spalten_nummer] = 'x'
            else:                                                           #lebende zelle
                if not (lebende_nachbarn == 2 or lebende_nachbarn == 3):
                    neue_welt[zeilen_nummer][spalten_nummer] = ' '          #zelle stirbt

    return neue_welt
    

def gitter_malen(gitter: list):
    """Zeichnet das Gitter im Terminal.

    Args:
        gitter (list): Das zu zeichnende Gitter wird übergeben
    """

    anzahl_spalten = len(gitter[0])
    # Rand oben zeichnen
    print("--" * (anzahl_spalten + 1))

    for zeile in gitter:
        # jede Zeile in einen String umwandeln
        # dafür jeden Eintrag der Zeile (entspricht Spalte) dem String hinzufügen
        zeilenstring = ''
        for element in zeile:
            zeilenstring += element+' '
        print("|" + zeilenstring + "|") 

    # Rand unten zeichnen
    print("--" * (anzahl_spalten + 1))


# ab hier Hauptprogramm
def game_of_life(gitter_input:list, anzahl_durchlaeufe: int):
    """Hauptprogramm.

    Args:
        gitter_input (list): Das Gitter welches genutzt werden soll
        anzahl_durchlaeufe (int): Anzahl Durchläufe für das Spiel
    """
    aktuelles_gitter = gitter_input
    gitter_malen(aktuelles_gitter)
    for i in range(anzahl_durchlaeufe):
        time.sleep(0.5)
        aktuelles_gitter = naechste_generation(aktuelles_gitter)
        os.system("clear")  # für linux
        # os.system("cls")  # für windows
        gitter_malen(aktuelles_gitter)


# Los gehts!!
anzahl_durchlaeufe = 25
game_of_life(random_gitter, anzahl_durchlaeufe)
