# -*- coding: cp1252 -*-
def fat(n,comp):
    if n==0:
        comp=+1
        return 1
    else:
        comp+=1
        resultado=n*fat(n-1,comp)
        
    return resultado
    


for i in range(10,110,10):
    comp=0
    resultado=fat(i,comp)
    print("o fatorial de {} é {} ".format(i,resultado))

    
        
