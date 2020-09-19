# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_por_hora = float(input("Digite o quanto você ganha por hora: "))
quantidade_horas_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))
quantidade_minutos_trabalhados = int(input("Digite o número de minutos trabalhados no mês (além das horas): "))

minutos_em_decimal = round(quantidade_minutos_trabalhados / 60, 2)

salario_do_mes = round((quantidade_horas_trabalhadas + minutos_em_decimal) * valor_por_hora, 2)

print("O seu salário deste mês é: ", salario_do_mes)
