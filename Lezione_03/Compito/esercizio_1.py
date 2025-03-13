while True:
    parola:str = str(input("Inserisci una parola: "))
    if parola == "fine":
        break
    if parola[0] == parola[-1]:
        print("Messaggio corrispondente")