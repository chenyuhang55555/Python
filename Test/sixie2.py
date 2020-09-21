## Low efficiency n^2!!

# def solution(X,Y):
#     l = len(X)
#     dic = {}
#     for i in range(l):
#         x0 = X[i]
#         y0 = Y[i]
#         existed = 0
#         for x,y in dic.keys():
#             if x0*y-x*y0==0:
#                 dic[(x,y)] += 1
#                 existed = 1
#                 break
#         if not existed:
#             dic[(x0,y0)] = 1
#     return max(dic.values())
import math
def solution(X, Y):
    num_zeros = len([a for a in X if a == 0])
    filtered_x = [X[i] for i in range(len(X)) if X[i] != 0]
    filtered_y = [Y[i] for i in range(len(X)) if X[i] != 0]
    res = {}

    for i in range(len(filtered_x)):
        x = filtered_x[i]
        y = filtered_y[i]
        d = math.gcd(x, y)
        k = (int(x/d), int(y/d))
        if k not in res:
            res[k] = 1
        else:
            res[k] += 1
    if len(res) > 0:
        return max(max(list(res.values())), num_zeros)
    else:
        return num_zeros

# X=[4,4,7,1,2]
# Y=[4,4,8,1,2]
X=[1,2,3,1,2]
Y=[2,4,6,5,10]
print(solution(X,Y))


# def getLCM(lst):
#     l = len(lst)
#     if l == 1:
#         return lst[0]
#     else:
#         # print(len(l//2))
#         bin_list = [int(lst[2 * i] * lst[2 * i + 1] / math.gcd(lst[2 * i], lst[2 * i + 1])) for i in range(l // 2)]
#
#         if (l % 2) == 1: bin_list += [lst[l - 1]]
#         # print(bin_list)
#         return getLCM(bin_list)
# # lst[2 * i] * lst[2 * i + 1] /
# # lst=[5,400,4,3]
# # l=len(lst)
# # print([lst[2 * i] * lst[2 * i + 1] for i in range(l // 2)])
# # print([math.gcd(lst[2 * i], lst[2 * i + 1]) for i in range(l // 2)])
# # print([int(lst[2 * i] * lst[2 * i + 1] / math.gcd(lst[2 * i], lst[2 * i + 1])) for i in range(l // 2)])
# # print(getLCM([5,400,4,3]))
# # print(list(range(1)))
# print(getLCM([1200,12]))
