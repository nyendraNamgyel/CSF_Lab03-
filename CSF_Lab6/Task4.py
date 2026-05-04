def selection_sort_trace(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
        print(f"Pass {i+1}: {lst}")

lst = [64, 25, 12, 22, 11]
selection_sort_trace(lst)