n=int(input())
str=[]
A=[]
B=[]
C=[]
D=[]
count=0
for i in range(0,n):
    input_num=input()
    testnum=input_num.split()
    A.append(int(testnum[0]))
    B.append(int(testnum[1]))
    C.append(int(testnum[2]))
    D.append(int(testnum[3]))
for a in A.__iter__():
    for b in B.__iter__():
        for c in C.__iter__():
            for d in D.__iter__():
                if a+b+c+d==0:
                    count=count+1
print(count)
