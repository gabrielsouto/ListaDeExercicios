# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temperatura_c = float(input("Digite a temperatura em Celsius: "))
print("A temperatura em Fahrenheit é: ", round((temperatura_c * 9/5) + 32, 2))
