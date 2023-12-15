from arquivar import arquivar
def adicionar(lista, contatos_arq):
    numeros=[]
    nome=input("digite o nome do contato:")
    endereco=input("digite o endereço:")
    while True:
        r=int(input("digite o numero(digite 0 para encerrar):"))
        if r==0:
            break
        numeros.append(r)
    dicionario={"nome":nome, "endereço": endereco, "numeros": numeros}
    lista.append(dicionario)
    return lista
