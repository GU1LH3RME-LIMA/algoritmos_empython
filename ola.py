arq=open('arquivo.txt','w+')
for i in range(5):
    nome=input("Digite o nome: ")
    arq.write(nome+"\n")

arq.seek(0)
for i in arq:
    print(i)
arq.close()
