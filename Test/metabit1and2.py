# Hello world!

# Problem1
# input: [0, 2, 0, 3, 0, 5]
# output: [0, 0, 0, 2, 3, 5]

def putZeroFront(lst):
    if len(lst) == 0:
        return lst

    for bottom_pos in range(len(lst) - 1, -1, -1):
        if lst[bottom_pos] == 0:
            break

    for i in range(bottom_pos, -1, -1):
        if lst[i] != 0:
            lst[i], lst[bottom_pos] = lst[bottom_pos], lst[i]
            bottom_pos -= 1
        else:
            pass

    return lst


# print(putZeroFront([0, 2, 0, 3, 0, 5]))
print(putZeroFront([]))
print(putZeroFront([0, 0, 0, 0, 0, 0]))
print(putZeroFront([0, 2, 0, 3, 0, 0, 0, 5]))
print(putZeroFront([2, 0, 3, 0, 5, 0, 0, 0]))
print(putZeroFront([2, 3, 5]))


#  10
#  / \
# 20 30
#    / \
# .  50  100


# Tree is not empty
# Find a non-empty path with max node sum

# output: 80 = 20 + 10 + 30 + 50

class Node:
    left: Node
    right: Node
    val: int


def getMaxPathSum(t):
    def getMaxPathSumHelper(t):
        # t: binary tree
        if t == None:
            return -INTMAX, -INTMAX
        l_maxSumWithin, l_maxSumRoot = getMaxPathSumHelper(t.left)
        r_maxSumWithin, r_maxSumRoot = getMaxPathSumHelper(t.right)
        maxSumWithin = max([r_maxSumWithin, l_maxSumWithin, t.val + l_maxSumRoot + r_maxSumRoot, t.val + l_maxSumRoot,
                            t.val + r_maxSumRoot, t.val])
        maxSumRoot = max([t.val + l_maxSumRoot, t.val + r_maxSumRoot, t.val])
        return maxSumWithin, maxSumRoot

    maxPathSum, _ = getMaxPathSumHelper(t)
    return maxPathSum

