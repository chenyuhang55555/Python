# f = open("solution.txt", "w")
#
# f.write("[")
# for i in range(1,100001):
#     f.write(","+str(i))
#
# f.write("]")
# f.close()

import numpy as np
import pandas as pd


def solution(A):
    # write your code in Python 3.6
    trial_list = [1, 2, 3, 4, 5, 6]
    count_step_list = [0] * len(trial_list)
    for ii in range(len(trial_list)):
        current_trial = trial_list[ii]
        sum_step = 0
        for elem in A:
            if elem == current_trial:
                continue
            elif elem == 7 - current_trial:
                sum_step += 2
            else:
                sum_step += 1
        count_step_list[ii]=sum_step
    return min(count_step_list)


A = [1, 6, 2, 3]
print(solution(A))
