# 5.10

# current_users : list[str] = ["Adolf", "Benito", "Stalin", "Anna Frank", "Aldo Moro"]
# new_users : list[str] = ["Benito", "Camilla", "Luca", "Aldo Moro", "Thomas"]

# for i in current_users:
#     if i.lower() in new_users:
#         print(f"l'username scelto {i} già è in uso! Sceglierne un'altro.")


# 5.11

# position: list[int] = [1,2,3,4,5,6,7,8,9]

# for i in position:

#     if i == 1:
#         print(f"{i}st!")

#     elif i == 2:
#         print(f"{i}nd!")

#     elif i == 3:
#         print(f"{i}rd!")
    
#     else:
#         print(f"{i}th!")

# 6.1

# from typing import Any
# person: dict[str,Any] = {"firt_name" : "Luca", "last_name" : "D'Ambra", "age" : 21, "city" : "Ischia" }

# print(person)

#6.2

# favourite_number:dict[str, int] = {"Luca":21, "Matteo":69,"Bozzo":13,"Lollo":71,"Andrea":90}
# for i in favourite_number.items():
#     print(i)

#6.3

# from typing import Any

# glossary: dict[str,Any] = {"for": "Permette di ripetere un operazione n numero di volte",
#                             "while": "Permette di ripetere una condizione finchè vera",
#                             "lower": "converte una stringa in lowercase",
#                             "upper": "converte una stringa in uppercase",
#                             "if": "permette di controllare una o più variabili in un algoritmo"
#                            }

# for i in glossary.items():
#     print(i)


#6.7

# from typing import Any
# person: dict[str,Any] = {"firt_name" : "Luca", "last_name" : "D'Ambra", "age" : 21, "city" : "Ischia" }
# person2 : dict[str,Any] = {"firt_name" : "Matteo", "last_name" : "Argenti", "age" : 21, "city" : "Trullo"}
# person3 : dict[str,Any] = {"firt_name" : "Thomas", "last_name" : "Marchionni", "age" : 19, "city" : "Acilia"}

# people : list[str] = []

# people.append(person)
# people.append(person2)
# people.append(person3)

# for i in people:
#     print(i)