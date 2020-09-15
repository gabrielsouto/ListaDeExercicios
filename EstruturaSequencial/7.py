# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Digite o comprimeto do lado do quadrado: "))

area = lado ** 2
area_em_dobro = area * 2

print("O dobro da área deste quadrado de lado", lado, "é:", area_em_dobro)
