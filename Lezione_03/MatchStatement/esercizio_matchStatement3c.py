lista_ogetti:list[any]=[]
for i in range(0,3):
    oggetto:str=(input("inserisci l'oggetto: "))
    lista_ogetti.append(oggetto)

match lista_ogetti:
    case ["penna", "matita", "quaderno"]:
        print("Questo è materiale scolastico")
    case ["pane", "latte", "uova"]:
        print("Si tratta di prodotti alimentari")
    case["sedia", "tavolo", "armadio"]:
        print("Si tratta di mobili")
    case["telefono", "computer", "tablet"]:
        print("Si tratta di dispositivi elettronici")
    case _ :
        print("Categoria sconosciuta")
