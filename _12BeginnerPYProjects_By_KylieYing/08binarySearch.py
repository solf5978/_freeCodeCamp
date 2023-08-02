
def brutal_search(input_arr, target):
    for ind in range(len(input_arr)):
        if input_arr[ind] == target:
            return ind
    return "Not Found"

# Recursive Way
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0;
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint -1)
    else:
        return binary_search(l, target, midpoint + 1, high)

if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(binary_search(test_arr,12))
'''
Direct Way
def bin_search(in_arr, target):
    anchor = (len(in_arr) // 2)
    while True:
        if in_arr[anchor] == target:
            return print(anchor)
        elif in_arr[anchor] > target and anchor != 1:
            anchor += (len(in_arr[:anchor]) // 2)
        elif in_arr[anchor] < target and anchor != len(in_arr) - 1:
            anchor += (len(in_arr[anchor:]) // 2)
        else:
            return print("Not Found")
test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(test_arr))
bin_search(test_arr, 10)
bin_search(test_arr, 12)
'''