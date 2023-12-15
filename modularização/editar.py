from arquivar import arquivar
def editar(lista, contatos_arq):
    nome=input("digite o nome do contato:")
    for contato in lista:
        if contato["nome"]==nome:
            r=input("digite se deseja mudar o endereço ou os numeros:")
            if r=="endereço":
                novo=input("digite o novo endereço:")
                contato["endereço"]=novo
                arquivar(lista, contatos_arq)
            if r=="numeros":
                for n in contato["numeros"]:
                    numero=int(input("digit o numero que deseja mudar:"))
                    if numero==n:
                        novo=int(input("digite o novo numero:"))
                        contato[n]=novo
                        arquivar(lista, contatos_arq)
                    else:
                        print("o numero não esta no arquivo")
        else:
            print("o nome não esta no arquivo")

