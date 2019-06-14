to_root=[]
is_leaf=[]
n=int(input())
tree=[[0]*n for _ in range(n)]
for i in range(0,n-1):
    input_num=input()
    testnum=input_num.split()
    num=list(map(int,testnum))
    tree[num[0]-1][num[1]-1]=num[2]
    tree[num[1]-1][num[0]-1]=num[2]
    if num[0]==1 or num[0] in to_root:
        to_root.append(num[1])
for i in to_root.__iter__():

print(tree)
