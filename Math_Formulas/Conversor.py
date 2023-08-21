import math

def convertTemp():
    tempC = float(input("insira a temperatura em Celsius:"))
    tempC = 9/5 * tempC + 32  # Formula de Conversão
    print(tempC, "Fahrenheit")


def IMC():
    peso = float(input("O teu peso é:"))
    altura = float(input("A tua altura é:"))
    indiceMC = peso/(altura ** 2)  # Formula para calcular o IMC
    print("O teu IMC é ", indiceMC)


def volumeCone():
    r = float(input("Insere o raio "))
    h = float(input("insere a altura "))
    volume = (math.pi * (r ** 2) * h) / 3  # Formula para calcular volume de um cone
    print("O volume do cone é:", volume)

def calcPolinomio(x):
    pol = (x ** 4) + (x ** 3) + (2 * x ** 2) - x  # Formula para calcular polinomio de um numero
    print("o valor do polinomio", x, "é", pol)

calcPolinomio(1.1)
calcPolinomio(5)
calcPolinomio(3/2)

import cmath ### Utilizado para numero complexos

def declive(x1, y1, x2, y2):
    """Calcula as raízes de um polinómio de segundo grau"""
    if x1 != x2:
        return (y2 - y1) / (x2 - x1)
    else:
        return float('Inf')

def poli_2(a, b, c):
    """Calcula as raízes de uma polinómio de segundo grau"""
    delta = cmath.sqrt(b**2 - 4 * a * c)
    raiz_1 = (-b + delta) / (2 * a)
    raiz_2 = (-b - delta) / (2 * a)
    return  raiz_1, raiz_2

def AreaTriangulo(a, b, c):
    """Calcula da area de uma triangulo utilizando a formula de Heron"""
    s = (a + b + c)/ 2
    area = math.sqrt(s * (s -a) * (s - b) * (s - c))
    return print(area)

AreaTriangulo(2,2,3)


def cumpEscada(alt, ang):
    """Supondo que quero colocar uma escada esncostada á parede, calculamos o comprimento da escada"""
    rad = math.pi/180 * ang
    comp = alt /math.sin(rad)
    return print(comp, 'metros de comprimento.')
cumpEscada(3,45)

def ValorMedBatCardiaco(idade):
    """Calcula a media de batimento cardiacos por idades"""
    batMed = 163+1.16* idade -0.018 * idade**2
    return print(batMed, 'bpm.')
ValorMedBatCardiaco(60)


def poupança(v, t, a):
    """Tendo um valor inicial, quanto dinheiro teria ao fim de x anos com uma taxa de juro t"""
    """v- valor inicial, t - taxa de juro, a - tempo(anos)"""
    valorFinal = v*(1+t)**a
    return print(valorFinal)
poupança(100, 0.1, 7.27259)

def fatorial(n):
    """Calcula fatorial de n"""
    if n == 0:
        return 1
    else:
        return n * (n -1)
fatorial(2)




