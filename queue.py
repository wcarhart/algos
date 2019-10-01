from linkedlists import LinkedListNode

class Queue:
	"""Basic queue implementation"""
	def __init__(self, value=None):
		if isinstance(value, list):
			self.head = LinkedListNode(value[0])
			self.tail = self.head
			self.length = 1
			for val in value[1:]:
				self.enqueue(val)
		else:
			self.head = LinkedListNode(value)
			if value:
				self.length = 1
				self.tail = self.head
			else:
				self.length = 0
				self.tail = None

	@property
	def is_empty(self):
		return self.length == 0

	def __contains__(self, value):
		head = self.head
		while head:
			if head.value == value:
				return True
			head = head.next
		return False

	def __iter__(self):
		head = self.head
		while head:
			yield head.value
			head = head.next

	def __add__(self, q):
		to_return = Queue()
		if self.length > 0:
			for value in self:
				to_return.enqueue(value)
		if q.length > 0:
			for value in q:
				to_return.enqueue(value)
		return to_return

	def __iadd__(self, q):
		if q.length > 0:
			for value in q:
				self.enqueue(value)
		return self

	def __str__(self):
		return self.__print_queue()

	def __repr__(self):
		return self.__print_queue()

	def print_queue(self):
		"""Print the queue"""
		print(self.__print_queue())

	def __print_queue(self):
		head = self.head
		result = ''
		while head:
			result += f'{head.value} --> '
			head = head.next
		return result

	def enqueue(self, value):
		"""Enqueue new value to end of queue"""
		if self.length == 0:
			self.head = LinkedListNode(value)
			self.tail = self.head
			self.length = 1
			return
		new_node = LinkedListNode(value)
		self.tail.next = new_node
		self.tail = self.tail.next
		self.length += 1

	def dequeue(self):
		"""Dequeue new value from front of queue"""
		if self.length == 0:
			return None
		new_head = self.head.next
		value = self.head.value
		self.head = new_head
		self.length -= 1
		return value

if __name__ == '__main__':
	q = Queue()
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q)
	print(f'length: {q.length}')
	item = q.dequeue()
	print(f'item: {item}')
	print(q)
	print(f'length: {q.length}')

