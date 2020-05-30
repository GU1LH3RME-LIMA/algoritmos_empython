n=int(input("Digite o numero de Funcionarios: "))
somaf=somam=mas=femi=maior=0
i=0
while i<n:
    idade=int(input("Qual é a idade do funcionario: "))
    salario=float(input("Qual o salario do funcionario: "))
    sexo=input("Qual o sexo(M / F): ")
    if sexo!="m" and sexo!="f":
        print("Opção invalida")
        idade=0
        sexo=0
        i-=1
   
    if(sexo=="m"):
        somam+=salario
        mas+=1
    else:
                  
        if(sexo=="f"):
            somaf+=salario
            femi+=1
    if (salario>maior and idade<30):
        maior=salario
    i+=1
mediamas=somam/mas
mediafem=somaf/femi
print("media masculina: ",mediamas)
print("media feminina: ",mediafem)
print("maior salario dos jovens: ",maior)
