# f = open("solution.txt", "w")
#
# f.write("[")
# for i in range(1,100001):
#     f.write(","+str(i))
#
# f.write("]")
# f.close()

# import numpy as np
# import pandas as pd


# def solution(A):
#     # write your code in Python 3.6
#     trial_list = [1, 2, 3, 4, 5, 6]
#     count_step_list = [0] * len(trial_list)
#     for ii in range(len(trial_list)):
#         current_trial = trial_list[ii]
#         sum_step = 0
#         for elem in A:
#             if elem == current_trial:
#                 continue
#             elif elem == 7 - current_trial:
#                 sum_step += 2
#             else:
#                 sum_step += 1
#         count_step_list[ii]=sum_step
#     return min(count_step_list)


# A = [1, 6, 2, 3]
# print(solution(A))

# import heapq
#
# def reductionCost(num):
#     heapq.heapify(num)
#     s = 0
#     while len(num) > 1:
#         a1 = heapq.heappop(num)
#         a2 = heapq.heappop(num)
#         s += a1 + a2
#         heapq.heappush(num, a1 + a2)
#     return s
#
# num=[3,1,4,2,-1,3]
# num.sort()
# print(num)
# print(reductionCost(num))
# print(3)

def permutation(s):
    if len(s)==1:
        return [s]
    else:
        res = []
        for i in range(len(s)):
            e = s[i]
            s_ = s[0:i]+s[i+1:]
            tmp = permutation(s_)
            res += [e+x for x in tmp]
        return res
#
# a="aigbc"
# print(len(permutation(a)))
# print(permutation(a))
# a+=[3,4]
#
# print(a)


# def permutationSentence(s):
#     wBag=s.split(" ")
#     if len(wBag)==1:
#         return wBag
#     else:
#         res = []
#         for i in range(len(wBag)):
#             w = wBag[i]
#             wBag_ = wBag[0:i] + wBag[i + 1:]
#             print(wBag_)
#             tmp = permutationSentence(wBag_)
#             print(tmp)
#             res += [w+" "+x for x in tmp]
#         return res
def permutationSentence(s):
    wBag=s.split(" ")
    if len(wBag)==1:
        return wBag
    else:
        res = []
        for i in range(len(wBag)):
            w = wBag[i]
            wBag_ = wBag[0:i] + wBag[i + 1:]
            tmp = permutationSentence(" ".join(wBag_))
            res += [w+" "+x for x in tmp]
        return res


a="This is me too"

print(len(permutationSentence(a)))
print(permutationSentence(a))