nk=input()
nk=nk.split()
nk=list(map(int,nk))
n=nk[0]
k=nk[1]
f=[[0,0,0] for _ in range(n)]
for i in range(n):
    nums=input()
    nums=list(map(int,nums.split()))
    f[i]=nums.copy()
mins=[0]*n
results=[]
for i in range(n):
    # mins[i]=-f[i][1]/(2*f[i][0])
    mins=int(-f[i][1]/(2*f[i][0]))
    low=int(mins-k/2-1)
    high=int(mins+k/2+1)
    for x in range(low,high):
        cal=f[i][0]*x*x + f[i][1]*x + f[i][2]
        results.append(cal)
results.sort()
res=str(results[0])
for i in range(1,k):
   res=res+' '+str(results[i])
print(res)