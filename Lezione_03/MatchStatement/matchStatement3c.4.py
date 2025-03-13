mammiferi:list[str]=["cane", "gatto", "cavallo", "elefante","leone" ]
rettili:list[str]=["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list[str]=["aquila", "pappagallo", "gufo", "falco"]
pesci:list[str]=["squalo", "trota", "salmone", "carpa"]
animale:str=(input("inserisci l'animale: "))

match animale:
    case animale if animale in mammiferi:
        print(f"{animale} è un mammifero")
    case animale if animale in rettili:
        print(f"{animale} è un rettile")
    case animale if animale in uccelli:
        print(f"{animale} è un'uccello")
    case animale if animale in pesci:
        print(f"{animale} Fa parte della categoria dei pesci")
    case _ :
        print("Il programma non è in grado di classificare l'animale inserito")
