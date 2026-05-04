import math

def indexed_search(lst, target):
    n = len(lst)
    block_size = int(math.sqrt(n))

    start = 0
    end = block_size

    while start < n and lst[min(end, n)-1] < target:
        start = end
        end += block_size

    for i in range(start, min(end, n)):
        if lst[i] == target:
            return True
    return False

lst = [5, 10, 15, 20, 25, 30]
target = int(input("Enter element: "))

if indexed_search(lst, target):
    print("Element found")
else:
    print("Element not found")