def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

a = [3, 0, 7, 2, 25, 200, 5, 55, 20]

print(a)
quicksort(a)
print(a)