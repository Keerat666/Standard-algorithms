def minmax(a,i,j):
    if i==j:
        mi=a[i]
        ma=a[i]
    elif j-1==i:
        if a[i]>a[j]:
            mi=a[j]
            ma=a[i]
        else:
            mi=a[i]
            ma=a[j]
    else :
        mid=(i+j) // 2
        m1=minmax(a,i,mid)
        m2=minmax(a,mid+1,j)

        if m1[0]>m2[0]:
            mi=m2[0]
        else:
             mi=m1[0]
        if m1[1]>m2[1]:
            ma=m1[1]
        else:
            ma=m2[1]
    return [mi , ma]

x={}
x=[1,2,3,4,5,6,7,8,9,10]

b=minmax(x,0,9)
print (b)
