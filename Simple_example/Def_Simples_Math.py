import math
import random


def volumeesf(raio):
    return print((4/3) * math.pi * raio ** 3)

volumeesf(2)

def sin(ang):
    return print(math.sin(ang))

sin(45)

def adivinha(tentativas):
    secreto = random.randint(20, 23)
    for i in range (tentativas):
        numero = eval(input("Digite o seu palpite: "))

        if numero == secreto:
            print("Acertou")
            return True
        else:
            if numero > secreto:
                print("É menor!")
    else:
        print("Excedeste as tentativas!")
        print("O numero era o", secreto,".")
        return False

adivinha(3)



