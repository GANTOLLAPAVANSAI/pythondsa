import array as ary
A=ary.array('i',[1,2,3,3,2,1])
i=0
j=len(A)-1
flag=0
while(i<=j):
    if(A[i]!=A[j]):
         print("Not a palondrome")
         flag=1
if(flag==0):
     print("Its a palindrom number")
