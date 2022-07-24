L = [(2,1),(1,2),(4,4),(2,3),(2,1)]
for i in range(0,len(L)-1):
 for j in range(i,len(L)):
  if L[i][1] > L[j][1]:
    L[i],L[j]=L[j],L[i]
print(L)
            