import os

def ip_valido(ip_string):
    partes = ip_string.split('.')
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit():
            return False
        parte_integer = int(parte)
        if parte_integer < 0 or parte_integer > 255:
            return False
    return True

if os.path.exists("1.txt"):
    ips = open("1.txt", "r")
    lista_ips = ips.read().split("\n")
    
    validos = []
    invalidos = []
    
    for ip in lista_ips:
        if ip_valido(ip) == True:
            validos.append(ip)
        else:
            invalidos.append(ip)
    
    if len(validos) > 0 or len(invalidos) > 0:
        arquivo_relatorio = open("resposta.txt", "wt")
        
        if len(validos) > 0:
            arquivo_relatorio.write("[Endereços válidos:]\n")
            for valido in validos:
                arquivo_relatorio.write(valido+"\n")
        
        if len(invalidos) > 0:
            arquivo_relatorio.write("\n[Endereços inválidos:]\n")
            for invalido in invalidos:
                arquivo_relatorio.write(invalido+"\n")
        
        arquivo_relatorio.close()
