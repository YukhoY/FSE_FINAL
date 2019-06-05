#coding: utf-8
instring=input("输入一个字符串")
repeat=1
for i in range(0,instring.__len__()):
    if i<instring.__len__()-1 and instring[i] == instring[i+1] :
            repeat = repeat + 1
    else:
        if repeat == 1:
            if i == 0:
                ans = instring[i]
            else:
                ans = ans + instring[i]
        else:
            if i == 0:
                ans = str(repeat) + instring[i]
            else:
                ans = ans + str(repeat) + instring[i]
        repeat = 1
print(ans)
