'''determinar se um determinado valor existe
na linha 1 de uma matriz mxn'''

def le():
    m=int(input("Digite numero de linhas "))#linhas
    n=int(input("Digite numero de colunas "))#colunas
    a=[None]*m#cria um vetor com m linhas
    for i in range(m):
        a[i]=[None]*n#para cada linha cria n colunas
        for j in range(n):
            a[i][j]=float(input('a['+str(i+1)+'].['+str(j+1)+']'))
        
    lista=[]
    #le o valor
    busca=float(input("Valor a procurar "))

    for i in range(n):
        lista.append(a[0][i])
        
    return lista,busca
def loc(lista,busca):
    lista.sort()    #ordena a lista
    achei=False
    inicio=0
    fim= len(lista)-1
    while inicio<=fim:
        meio = (inicio +fim)//2
        if busca== lista[meio]:
            achei=True
            break
        else:
            if lista[meio]<busca:
                inicio= meio+1
            else:
                fim = meio-1
    return achei
def impr(busca,achei):
    if achei==True:
        print ("Valor {:5.2f} encontrado".format(busca))
    else:
        print("Valor {:5.2f} não encontrado".format (busca))
    return

lista,busca=le()
achei=loc(lista,busca)
impr(busca,achei)

            
                      
