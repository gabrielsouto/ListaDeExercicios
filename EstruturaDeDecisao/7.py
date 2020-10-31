# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

primeiro_numero = float(input("Digite o primeiro número:"))
segundo_numero = float(input("Digite o segundo número:"))
terceiro_numero = float(input("Digite o terceiro número:"))

if primeiro_numero == segundo_numero and segundo_numero == terceiro_numero: # elif primeiro_numero == segundo_numero == terceiro_numero:
    print("Os números são iguais.")
else:
    #confere o(s) maior(es)
    if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero: # if segundo_numero < primeiro_numero > terceiro_numero:
        print("O maior número é o primeiro:", primeiro_numero)
    elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero: # elif primeiro_numero < segundo_numero > terceiro_numero:
        print("O maior número é o segundo:", segundo_numero)
    elif terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero: # elif primeiro_numero < terceiro_numero > segundo_numero:
        print("O maior número é o terceiro:", terceiro_numero)
    else:
        if primeiro_numero == segundo_numero:
            print("O primeiro número (",primeiro_numero,") e o segundo número (",segundo_numero,") são maiores que o terceiro número (",terceiro_numero,").")
        elif primeiro_numero == terceiro_numero:
            print("O primeiro número (",primeiro_numero,") e o terceiro número (",terceiro_numero,") são maiores que o segundo número (",segundo_numero,").")
        elif segundo_numero == terceiro_numero:
            print("O segundo número (",segundo_numero,") e o terceiro número (",terceiro_numero,") são maiores que o primeiro número (",primeiro_numero,").")
    
    #confere o(s) menor(es)        
    if primeiro_numero < segundo_numero and primeiro_numero < terceiro_numero: # if segundo_numero < primeiro_numero > terceiro_numero:
        print("O menor número é o primeiro:", primeiro_numero)
    elif segundo_numero < primeiro_numero and segundo_numero < terceiro_numero: # elif primeiro_numero < segundo_numero > terceiro_numero:
        print("O menor número é o segundo:", segundo_numero)
    elif terceiro_numero < primeiro_numero and terceiro_numero < segundo_numero: # elif primeiro_numero < terceiro_numero > segundo_numero:
        print("O menor número é o terceiro:", terceiro_numero)
    else:
        if primeiro_numero == segundo_numero:
            print("O primeiro número (",primeiro_numero,") e o segundo número (",segundo_numero,") são menores que o terceiro número (",terceiro_numero,").")
        elif primeiro_numero == terceiro_numero:
            print("O primeiro número (",primeiro_numero,") e o terceiro número (",terceiro_numero,") são menores que o segundo número (",segundo_numero,").")
        elif segundo_numero == terceiro_numero:
            print("O segundo número (",segundo_numero,") e o terceiro número (",terceiro_numero,") são menores que o primeiro número (",primeiro_numero,").")
