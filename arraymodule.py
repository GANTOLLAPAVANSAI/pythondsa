import array as ary
A=ary.array('i',[0,0,1,1,0,0])
i=0

for i in range(len(A)-1):
     if A[i] == 0:
        a=A[i]
        A[i]=A[i+1]
        A[i+1]=a

print(A)