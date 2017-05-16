def issafe(posx):
      for i in range(posx):
          if posy[i]==posy[posx] or abs(i-posx)==abs(posy[i]-posy[posx]):
             return 0
      return 1
def queen(k,n):
    if k==n:
        print(posy)
        return
    for i in range(0,n):
        posy[k]=i
        if issafe(k)==1:
            queen(k+1,n)
n=int(input("enter the board size"))
posy=[0 for i in range(n)]
queen(0,n)
