nome:str=str(input("Inserire Nome: "))
genere:str=str(input("Inserire il Genere:"))
match genere:
    case "m":
        print(f"{nome}, Maschio")
    case "f":
        print(f"{nome}, Femmina")
    case _:
        print("Impossibile generare un documento d'identità")
 