pizza_list : list[str] = ["Margherita" , "Marinara" , "Diavola"]
friend_pizzas:list[str]= ["Margherita" , "Marinara" , "Diavola"]
pizza_list.append ("Vegetariana")
friend_pizzas.append ("Pistacchiosa")

for i in pizza_list:
    print(f"le mie pizze preferite sono:\n {i}")
for i in friend_pizzas:
    print(f"Le pizze preferite del mio amico sono:\n {i}")
