'''
def hash_one(i):
    return i % 13

def hash_dos(i):
    return 1 + (i % 9)
    
#num = list(map(int,input().split(",")))
num = [5224, 6227, 8404, 2357, 3333, 1826, 9994]
lista = [None]*13

cont = 0 
for i in num:
    
    hash_ = hash_one(i)
    
    if lista[hash_] == None:
        lista[hash_] = i
    else:
        cont += 1 
        hash_ = (hash_dos(i) + hash_one(i)) % 13
        print(hash_,i)
        lista[hash_] = i
        
print(lista)

'''
class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function_1(self, key):
        return key % self.size

    def hash_function_2(self, key):
        return 1 + (key % 9)

    def double_hashing(self, key, i):
        print("->>",(self.hash_function_1(key) + i * self.hash_function_2(key)) % self.size)
        return (self.hash_function_1(key) + i * self.hash_function_2(key)) % self.size

    def insert(self, key):
        i = 0
        hash_value = self.hash_function_1(key)
        while self.table[hash_value] is not None:
            i += 1
            print(i,key)
            hash_value = self.double_hashing(key, i)
        self.table[hash_value] = key

    def print_table(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"Slot {i}: {self.table[i]}")
            else:
                print(f"Slot {i}: Empty")


# Crear una tabla hash con tamaño 13
hash_table = DoubleHashingHashTable(13)

# Insertar elementos en la tabla hash
elements = [5224, 6227, 8404, 2357, 3333, 1826, 9994]
for element in elements:
    hash_table.insert(element)

# Imprimir la tabla hash
hash_table.print_table()
