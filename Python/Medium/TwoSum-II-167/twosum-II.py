def twosum(num,target):
    l,r = 0,len(num)-1
    while l<r:
        x = num[l] + num[r]
        if x == target:
            return [l+1,r+1]
        elif x<target:
            l+=1
        else:
            r -=1
print(twosum([2,7,11,13,15],9))