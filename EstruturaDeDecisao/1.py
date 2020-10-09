# Faça um Programa que peça dois números e imprima o maior deles.
numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

if numero_1 > numero_2:
    print("O primeiro número (", numero_1, ") é maior que o segundo número (", numero_2,")")
elif numero_2 > numero_1:
    print("O segundo número (", numero_2, ") é maior que o primeiro número (", numero_1,")")
else:
    print("Os números são iguais")
