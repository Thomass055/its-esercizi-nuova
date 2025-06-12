def sum_primary_diagonal(matrix):
  
    n = len(matrix)
    somma = 0
    for i in range(n):
        somma += matrix[i][i]
    return somma

def sum_secondary_diagonal(matrix):
  
    n = len(matrix)
    somma = 0
    for i in range(n):
        somma += matrix[i][n - 1 - i]
    return somma
