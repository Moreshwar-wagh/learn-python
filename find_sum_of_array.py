# find the sum of the array

def sum(arr):
    ans = 0
    for i in arr:
        # ans = ans + i
        ans += i
    return ans


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    ans = sum(arr)
    print("Sum of the array is", ans)
# Time complexity: O(n)
# Auxiliary Space: O(1)

# different approach
arr = [12, 3, 4, 15]
ans = sum(arr)
print("Sum of the array is", ans)

# using reduce method
from functools import reduce


def sum(arr):
    sum = reduce(lambda a, b: a + b, arr)
    return sum


arr = [1, 2, 3, 4, 5]
ans = sum(arr)
print("Sum of the array is", ans)
