cars:str= input ("inserisci modello macchina: ")
predict : bool

if cars == "Audi":
    predict= True
    print(f"{cars} == macchina? {predict}")
elif cars == "Bmw":
    predict= True
    print(f"{cars} ==  macchina? {predict}")
elif cars == "Ferrari":
    predict= True
    print(f"{cars} ==  macchina? {predict}")
elif cars == "Lamborghini":
    predict= True
    print(f"{cars} ==  macchina? {predict}")
elif cars == "Maserati":
    predict= True
    print(f"{cars} ==  macchina? {predict}")
elif cars == "Yamaha":
    predict= False
    print(f"{cars} ==  macchina? {predict}")
elif cars == "Kawasaki":
    predict= False
    print(f"{cars} ==  macchina? {predict}")
elif cars == "Aprilia":
    predict= False
    print(f"{cars} ==  macchina? {predict}")
elif cars == "Ducati":
    predict= False
    print(f"{cars} ==  macchina? {predict}")
elif cars == "Ktm":
    predict= False
    print(f"{cars} ==  macchina? {predict}")
else:
    print("La macchina che hai inserito non è nell'elenco")