from faker import Faker
import random


class DistanciaEdicion:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.n = len(A)
        self.m = len(B)
        self.memo = [[0] * (self.m+1) for _ in range(self.n+1)]

    def distancia_edicion(self):
        return self.calcular_distancia(self.n, self.m)

    def calcular_distancia(self, i, j):
        if self.memo[i][j] != -1:
            return self.memo[i][j]

        if i == 0:
            self.memo[i][j] = j
            return j

        if j == 0:
            self.memo[i][j] = i
            return i

        if self.A[i-1] == self.B[j-1]:
            self.memo[i][j] = self.calcular_distancia(i-1, j-1)
            return self.memo[i][j]

        insertar = 1 + self.calcular_distancia(i, j-1)
        borrar = 1 + self.calcular_distancia(i-1, j)
        reemplazar = 1 + self.calcular_distancia(i-1, j-1)

        minimo = min(insertar, borrar, reemplazar)
        self.memo[i][j] = minimo

        if minimo == insertar:
            # Realizar la operación de inserción
            # Agregar carácter B[j-1] a A
            self.A = self.A[:i] + self.B[j-1] + self.A[i:]

        elif minimo == borrar:
            # Realizar la operación de borrado
            # Eliminar carácter A[i-1]
            self.A = self.A[:i-1] + self.A[i:]

        else:
            # Realizar la operación de reemplazo
            # Reemplazar carácter A[i-1] por B[j-1]
            self.A = self.A[:i-1] + self.B[j-1] + self.A[i:]

        return minimo

def generar_palabra_aleatoria(length):
    faker = Faker('es_ES')
    palabra = faker.word()
    while len(palabra) < length:
        palabra += random.choice(faker.word())
    palabra = palabra[:length]
    return palabra


# Generar 10 ejemplos con palabras de longitud 5 y mostrar los subproblemas
for _ in range(1,11):
    print("Ejemplo número",_)
    length = 5
    A = generar_palabra_aleatoria(length)
    B = generar_palabra_aleatoria(length)

    distancia = DistanciaEdicion(A, B)
    resultado = distancia.distancia_edicion()
    
    print("A:", A)
    print("B:", B)
    print("Distancia óptima:", distancia)
    print("Solución:", resultado)
    print("")