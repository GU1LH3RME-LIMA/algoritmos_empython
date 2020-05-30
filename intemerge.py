v1=[1,2,3,4,5]
v2=[2,3,3,4,4]
v3=[]
i=0
j=0
m=len(v1)-1
n=len(v2)-1
while(i<=m)and(j<=n):
    if (v1[i]<v2[j]):
        v3.append(v1[i])
        i+=1
    elif(v1[i]==v2[j]):
        i+=1
        j+=1
        
    else:
        
        j+=1
while(i<=m):
    v3.append(v1[i])
    i+=1


print(v3)

