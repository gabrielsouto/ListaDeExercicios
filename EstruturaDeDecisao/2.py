# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = float(input("Digite um valor: "))

if valor == 0:
    print("O valor", valor, "é neutro.")
elif valor > 0:
    print("O valor", valor, "é positivo.")
else:
    print("O valor", valor, "é negativo.")
