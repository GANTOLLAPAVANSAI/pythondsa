def slidingwindow(arr,n,x):
    i=0
    while(i<n-2):
        if(a[i]+a[i+1]==x):
            print("True ",i,i+1)
            break

import array as ary
a=ary.array('i',[1,3,4,6,8,9,10])
slidingwindow(a,len(a),10)