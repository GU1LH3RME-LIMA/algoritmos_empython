def div7(num):
    
    if(num<10):
        if(num==0 or num==7):
            return True
        else:
            return False
    elif(num==49):
        return False
    else:
        return div7(5*(num%10)+(num//10))

n=int(input("Digite um numero para saber se é ou não divisivel por 7: "))
if(div7(n)==True):
   print("sim")
else:
   print("não")
