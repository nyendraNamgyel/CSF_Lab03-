def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i + 1
    return -1

lst = [10, 20, 30, 40, 50]
target = int(input("Enter element to search: "))

result = linear_search(lst, target)

if result != -1:
    print(f"Element found at position {result}")
else:
    print("Element not found")