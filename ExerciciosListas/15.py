# 15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
# de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
nota_lida = 0
notas_lidas = []

while nota_lida != -1:
    nota_lida = float(input("Digite a nota ou -1 para encerrar: "))
    if nota_lida != -1:
        notas_lidas.append(nota_lida)
        
# Mostre a quantidade de valores que foram lidos;
print("A. Quantidade de valores que foram lidos:", len(notas_lidas))

# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print("B. Valores na ordem em que foram informados, um ao lado do outro:", notas_lidas)
for nota in notas_lidas:
    print(nota, end=" ")
    
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
print("\nC. Valores na ordem inversa à que foram informados, um abaixo do outro:")
for indice in range(len(notas_lidas)-1, -1, -1):
    print(notas_lidas[indice])
    
# Calcule e mostre a soma dos valores
print("D. Soma dos valores")
print("\tUsandao a função Sum:", sum(notas_lidas))
print("\tUsando for e somando 1 a 1: ", end="")
soma = 0
for nota in notas_lidas:
    soma += nota
print(soma)

# Calcule e mostre a média dos valores
media = soma/len(notas_lidas)
print("E. A média das notas:", media)

# Calcule e mostre a quantidade de valores acima da média calculada;
print("F. Quantidade de valores acima da média: ", end="")
acima_media = 0
for nota in notas_lidas:
    if nota > media:
        acima_media += 1
print(acima_media)

# Calcule e mostre a quantidade de valores abaixo de sete;
print("G. Quantidade de valores abaixo de sete: ", end="")
abaixo_7 = 0
for nota in notas_lidas:
    if nota < 7:
        abaixo_7 += 1
print(abaixo_7)

# Encerre o programa com uma mensagem;
print("Programa encerrado.")
