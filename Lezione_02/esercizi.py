# print("Hello World")
# esercizio 1 lezione 1 diagrammi a blocchi

# import math

# a = float(input("inserire il valore dell'ipotenusa:"))
# b = float(input("inserire il valore del cateto: "))

# if a > b:
#     c: float = math.sqrt((a*a)-(b*b))
#     print(f"il cateto c vale {c}")

# else:
#     print("ERRORE")


#ESERCIZIO 2

# max:int = int(input("inserisci valore: "))
# cont:int = 1

# while cont<4:
#     cont += 1
#     n: int = int(input("inserisci valore: "))
    
# if n > max:
#      max= n

# print(f"questo è il valore maggiore: {max}") 
  
# ESERCIZIO 3

# somma: int = 0
# i = 1
# while i<=5:
#     n:int = int(input("inserisci i numeri da sommare: "))
#     if n> 0:
#         somma += n
#     i += 1
# print(f"la somma tra i numeri inseriti è {somma}")

# ESERCIZIO 4

# n:int = int(input("inserisci un numero: "))

# if n%2 ==  0:
#     print("il numero è pari: ")

# else:
#     print("il numero è dispari: ")

# ESERCIZIO 5

# n:int = int(input("inserisci un numero: "))
# div:int = 0

# if n<2:
#     print("il numero non è pari")

# else:
#     div = 2

# while div<n:
#      if n % div == 0:
#         print("il numero non è primo")
#         break
#      else:
#          div += 1

# else:
#     print("il numero è primo")

# ESERCIZIO 6

# n:int = int(input("inserisci un numero: "))

# if n>0:
#     fattoriale = 1
#     i = 1
#     while i <= n:
#         fattoriale = fattoriale *  i
#         i = i + 1
#     print(f"il fattoriale del numero inserito è: {fattoriale}")

# else:  
#     print("il numero non è positivo")

# ESERCIZIO 7

# pari: int = 0
# dispari: int = 0
# i = 1

# while i <= 10:
#     n: int = int(input("inserisci un numero: "))
#     i = i + 1
#     if n%2 == 0:
#         pari = pari + 1
#     else:
#         dispari = dispari + 1
      
# print(f"dispari: {dispari}")
# print(f"pari: {pari}")

#ESERCIZIO 8

# soglia: int = int(input("inserisci valori: "))
# i = 1

# while i <=7:
#     n: int = int(input("inserisci un valore: "))
    

#     if n > soglia:
#         print(f"il valore è: {n}")
#     i = i + 1

# ESERCIZIO 9

# nome : str = input("inserire il nome: ")
# vendite : int = int(input("inserire il valore: ")) 
# max_nome:str =nome
# max:int = vendite
# min_nome:str = nome

# min:int = vendite
# i = 0

# while i != 4:
#     new_nome: str = input("inserisci nuovo nome: ")
#     new_vendite: int = int(input("inserisci nuovo valore: "))
#     i = i+1 

#    if new_vendite > max:
#         max_nome = new_nome
#         max = new_vendite
    
#         if new_vendite < min :
#             min_nome = new_nome
#             min = new_vendite

# print(f"questo è il massimo: {max_nome} , {max}")
# print(f"questo è il minimo: {min_nome} , {min}")

# ESERCIZIO 10

# reddito : int = int(input("inserisci il reddito: "))
# media: int = int(input("inserisci media: "))

# if reddito < 20000 and media >27: 
#     print("borsa di studio approvata")

# else:
#     print("borsa di studio rifiutata")

#ESERCIZIO 11   

# liberi = 20

# while True:
#     opzioni:str = input("inserisci opzioni: ")

#     if opzioni == "prenota":
#         if liberi>0:
#             liberi -= 1

#         else:
#             print("non ci sono postidisponibili.")
#     elif opzioni == "libera":
#         if liberi < 20:
#             liberi += 1
#             print("tutti i posti sono gia disponibili")
    
#     elif opzioni == "visualizza":
#         print(liberi)
#         print( 20 - liberi)

#     elif opzioni == "esci":
#         break
    
#     else:
#         print("errore,inserire una delle opzioni disponibili")

# ESERCIZI DIAGRAMMI A BLOCCHI SECONDA SCHEDA

# ESERCIZIO 1

#posti_max:int= int(input("inserisci numero massimo di posti: "))
# posti_liberi = posti_max

# while True:
#     opzioni:str = input("inserisci opzioni: ")

#     if opzioni =="ingresso":
#         if posti_liberi>0:
#             posti_liberi -= 1

#         else:
#             print("il parcheggio è pieno:")

#     elif opzioni == "uscita":
#         if posti_liberi<posti_max:
#             posti_liberi += 1
   
#         else:
#             print("il parcheggio è gia vuoto")


#     elif opzioni == "stato":
#         print(posti_liberi)
#         print(posti_max - posti_liberi)

#     elif opzioni =="esci":
#         break

#     else:
#         print("errore,selezionare una scelta")

 # ESERCIZIO  3


# nome_corso:str = input("inserire il nome: ")
# max_posti:int = 100

# while True:
#     opzione:str = input("inserisci opzione: ")    
#     if opzione == "iscrivi":
#         if max_posti > 0:
#             max_posti -=1

#         else:
#             print("non ci sono posti disponibili: ")

#     elif opzione == "annulla":
#         if max_posti < 100:
#             max_posti += 1

#         else:
#             print("tutti i posti sono gia disdponibili: ")

#     elif opzione == "visualizza":
#         print(max_posti)
#         print(100 - max_posti)

#     elif opzione == "elimina":
#         nome_corso: str = input("inserire il nome: ")

#     elif opzione == "esci":
#         break