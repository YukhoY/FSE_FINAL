ch=''
str=[]
res=[]
while ch!='@':
    ch=input()
    str.append(ch)
ch=str[0]
for i in range(1,str.__len__()-1):
    res.append(str[i].replace(ch,''))
res.sort(reverse=True)
for i in res.__iter__():
     print(i)
