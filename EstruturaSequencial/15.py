# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato (5%) : R$
# = Salário Liquido : R$

valor_por_hora = float(input("Digite o quanto você ganha por hora: "))
quantidade_horas_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))
quantidade_minutos_trabalhados = int(input("Digite o número de minutos trabalhados no mês (além das horas): "))

minutos_em_decimal = round(quantidade_minutos_trabalhados / 60, 2)

salario_bruto = round((quantidade_horas_trabalhadas + minutos_em_decimal) * valor_por_hora, 2)
ir = salario_bruto*11/100
inss = salario_bruto*8/100
sindicato = salario_bruto*5/100
salario_liquido = salario_bruto - ir - inss - sindicato

print(" + Salário Bruto : R$", salario_bruto)
print(" - IR (11%) : R$", ir)
print(" - INSS (8%) : R$", inss)
print(" - Sindicato (5%) : R$", sindicato)
print(" = Salário Liquido : R$", salario_liquido)
