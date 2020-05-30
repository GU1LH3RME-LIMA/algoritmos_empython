def le():
    lista=[]
    while True:
        nome=input("Digite o nome: ")
        if nome=="":break
        lista.append(nome)
    busca=input("Digite o valor a ser procurado: ")
    return lista,busca
def procv(lista,busca):
    lista.sort()
    inicio=0
    fim=len(lista)-1
    achei=False
    while inicio<=fim:
        meio=(fim+inicio)//2
        if busca==lista[meio]:
            achei=True
            break
        if busca>lista[meio]:
            inicio=meio+1
        else:
            fim=meio-1
    return achei
def prinln(busca,achei):

    if achei:
        print("O nome {:1s} foi encontrado".format(busca))
    else:
        print("O nome {:1s} não foi encontrado".format(busca))
    return

lista,busca=le()
achei=procv(lista,busca)
prinln(busca,achei)
    
    
        
