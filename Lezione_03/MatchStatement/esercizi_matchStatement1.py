n:int = int(input("Inserisci il numero di neonati: "))
match n:
    case n if n == 0:
        print("Errore")
    case 1:
        print("Congratulazini!")
    case 2: 
        print("Wow!Gemelli")
    case 3:
        print("Wow!Tre")
    case 4:
        print("Mamma mia Quattro!Wow")
    case 5:
        print("Incredibile!Cinque")
    case n if n > 5:
        print(f"Non ci credo! {n} bambini!")
