numero_lido = 0
numeros_lidos = []

while numero_lido != -1:
    numero_lido = float(input("Digite um número ou -1 para encerrar: "))
    if numero_lido != -1:
        numeros_lidos.append(numero_lido)

print("A. Quantidade de valores que foram lidos:", len(numeros_lidos))

print("B. Valores na ordem em que foram informados, um ao lado do outro:")
for numero in numeros_lidos:
    print(numero, end=" ")
    
print("\nC. Valores na ordem inversa à que foram informados, um abaixo do outro:")
for indice in range(len(numeros_lidos)-1, -1, -1):
    print(numeros_lidos[indice])
    
print("D. A soma dos valores:")
print("\tUsando sum:", sum(numeros_lidos))
print("\tUsando for e somando 1 a 1: ", end="")
soma = 0
for numero in numeros_lidos:
    soma += numero
print(soma)

media = soma/len(numeros_lidos)
print("E. A média dos valores:", media)

print("F. Quantidade de valores acima da média calculada: ", end="")
acima_media = 0
for numero in numeros_lidos:
    if numero > media:
        acima_media += 1
print(acima_media)

print("G. Quantidade de valores abaixo de sete: ", end="")
abaixo_7 = 0
for numero in numeros_lidos:
    if numero < 7:
        abaixo_7 += 1
print(abaixo_7)

print("Programa encerrado.")
