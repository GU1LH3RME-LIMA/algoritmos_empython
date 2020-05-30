soma=0
for i in range(1,4):
    x=float(input("Nota da {:2d} prova: ".format(i)))
    soma+=x
media=soma/3
print("Media : {:5.2f}".format(media))
    
