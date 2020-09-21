def solution(A):
    ## No two adjecent trees need to be cut at the same time
    if len(A)==1:
        return 0

    even=(len(A)%2==0)

    first_is_low_violations = 0
    A1 = [100001]+A+[1 if even else 100001]
    for i in range(1,len(A1)-1,2):
        if (A1[i]>=A1[i-1]) or (A1[i]>=A1[i+1]):
            first_is_low_violations += 1

    first_is_high_violations = 0
    A2 = [1]+A+[100001 if even else 1]
    for i in range(2,len(A2)-1,2):
        if (A2[i] >= A2[i - 1]) or (A2[i] >= A2[i + 1]):
            first_is_high_violations += 1

    return min(first_is_high_violations,first_is_low_violations)

A=[5,4,3,2,6,7]
# A=[5,4,3,2,6,7,8]
# A=[3,7,4,5]
# A=[5,5]
print(solution(A))

def solution(A):
    if len(A) <= 2:
        return 0

    trim = [0] * len(A)

    for i in range(len(A)):
        if i == 0:
            if A[i] >= A[i+1]:
                trim[i] = 1
            continue

        if i == len(A) - 1:
            if A[i] >= A[i-1]:
                trim[i] = 1
            continue

        if A[i] >= A[i+1] or A[i] >= A[i-1]:
            trim[i] = 1

    even_sum = 0
    odd_sum = 0
    for j in range(len(trim)):
        if trim[j] == 1:
            if j % 2 == 0:
                even_sum += 1
            else:
                odd_sum += 1

    return min(even_sum, odd_sum)