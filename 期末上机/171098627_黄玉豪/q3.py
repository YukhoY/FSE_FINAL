# def is_to_root(tree,i):
#     if i==0:
#         return True
#     i_list=list(tree[i].index(2))
#     for j in i_list.__iter__():
#         if is_to_root(tree,j+1):
#             return True
#     return False
to_root=[]
n=int(input())
tree=[[0]*n for _ in range(5)]
for i in range(0,n-1):
    input_num=input()
    testnum=input_num.split()
    num=list(map(int,testnum))
    tree[num[0]-1][num[1]-1]=num[2]
    tree[num[1]-1][num[0]-1]=num[2]
    if num[0]==1 or num[0] in to_root:
        to_root.append(num[1])
for i in to_root.__iter__():
    if 
# is_to_root(tree,2)
# is_to_root(tree,3)
print(tree)
