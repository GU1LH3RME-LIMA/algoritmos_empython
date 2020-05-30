def busca(k,Vet,inicio,fim):
    meio=(inicio+fim)//2
    if(Vet[meio]==k):
        return True
    elif(inicio>fim):
        return False
    else:
        if(Vet[meio]>k):
            return busca(k,Vet,inicio,meio-1)
        else:
            return busca(k,Vet,meio+1,fim)

Vet=[0,1,2,3,4,5,6]

k=int(input("Digite um numero: "))

if(busca(k,Vet,0,len(Vet)-1)==True):
    print("achei")
else:
    print("não achei")
