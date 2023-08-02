import array as ary
A = ary.array('i', [1, 3, 4, 6, 8, 9])

d = int(input("give me the element : "))

for i in range(len(A)):
     if(d == A[i]):
         j = i
         while(j < len(A)-2):
             A[j] = A[j+2]
             j+=1
         break

print(A)