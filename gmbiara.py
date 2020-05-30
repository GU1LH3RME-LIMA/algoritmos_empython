def ler():
    a=[]
    b=[]
    j=soma=0
    while True:
        x=(input("Digite um nome "))
        while True:
            try:
                y=int(input("Digite a idade dessa pessoa: "))
                if (y==0):break 
                if (y<18) or (y>99):raise
                break
                
                
            except:
                print("dado invalido")
        if (y==0):break      
        a.append(x)
        b.append(y)
        soma+= y   
    j=len(a)
    return a,soma,j

def calc_media(soma,j):
    media=soma/j    
    print("media é igual a {:5.2f} ".format(media))
    return media

def maiores(a,j):
    maior=0
    nomeMaior=""

    for i in range(j):
        if len(a[i])>maior:
            nomeMaior=a[i]
    print("Existem {:1s} o maior nome".format(nomeMaior))
    return
import time
t1=time.time()
a,soma,j=ler()
media=calc_media(soma,j)
maiores(a,j)
t2=time.time()
print("Gastei {:5.2f} segundos".format(t2-t1))           
