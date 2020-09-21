def consecutive(num):
    # if the array starts from n and has length l
    # sum = n*l + (l-1)*l/2
    # n*l = sum - (l-1)*l/2
    # n = sum/l - (l-1)/2

    # iterate over l
    count=0
    l=2
    while (num-(l-1)*l/2)>0:
        if (num - (l-1)*l/2) % l == 0:
            count += 1
        l += 1
    return count

print(consecutive(21))