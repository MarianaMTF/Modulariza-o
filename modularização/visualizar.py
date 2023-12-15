def mostrar(contatos_arq):
    with open(contatos_arq, "r")as arquivo:
        for linha in arquivo:
            print(linha)