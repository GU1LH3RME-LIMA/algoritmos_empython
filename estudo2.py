def le():
    lista=[]
    m=int(input("Digite um numero de linhas: "))
    n=int(input("Digite um numero de colunas: "))
    a=[None]*m
    for i in range(m):
        a[i]=[None]*n
        for j in range(n):
            while True:
                try:
                    a[i][j]=int(input("Defina na matriz A ["+str(i+1)+"].["+str(j+1)+"]"))
                    break
                except:
                    print("Dado invalido, por favor digite novamente")
    for i in  range (m):
        lista.append(a[i][0])
    print ("\n{:*^30}\n".format("Matriz Lida"))
    for i in  range (m):
        for j in range(n):
            print("{:>10.2f}".format(a[i][j]),end="")
        print()
    busca=int(input("Digite um elemento a ser encontrado na 1ª coluna: "))

    return lista,busca

def procv(lista,busca):
    lista.sort()
    inicio=0
    fim=len(lista)-1
    achei=False
    while inicio<=fim:
        meio=(inicio+fim)//2
        if busca==lista[meio]:
            achei=True
            break
        elif busca>lista[meio]:
            inicio=meio+1
        else:
            fim=meio-1
    return achei

def println(busca,achei):
    if achei:
        print("O valor {:5.2f} foi encontrado ".format(busca))
    else:
        print("O valor {:5.2f} não foi encontrado ".format(busca))

lista,busca=le()
achei=procv(lista,busca)
println(busca,achei)
        
        
              
        
