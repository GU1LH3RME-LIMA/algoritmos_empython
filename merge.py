v1=[1,2,3,4]
v2=[2,3,3,4,4]
v3=[]
i=0
j=0
m=len(v1)-1
n=len(v2)-1
while(i<=m)and(j<=n):
    if (v1[i]<=v2[j]):
        v3.append(v1[i])
        i+=1
        
    else:
        v3.append(v2[j])
        j+=1
while(i<=m):
    v3.append(v1[i])
    i+=1
while(j<=n):
    v3.append(v2[i])
    j+=1

print(v3)

