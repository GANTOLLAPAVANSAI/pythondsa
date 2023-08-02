import array as ary
a=ary.array('i',[100,22,3,4,1])
for i in range(len(a)):
    for j in range((len(a)-i)-1):
        if(a[j]>a[j+1]):
          temp=a[j]
          a[j]=a[j+1]
          a[j+1]=temp
print(a)