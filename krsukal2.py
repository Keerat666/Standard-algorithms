n=int(input("Enter the number of matrices"))
global u , v
cost=[[0 for x in range(n+1)] for x in range(n+1)]
parent = [0 for x in range(n)]
for i in range(1,n+1):
    print("Enter the cost matrix for ", i)
    for j in range(1,n+1):
        cost[i][j]=int(input())
        if cost[i][j]==0:
            cost[i][j]=999
print(cost)

def find(i,j):
    while parent[i]:
        i=parent[i]
    return i

def uni(i,j):
    if i!=j:
        parent[j]=i
        return 1
    return 0

ne=1
tc=0
while ne<n:
    min1=999
    for i in range(1,n+1):
            for j in range(1,n+1):
                if cost[i][j]<min1:
                    min1=cost[i][j]
                    u=a=i
                    v=b=j
    u=find(u,v)
    v=find(u,v)

    if uni(u,v):
        print(ne, "edge(", a, ",", b, ") = ", min1)
        tc+=min1
        ne=ne+1
    cost[a][b]=cost[b][a]=999
print(tc)
