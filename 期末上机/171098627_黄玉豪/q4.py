k=input()
nk=nk.split()
nk=list(map(int,nk))
n=nk[0]
k=nk[1]
routes=[[[0]*n for _ in range(n)]]
for i in range(k):
    input_num=input()
    testnum=input_num.split()
    num=list(map(int,testnum))
    routes[num[0]-1][num[1]-1]=num[2]
    routes[num[1]-1][num[0]-1]=num[2]