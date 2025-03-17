l1 = [1,2,3,4,5,6,7]
target = 7
l2 = []
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i] + l1[j] == target:
            l2.append([i,j])
print(l2)