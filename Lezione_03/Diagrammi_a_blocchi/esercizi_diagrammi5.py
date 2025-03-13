n:int = int (input(f" Inserisci numero: "))

if n % 1 == 0 and n > 0:
    somma:int = 0
    i = 0
    while i <= n:
        somma = (somma + (i *i))
        i += 1
    print (f" La somma è {somma}")
else:
    print (" Errore, n deve essere positivo")