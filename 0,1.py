import array as arr
a=arr.array("i",[1,1,0,0,0])

onecount=a.count(1)

for j in range(onecount):
    a.remove(1)

for k in range(onecount):
    a.append(1)
print(a)