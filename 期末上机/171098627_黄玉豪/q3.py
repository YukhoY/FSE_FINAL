n=int(input())
tree=[[0]*n for _ in range(5)]
for i in range(0,n-1):
    input_num=input()
    testnum=input_num.split()
    num=list(map(int,testnum))
    tree[num[0]-1][num[1]-1]=num[2]
    tree[num[1]-1][num[0]-1]=num[2]
print(tree)
def is_to_root(tree,i):
    if i==1:
        return True
    i_list=list(tree[i-1].index(2))
    for j in i_list.__iter__():
        if is_to_root(tree,j+1):
            flag=1
        else: flag=0