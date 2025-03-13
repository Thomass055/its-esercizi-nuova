giorno:int=int(input("inserisci il giorno: "))
mese:int=int(input("inserisci il mese: "))

data:tuple=(giorno,mese)

match data:
    case (1,1):
        print("capodanno")
    case(14,2):
        print("San Valentino")
    case(_ ,6):
        print("Festa della Repubblica Italiana")
    case (15,8):
        print("Ferragosto")
    case(31,10):
        print("Halloween")
    case(25,12):
        print("Natale")
    case _:
        print("Nessuna festività importante in questa data.")