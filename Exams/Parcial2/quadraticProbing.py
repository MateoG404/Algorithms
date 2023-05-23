
def hash_one(i):
    return i % 12

    
#num = list(map(int,input().split(",")))
num = [5224, 6227, 8404, 2357, 3333, 1826, 9994]
lista = [None]*12


for i in num :
    cont = 0
    hash_ = hash_one(i)
    while lista[hash_] != None:
        cont += 1
        hash_ = ( (hash_one(i)) + (3*cont) + ( 10 * (cont** 2) ) ) % 12
        
    lista[hash_] = i 
    #print(lista)
    
print(lista)