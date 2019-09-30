from linkedlists import LinkedListNode

class Stack:
	def __init__(self, value=None):
		if isinstance(value, list):
			self.top = LinkedListNode(value)
			self.height = 1
			for val in value[1:]:
				self.push(val)
		else:
			self.top = LinkedListNode(value)
			if value:
				self.height = 1
			else:
				self.height = 0

	@property
	def is_empty(self):
		return self.height == 0

	def __contains__(self, value):
		top = self.top
		while top:
			if top.value == value:
				return True
			top = top.next
		return False

	def __iter__(self):
		top = self.top
		while top:
			yield top.value
			top = top.next

	def __add__(self, stack):
		to_return = Stack()
		if self.height > 0:
			for value in self:
				to_return.push(value)
		if stack.height > 0:
			for value in stack:
				to_return.push(value)
		return to_return

	def __iadd__(self, stack):
		if stack.height > 0:
			for value in stack:
				self.push(value)
		return self
	
	def __str__(self):
		return self.__print_stack()

	def __repr__(self):
		return self.__print_stack()

	def print_stack(self):
		"""Print the stack"""
		print(self.__print_stack())

	def __print_stack(self):
		result = []
		for value in self:
			result.append(repr(value))
		return 'top --> ' + '\n        '.join(result[::-1])

	def push(self, value):
		"""Push new value to top of stack"""
		if self.height == 0:
			self.top = LinkedListNode(value)
			self.height = 1
			return
		top = self.top
		while top.next:
			top = top.next
		top.next = LinkedListNode(value)
		self.height += 1

	def pop(self):
		"""Pop value off of top of stack"""
		if self.height == 0:
			return None
		if self.height == 1:
			value = self.top.value
			self.top = LinkedListNode(None)
			self.height = 0
			return value
		top = self.top
		while top.next.next:
			top = top.next
		value = top.next.value
		top.next = None
		self.height -= 1
		return value

	def peek(self):
		"""Peek at value on top of stack"""
		if self.height == 0:
			return None
		if self.height == 1:
			return self.top.value
		top = self.top
		while top.next:
			top = top.next
		return top.value

class TowersOfHanoi:
	# TODO
	def __init__(self):
		return
