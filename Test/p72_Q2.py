#
# def getMaxColors(prices, money):
#     ## double pointer
#     i=j=0
#     s=0
#     max_number = 0
#     while j < len(prices):
#         s += prices[j]
#         if s <= money:
#             max_number = max(j-i+1, max_number)
#         else:
#             while i <= j and s > money:
#                 s -= prices[i]
#                 i += 1
#         j += 1
#     return max_number

def getMaxColors(prices, money):
    # Write your code here
    arr_sum = 0
    count = 0
    max_count = 0
    for i in range(len(prices)):
        arr_sum += prices[i]
        if (arr_sum <= money):
            count += 1
        else:
            arr_sum -= prices[i-count]
        max_count = max(max_count, count )
    return (max_count)

prices=[2,3,5,1,6,2,1,1,10,1,1]
# prices=[5,10,10]
money=10
print(getMaxColors(prices,money))