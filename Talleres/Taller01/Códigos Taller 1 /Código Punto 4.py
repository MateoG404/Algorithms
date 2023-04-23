import math
def primes(A,p,r):
  if int(p)==int(r):
      a=CheckPrimes(A,p)
      return a
  else: 
      q=math.floor((p+r)/2)
      a = primes(A,p,q)
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
        for i in range(2, int(math.sqrt(n))+1):
            if(n%i==0):
                return 0
        P.append(n)
        return 1

P=[]        
A=[2,2,2,2]
primes(A,0,len(A)-1)