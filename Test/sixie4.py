def solution(A):
    l = len(A)

    if l == 1:
        return 0

    current_val = A[0]

    # double pointers
    i=0
    j=l-1
    flag = True
    while i<=j:
        if flag:
            if A[j] != current_val:
                return j
            j -= 1
        else:
            if A[i] != current_val:
                return l-1-i
            i += 1
        flag = not flag
    return 0

A=[4,1,2,3,3,1,1,1]
# A=[1,1,1,1,1,1,1,1]
# A=[1,1,1,1,1,1,1]
A = list(range(75001))
A = [1]*75001

print(solution(A))