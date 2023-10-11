#Faça um programa em que o usuário digita um número inteiro e o programa exibe todos os números ímpares do 1 até o valor inserido.
n = int(input("Digite um número inteiro: "))

print("Números ímpares de 1 até", n, ":")
for x in range(1, n+1, 2):
    print(x)

