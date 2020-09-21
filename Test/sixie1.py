def solution(T):
    # write your code in Python 3.6
    T_no_dup = list(dict.fromkeys(T))
    return min(len(T_no_dup), len(T)//2)

# mylist = ["a", "b", "a", "c", "c"]
# # mylist = list(dict.fromkeys(mylist))
# mylist = dict.fromkeys(mylist)
# print(mylist)
T = [3, 4, 7, 7, 6, 6]
T = [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]
print(solution(T))