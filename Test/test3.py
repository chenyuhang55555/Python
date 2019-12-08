def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return -1

    def getStatus(current, prev):
        return (current > prev) - (current < prev)

    status = 0  # 0: not counting; -1:going down; 1:going up
    max_depth = -1
    left_depth = -1
    right_depth = -1
    left_peak = A[0]
    prev_elem = A[0]
    prev_status = 0
    for ii in range(1, len(A)):
        status = getStatus(A[ii], prev_elem)
        if status == 0:
            if prev_status == 1:
                right_depth = A[ii] - pit
                if max_depth < left_depth and max_depth < right_depth:
                    max_depth = min(left_depth, right_depth)
            left_depth = -1
            right_depth = -1
            left_peak = A[ii]

        elif status == -1:
            if prev_status == 1:
                left_peak = prev_elem
                right_depth = right_peak - pit
                if max_depth < left_depth and max_depth < right_depth:
                    max_depth = min(left_depth, right_depth)
            elif prev_status == 0:
                left_peak = prev_elem
            elif prev_status == -1:
                pass

        elif status == 1:
            if ii == len(A) - 1 and prev_status != 0:
                right_depth = right_peak - pit
                if max_depth < left_depth and max_depth < right_depth:
                    max_depth = min(left_depth, right_depth)
            else:
                if prev_status == 1:
                    right_peak = A[ii]
                elif prev_status == 0:
                    status = 0
                elif prev_status == -1:
                    right_peak = A[ii]
                    pit = prev_elem
                    left_depth = left_peak - pit

        prev_status = status
        prev_elem = A[ii]
    return max_depth


A = [2, 4, 0, 1, 1, 2, 3, 4, 3, 2]

# A[0] = 0
# A[1] = 1
# A[2] = 3
# A[3] = -2
# A[4] = 0
# A[5] = 1
# A[6] = 0
# A[7] = -3
# A[8] = 2
# A[9] = 3
A += [2, 4, 0, 1, 2, 4, 3, 4, 3, 2]
print(A)
print(solution(A))
