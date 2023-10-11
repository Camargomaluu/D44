#Faça um programa que gere as tabuadas do 1 até o 10
for x in range(1, 11):
    print(f"Tabuada do {x}:")
    for n in range(1, 11):
        resultado = x * n
        print(f"{x} x {n} = {resultado}")
    print()  # Adiciona uma linha em branco entre as tabuadas