n=int(input("Escolha o numero de repetições: "))
soma=0
for i in range(1,n+1):
    
    x=int(input("Escolha um numero: "))
    if (i==n):
        x=0
    soma=soma+x
media=soma/n
print("a media dessa soma é ",media)
