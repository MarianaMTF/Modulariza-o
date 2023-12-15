def arquivar(lista, contatos_arq):
    with open(contatos_arq, "a")as arquivo:
        for contato in lista:
            for chave, valor in contato.items():
                arquivo.write(f'{chave}: {valor}\n')