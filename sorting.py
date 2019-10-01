from heap import MaxHeap
from random import randint
from copy import deepcopy
import sys

def unsort(arr):
	"""
	We pick a random index in the array. Then, we pull out the value at that
	index and save it in our result. Finally, we pop the last element in the 
	array and move it into the random index. We repeat this until our original
	array is empty and our result is full.
	"""
	clone = deepcopy(arr)
	to_return = []
	for i in range(0, len(clone)):
		index = randint(0, len(clone)-1)
		to_return.append(clone[index])
		clone[index] = clone[-1]
		clone.pop()
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

def mergesort(arr):
	"""
	This algorithm builds off the concept of merging arrays. Merging two sorted
	arrays is easy; we use two pointers, one per array, and merge the arrays 
	by iterating through each one. Building off of this, we can split our input
	array down into subarrays of size one, and then go about merging them like
	we would two larger, sorted arrays.
	"""
	for index, value in enumerate(__mergesort(arr)):
		arr[index] = value

def __mergesort(arr):
	if len(arr) <= 1:
		return arr
	mid = int(len(arr) / 2)
	left = __mergesort(arr[:mid])
	right = __mergesort(arr[mid:])
	return merge(left, right)

def merge(left, right):
	result = []
	left_pointer = right_pointer = 0
	while left_pointer < len(left) and right_pointer < len(right):
		if left[left_pointer] < right[right_pointer]:
			result.append(left[left_pointer])
			left_pointer += 1
		else:
			result.append(right[right_pointer])
			right_pointer += 1
	result += left[left_pointer:]
	result += right[right_pointer:]
	return result

# TODO
def shellsort(arr):
	return

def quicksort(arr):
	"""
	Basic quick sort implementation. We start by designating the last item in
	our array as the "pivot." Then, we segment the portion of our array before
	our pivot as our "range." The range is the portion of the array that we are
	trying to sort. For each item in the range, if it is bigger than our pivot,
	then we move the item out of the range and behind the pivot. At the end of
	this iteration, our pivot is slotted into its correct position in the
	sorted array. In addition, all of the elements before the pivot are less
	than the pivot, while all the elements after the pivot are greater. We then
	repeat this process with the subarrays before and after our pivot until the
	whole array is sorted.
	"""
	__quicksort(arr, 0, len(arr)-1)

def __quicksort(arr, start, end):
	if start >= end:
		return
	pivot = arr[end]
	range_start = start
	range_end = end - 1
	while range_start <= range_end:
		if arr[range_start] > pivot:
			if range_end == range_start:
				arr[range_end+1], arr[range_start] = arr[range_start], arr[range_end+1]
			else:
				temp = arr[range_end]
				arr[range_end] = arr[range_end + 1]
				arr[range_end + 1] = arr[range_start]
				arr[range_start] = temp
			range_end -= 1
		else:
			range_start += 1
	__quicksort(arr, start, range_end)
	__quicksort(arr, range_end+2, end)

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

def bogosort(arr):
	"""
	We generate a random permutation of our input array. If this permutation is
	sorted, we are done. If it is not, we generate a new permutation and
	continue.
	"""
	clone = deepcopy(arr)
	is_sorted = False
	while not is_sorted:
		clone = unsort(clone)
		is_sorted = True
		for index in range(0, len(clone)-1):
			if clone[index] > clone[index+1]:
				is_sorted = False
	for index, item in enumerate(clone):
		arr[index] = item

if __name__ == '__main__':
	arr = unsort(list(range(0, 40)))
	print(arr)
	quicksort(arr)
	print(arr)











