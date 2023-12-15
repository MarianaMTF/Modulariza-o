from arquivar import arquivar
def remover(lista, contatos_arq):
    nome=input("digite o nome do contato:")
    for contato in lista:
        if contato["nome"]==nome:
            lista.remove(contato)
            arquivar(lista, contatos_arq)
        else:
            print("o contato não existe")