# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
primeiro_inteiro = int(input("Digite o primeiro número inteiro:"))
segundo_inteiro = int(input("Digite o segundo número inteiro:"))
terceiro_real = float(input("Digite o terceiro número real:"))

print("O produto do dobro do primeiro com metade do segundo:", (primeiro_inteiro*2) * (segundo_inteiro/2))
print("A soma do triplo do primeiro com o terceiro:", (primeiro_inteiro*3) + terceiro_real)
print("O terceiro elevado ao cubo:", terceiro_real**3)
