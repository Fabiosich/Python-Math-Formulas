import math

def raizquad(a):
    print("Raiz quadrada de: ", a)
    x = eval(input("valor inicial sff: "))
    for i in range(10):
        x = 1/2 * (x + (a/x))
        print(x)
        return x

raizquad(16)