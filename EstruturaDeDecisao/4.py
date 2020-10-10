# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: ")

letra_minuscula = letra.lower()

alfabeto = list(map(chr, range(ord('a'), ord('z')+1)))

if letra_minuscula in alfabeto:
    if letra_minuscula in ['a', 'e', 'i', 'o', 'u']:
        print("O usuário digitou uma vogal")
    else:
        print("O usuário digitou uma consoante")
else:
    print("O usuário não digitou uma letra")
