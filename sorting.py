from heap import MaxHeap
from random import randint

def unsort(arr):
	"""
	We pick a random index in the array. Then, we pull out the value at that
	index and save it in our result. Finally, we pop the last element in the 
	array and move it into the random index. We repeat this until our original
	array is empty and our result is full.
	"""
	to_return = []
	for i in range(0, len(arr)):
		index = randint(0, len(arr)-1)
		to_return.append(arr[index])
		arr[index] = arr[-1]
		arr.pop()
	return to_return

def binarysearch(arr, value):
	"""
	We continuously halve the input array, which we assume is sorted. If the
	value at our midpoint is our search target, we return true. Otherwise, we
	search the upper half of the array if the value at our midpoint is less
	than our search target or the lower half of the array if the value of our
	midpoint is greater than our search target. We continue until we've
	exhausted the whole array.
	"""
	return __binarysearch(arr, value, 0, len(arr) - 1)

def __binarysearch(arr, value, lo, hi):
	mid = int((lo + hi) / 2)
	if arr[mid] == value:
		return mid
	if lo == hi:
		return -1
	if arr[mid] > value:
		return __binarysearch(arr, value, lo, mid)
	return __binarysearch(arr, value, mid+1, hi)

def bubblesort(arr):
	"""
	We iterate through each item in the array. If the item is bigger than the
	item directly to the right of it, we swap the two elements. This causes the
	smallest elements to "bubble" up to the front of the array.
	"""
	is_sorted = False
	while not is_sorted:
		is_sorted = True
		for i in range(0, len(arr) - 1):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				is_sorted = False

def bubblesort_improved(arr):
	"""
	Bubble sort iterates through the whole array over and over. With each
	iteration, we can observe that the greatest element gets slotted into the
	correct index, until the whole array is sorted. Thus, for an unsorted array
	of n numbers, we only need to compare the first n-1 numbers; we can shrink
	the end index by one during each iteration.
	"""
	is_sorted = False
	last_unsorted = len(arr) - 1
	while not is_sorted:
		is_sorted = True
		for i in range(0, last_unsorted):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				is_sorted = False
		last_unsorted -= 1

def cocktailshakersort(arr):
	"""
	Improving on bubblesort_improved, we can use the same strategy with the
	start index, so the elements of the array bubble up and down with each
	iteration, effectively shrinking our unsorted portion on both ends.
	"""
	is_sorted = False
	start_index = 0
	end_index = len(arr) - 1
	while not is_sorted:
		is_sorted = True
		for i in range(start_index, end_index):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				is_sorted = False
		end_index -= 1
		for i in range(end_index, start_index, -1):
			if arr[i] < arr[i-1]:
				arr[i], arr[i-1] = arr[i-1], arr[i]
				is_sorted = False
		start_index += 1

def insertionsort(arr):
	"""
	We segment the array into two portions: sorted and unsorted. Initially, the
	sorted section is just the first element in the array. Then, we take an
	element from the unsorted section and "insert" it into the sorted section.
	We do this by removing the element from the array (creating a slot), and
	then shifting the sorted portion up by one before inserting the element
	back into its correct index.
	"""
	for i in range(1, len(arr)):
		temp = arr[i]
		slot = i
		while slot > 0 and arr[slot-1] > temp:
			arr[slot] = arr[slot-1]
			slot -= 1
		arr[slot] = temp

# TODO
def mergesort(arr):
	return

# TODO
def shellsort(arr):
	return

# TODO
def quicksort(arr):
	return

# TODO
def selectionsort(arr):
	return

# TODO
def doubleselectionsort(arr):
	return

# TODO
def heapsort(arr):
	return

# TODO
def radixsort(arr):
	return

# TODO
def bogosort(arr):
	return

if __name__ == '__main__':
	# arr = [1,2,3,4,5]
	# print(unsort(arr))
	# print('bubble sort')
	# arr = [3, 2, 5, 1, 4, 6, 8, 10, 0, 9, 7]
	# bubblesort(arr)
	# print(arr)

	# print('bubble sort improved')
	# arr = [3, 2, 5, 1, 4, 6, 8, 10, 0, 9, 7]
	# bubblesort_improved(arr)
	# print(arr)
	# cocktailshakersort(arr)
	# insertionsort(arr)
	# print(arr)

	# arr = list(range(0, 20))
	# arr = unsort(arr)
	# print(arr)
	# insertionsort(arr)
	# print(arr)

	arr = list(range(0, 20, 2))
	for i in range(-10, 25):
		print(f'{i}: {binarysearch(arr, i)}')











