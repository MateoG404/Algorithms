from faker import Faker
import random

class DistanciaEdicion:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.n = len(A)
        self.m = len(B)
        self.dp = [[0] * (self.m+1) for _ in range(self.n+1)]
    
    def distancia(self):
        for i in range(self.n+1):
            self.dp[i][0] = i
            
        for j in range(self.m+1):
            self.dp[0][j] = j
        
        for i in range(1, self.n+1):
            for j in range(1, self.m+1):
                if self.A[i-1] == self.B[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1]
                else:
                    insertar = 1 + self.dp[i][j-1]
                    borrar = 1 + self.dp[i-1][j]
                    reemplazar = 1 + self.dp[i-1][j-1]
                    self.dp[i][j] = min(insertar, borrar, reemplazar)
        
        return self.dp[self.n][self.m]
    
    def obtenerSolucion(self):
        solucion = []
        i = self.n
        j = self.m
        
        while i > 0 or j > 0:
            if self.A[i-1] == self.B[j-1]:
                solucion.append("Mantener " + self.A[i-1])
                i -= 1
                j -= 1
            else:
                actual = self.dp[i][j]
                izquierda = self.dp[i][j-1]
                arriba = self.dp[i-1][j]
                diagonal = self.dp[i-1][j-1]
                
                if actual == diagonal + 1:
                    solucion.append("Reemplazar " + self.A[i-1] + " con " + self.B[j-1])
                    i -= 1
                    j -= 1
                elif actual == izquierda + 1:
                    solucion.append("Insertar " + self.B[j-1])
                    j -= 1
                elif actual == arriba + 1:
                    solucion.append("Borrar " + self.A[i-1])
                    i -= 1
        
        solucion.reverse()
        return solucion

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
    de = DistanciaEdicion(A, B)
    distancia_optima = de.distancia()
    solucion = de.obtenerSolucion()

    print("A:", A)
    print("B:", B)
    print("Distancia óptima:", distancia_optima)
    print("Solución:", solucion)
    print("")
