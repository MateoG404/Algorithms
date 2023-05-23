def hash_one(i):
    return i % LENGTH

LENGTH = 16
num = [5224, 6227, 8404, 2357, 3333, 1826, 9994]
lista = [None] * LENGTH 


for i in num :
    cont = 0
    hash_ = hash_one(i)
    while lista[hash_] != None:
        cont += 1
        hash_ = ( (hash_one(i)) + (7*cont) ) % LENGTH
        
    lista[hash_] = i 
    #print(lista)
    
print(lista)