#coding: utf-8
prices = [int(n) for n in input('输入一个数组，以空格分隔数字').split()]
maxprofit = 0
bought = False
buypoint = 0
for i in range(0, prices.__len__()):
    if i == prices.__len__()-1:
        if bought:
            maxprofit = maxprofit + prices[i]-prices[buypoint]
        break
    if prices[i]<=prices[i+1]:
        if bought:
            continue
        else:
            buypoint = i
            bought = True
    else:
        if bought:
            maxprofit = maxprofit + prices[i]-prices[buypoint]
            bought = False
        else:
            continue
print(maxprofit)


# def bestprofit(prices):
#     l = prices.length()
#     if l == 1:
#         return 0
#     else:
#         return max(prices[l-1]-prices[0], bestprofit(prices[1:l]))