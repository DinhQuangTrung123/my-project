
a=[5,4,8,9,10,12,2,5,8]

for i in range(len(a)):
    for j in range(len(a)-1):
        if (a[i]<a[j]):
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
print(a)