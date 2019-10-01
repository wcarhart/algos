class LinkedListNode:
	"""Node for linked list"""
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedList:
	"""Regular linked list implementation"""
	def __init__(self, value=None):
		if isinstance(value, list):
			self.head = LinkedListNode(value[0])
			self.length = 1
			for val in value[1:]:
				self.append(val)
		else:
			self.head = LinkedListNode(value)
			if value:
				self.length = 1
			else:
				self.length = 0

	@property
	def is_empty(self):
		return self.length == 0

	def __contains__(self, value):
		lili = self.head
		while lili:
			if lili.value == value:
				return True
			lili = lili.next
		return False

	def __iter__(self):
		lili = self.head
		while lili:
			yield lili.value
			lili = lili.next

	def __add__(self, lili):
		to_return = LinkedList()
		if self.length > 0:
			for value in self:
				to_return.append(value)
		if lili.length > 0:
			for value in lili:
				to_return.append(value)
		return to_return

	def __iadd__(self, lili):
		if lili.length > 0:
			for value in lili:
				self.append(value)
		return self

	def __str__(self):
		return self.__print_list()

	def __repr__(self):
		return self.__print_list()

	def print_list(self):
		"""Print the list"""
		print(self.__print_list())

	def __print_list(self):
		lili = self.head
		result = ''
		if lili.value == None:
			return result
		while lili:
			result += f'{repr(lili.value)} --> '
			lili = lili.next
		return result

	def append(self, value):
		"""Append new value to end of list"""
		if self.length == 0:
			self.head = LinkedListNode(value)
			self.length = 1
			return
		lili = self.head
		while lili.next:
			lili = lili.next
		lili.next = LinkedListNode(value)
		self.length += 1

	def prepend(self, value):
		"""Prepend new value to start of list"""
		if self.length == 0:
			self.head = LinkedListNode(value)
			self.length = 1
			return
		new_head = LinkedListNode(value)
		new_head.next = self.head
		self.head = new_head
		self.length += 1

	def insert(self, index, value):
		"""Insert new value into list at index"""
		if self.length == 0:
			self.head = LinkedListNode(value)
			self.length = 1
			return
		if index == 0:
			self.prepend(value)
			return
		lili = self.head
		index -= 1
		count = 0
		while lili:
			if count == index:
				new_node = LinkedListNode(value)
				new_node.next = lili.next
				lili.next = new_node
				self.length += 1
				return
			lili = lili.next
			count += 1
		raise ValueError('Linked list index out of bounds')

	def replace(self, old_value, new_value, count=1):
		"""Replace old_value with new_value in the list count number of times"""
		result = None
		lili = self.head
		instanced_replaced = 0
		while lili:
			if lili.value == old_value:
				lili.value = new_value
				result = old_value
				instanced_replaced += 1
				if instanced_replaced == count:
					break
			lili = lili.next
		return instanced_replaced

	def get_value(self, index):
		"""Retrieve the value at node index"""
		lili = self.head
		result = None
		count = 0
		while lili:
			if count == index:
				result = lili.value
				break
			lili = lili.next
			count += 1
		return result

	def delete(self, index):
		"""Delete the value at index"""
		lili = self.head
		count = 0
		result = previous = None
		while lili:
			if count == index:
				result = lili.value
				if previous:
					previous.next = lili.next
				else:
					self.head = lili.next
				self.length -= 1
				break
			previous = lili
			lili = lili.next
			count += 1
		return result

	def pop(self, index=None):
		"""Pop an element out of the list"""
		return self.delete(index if not index == None else self.length-1)

	def remove(self, value, count=1):
		"""Remove a value from the list, if it exists"""
		lili = self.head
		result = previous = None
		instances_removed = 0
		while lili:
			if lili.value == value:
				result = value
				if previous:
					previous.next = lili.next
				else:
					self.head = lili.next
				self.length -=1
				instances_removed += 1
				if instances_removed == count:
					break
			else:
				previous = lili
			lili = lili.next
		return result

	def reverse(self):
		"""Reverse the list"""
		current = self.head
		previous = None
		next_node = current.next
		while current:
			next_node = current.next
			current.next = previous
			previous = current
			current = next_node
		self.head = previous

	def count(self, value):
		"""Count the number of times value occurs in the list"""
		lili = self.head
		count = 0
		while lili:
			if lili.value == value:
				count += 1
			lili = lili.next
		return count

	def contains_loop(self):
		"""Detects if the list contains a loop"""
		back_pointer = self.head
		if self.head.next:
			front_pointer = self.head.next
		else:
			return False
		while front_pointer:
			if front_pointer.next:
				if front_pointer.next.next:
					front_pointer = front_pointer.next.next
					if front_pointer is back_pointer:
						return True
				else:
					front_pointer = None
			else:
				front_pointer = None
			back_pointer = back_pointer.next
		return False

	def remove_duplicates(self):
		"""Removes duplicates from the list"""
		found = set()
		lili = self.head
		index = 0
		while lili:
			if lili.value in found:
				self.delete(index)
			else:
				found |= {lili.value}
				index += 1
			lili = lili.next

	# TODO: implement with merge sort
	def sort(self):
		return

	def union(self, lili):
		"""Performs a union of two lists, stores result in self"""
		for value in lili:
			self.append(value)
		self.remove_duplicates()

	def intersection(self, lili):
		"""Performs an intersection of two lists, stores result in self"""
		self.remove_duplicates()
		for value in self:
			if not value in lili:
				self.remove(value, count=-1)

	def difference_merge(self, lili):
		"""Performs a merge between two lists where the result is the values that are only present in the first list"""
		for value in self:
			if value in lili:
				self.remove(value, count=-1)

	def zip(self, lili):
		"""Zips (interleaves) two lists together"""
		lili1 = self.head
		lili2 = lili.head
		result = LinkedList()
		while lili1 and lili2:
			result.append(lili1.value)
			result.append(lili2.value)
			lili1 = lili1.next
			lili2 = lili2.next
		if lili1:
			while lili1:
				result.append(lili1.value)
				lili1 = lili1.next
		else:
			while lili2:
				result.append(lili2.value)
				lili2 = lili2.next
		self.head = result.head

	def split(self):
		"""Splits a list into two"""
		lili = self.head
		result1 = LinkedList()
		result2 = LinkedList()
		while lili:
			result1.append(lili.value)
			if lili.next:
				result2.append(lili.next.value)
				lili = lili.next.next
			else:
				lili = lili.next
		self.head = result1.head
		return result2

class DoublyLinkedListNode(LinkedListNode):
	"""Node for doubly linked list"""
	def __init__(self, value):
		super().__init__(value)
		self.previous = None

class DoublyLinkedList:
	# TODO
	def __init__(self, value=None):
		if isinstance(value, list):
			self.head = DoublyLinkedListNode(value[0])
			self.length = 1
			for val in value[1:]:
				self.append(val)
		else:
			self.head = DoublyLinkedListNode(value)
			if value:
				self.length = 1
			else:
				self.length = 0

class CircularLinkedListNode(LinkedListNode):
	"""Node for circular linked list"""
	def __init__(self, value):
		super().__init__(value)

class CircularLinkedList(LinkedList):
	# TODO
	def __init__(self):
		return

if __name__ == '__main__':
	l1 = LinkedList('1')
	l1.append('2')
	l1.append('2')
	l1.append('3')
	l1.append('4')
	l1.append('4')
	l1.append('5')
	l1.append('6')
	l2 = LinkedList(['1', '5', '10', '15', '20'])
	#l3 = l1 + l2
	l3 = (l1 + l2).split()
	print(l1 + l2)
	print(l3)
