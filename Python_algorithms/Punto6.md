# Python Divide-to-Conquer Algoritm: Finding how many prime numbers there are in an array with $2^k$ elements

Se presentará el algoritmo correspondiente al punto 4 D, el cuál solicitaba crear una implementación en Python que fuera capaz de identificar cuántos números primos existen en un arreglo de longitud n, en donde n es una potencia de 2 de la forma $2^k$.

```{python}
import math
def primes(A,p,r):        # Donde A es el arreglo, p es el índice inicial y r es el índice final
  if int(p)==int(r):      # Cuando la longitud del arreglo es 1, se mira si este número es primo
      a=CheckPrimes(A,p)
      return a
  else: 
      q=math.floor((p+r)/2)
      a = primes(A,p,q)   # Se divide sucesivamente el arreglo hasta quedar en subarreglos de 1 y verificar si son primos
      b = primes(A,q+1,r)
      return a+b

def CheckPrimes(A,p):
    n = int(A[p])
    cont = 0
    if n in P:
        return 1
    else:
        if n == 1 or n==0:
            return 0
        for i in range(2, int(math.sqrt(n))+1):  # Se verifica si el número es divisible por factores que están entre 2 y su raíz cuadrada, si lo es, se retorna 0
            if(n%i==0):
                return 0
        P.append(n)
        return 1

P=[]        
A=[2,2,2,2]
primes(A,0,len(A)-1)
```
