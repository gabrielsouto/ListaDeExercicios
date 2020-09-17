# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
temperatura_f = float(input("Digite a temperatura em Fahrenheit: "))
print("A temperatura em Celsius é: ", round((temperatura_f-32)*5/9, 2))
