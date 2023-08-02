import array as ary
A = ary.array('i', [1, 3, 4, 6, 8, 9, 10])

i = 0
j = len(A)-1

while(i<=j):
     print(A[i])
     print(A[j])
     i+=1
     j-=1