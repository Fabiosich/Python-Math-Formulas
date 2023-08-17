def peso(n):
    for i in range(n):
        altura = float(input("Qual a tua altura?"))
        sexo = (input("Qual o teu género?"))

    if sexo == "M":
        ideal = 62.1 * altura
        return print("O seu peso ideal é ", ideal, "quilogramas")
    elif sexo == "H":
        ideal = 72.7 * altura
        return print("O seu peso ideal é ", ideal, "quilogramas")
    else:
        print("Opção invalida")

peso(1) 
