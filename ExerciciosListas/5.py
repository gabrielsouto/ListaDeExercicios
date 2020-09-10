# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
# Imprima os três vetores.

numeros_inteiros_lidos = []
pares = []
impares = []

for posicao in range(0, 20):
    print("Digite o ", posicao+1, "º número: ", sep="")
    numero = int(input())
    numeros_inteiros_lidos.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lidos:", numeros_inteiros_lidos)
print("Pares:", pares)
print("Ímpares:", impares)
