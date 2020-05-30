def ler():
    plv=input("Escreva uma palavra: ")
    plvs=''
    for i in plv:
        if i!=' ':
            plvs+=i
    return plv,plvs
def compr(plv,plvs):
    if (plvs==plvs[::-1]):
        print("{:1s} é uma palavra paliativa".format(plv))
    else:
        print("{:1s} não é uma palavra paliativa".format(plv))
    return
n,n2=ler()
compr(n,n2)
