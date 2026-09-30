#Sin P. Dinamica N -> 5 n->60

def fibonacci(n):
    if n <= 1:
        return(n)
    
    return fibonacci(n-1) + fibonacci(n-2)
