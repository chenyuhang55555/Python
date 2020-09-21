
def countBalancingElements(arr):
    odd_all_sum = sum([arr[i] for i in range(0, len(arr), 2)])
    even_all_sum = sum([arr[i] for i in range(1, len(arr), 2)])

    even_left = 0
    odd_left = 0
    count = 0
    for i in range(len(arr)):
        if (i+1)%2 == 1: # itself is in odd position
            even_left += arr[i-1] if (i - 1 >= 0) else 0
            odd_right = odd_all_sum - odd_left - arr[i]
            even_right = even_all_sum - even_left
        elif (i+1)%2 == 0: # itself is in even position
            odd_left += arr[i - 1] if (i - 1 >= 0) else 0
            odd_right = odd_all_sum - odd_left
            even_right = even_all_sum - even_left - arr[i]
        if (even_left + odd_right) == (odd_left + even_right):
            count += 1
    return count

a = [5,5,2,5,8]
print(countBalancingElements(a))