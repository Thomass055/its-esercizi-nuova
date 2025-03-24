
# def rotate_left(lista, k):
#     if len(lista) == 0:
#         return lista
#     k = k % len(lista)
#     if k == 0:
#         return lista
#     for _ in range(k):
#         primo_elemento = lista.pop(0)
#         lista.append(primo_elemento)
#     return lista
# lista = [1, 2, 3, 4, 5]
# k = 2
# risultato = rotate_left(lista, k)
 

# def sum_above_threshold(numbers: list[int], threshold) -> int:
    
#     s=0
#     for i in numbers:
#         if  i>threshold:
#             s=s+i
#     return s


# def frequency_dict(list) -> dict:
#     frequency={}
#     for elements in list:
#         if elements in frequency:
#             frequency[elements] += 1
#         else:
#             frequency[elements] = 1
#     return frequency



# def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
#     if conditionA or (conditionB and conditionC):
#         return "Operazione permessa"
#     else:
#         return "Operazione negata"


# def list_statistics(list) -> int :
#     if len(list) == 0:
#         return "La lista è vuota"
    
#     massimo = max(list)
#     minimo = min(list)
#     media = sum(list) / len(list)
    
#     return massimo, minimo, media


# def remove_duplicates(elements:list[str,int]) -> list:
#     lista : list = (elements)
#     result = []
#     duplicates = set()
    
#     for elements in lista:
#         if elements not in duplicates:
#             result.append(elements)
#             duplicates.add(elements)
            
#     return result


# def unisci_dizionari(dict1, dict2):
    
#     risultato = dict1.copy()
    
#     for chiave, valore in dict2.items():
#         if chiave in risultato:
#             risultato[chiave] += valore
#         else:
#             risultato[chiave] = valore
            
#     return risultato