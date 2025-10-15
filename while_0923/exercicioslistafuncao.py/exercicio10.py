def fibonacci(n):
 
    serie = [1, 1]
    
    for i in range(2, n):
        proximo_termo = serie[i-1] + serie[i-2]
        serie.append(proximo_termo)
    return serie

n = 10
print(f'Fibonacci({n}) = {fibonacci(n)}')  
