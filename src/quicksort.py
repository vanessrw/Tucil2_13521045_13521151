def partition(arr, left, right):
	pivot = arr[right]
	i = left - 1

    # compare ele with pivot
	for j in range(left, right):
		if arr[j] <= pivot:
			i += 1
			# Swap element
			(arr[i], arr[j]) = (arr[j], arr[i])

	# Swap pivot element
	(arr[i + 1], arr[right]) = (arr[right], arr[i + 1])

	# partition position
	return i + 1

def quickSort(arr, left, right):
	if left < right:
		part = partition(arr, left, right)
		quickSort(arr, left, part - 1)
		quickSort(arr, part + 1, right)


#data = [1, 7, 4, 1, 10, 9, -2]
#print("Unsorted Array")
#print(data)

#size = len(data)

#quickSort(data, 0, size - 1)

#print('Sorted Array in Ascending Order:')
#print(data)
