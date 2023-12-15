from adicionar_contato import adicionar
from visualizar import mostrar
from deletar import remover
from editar import editar

if __name__=="__main":
    lista=[]
    contatos_arq='arquivo.txt'
    while True:
        r=int(input("digite 1 para adicionar um contato, 2 para ver os contatos, 3 para remover, 4 para editar um contato, 0 para encerrar:"))
        if r==1:
            lista=adicionar(lista, contatos_arq)
        elif r==2:
            mostrar(contatos_arq)
        elif r==3:
            remover(lista, contatos_arq)
        elif r==4:
            editar(lista, contatos_arq)
        elif r==0:
            break