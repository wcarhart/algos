class Vector:
	"""Dynamically resizing array"""
	def __init__(self):
		self.__arr = []
		self.size = 0
		self.capacity = 0
		self.is_empty = True
		return

	def __str__(self):
		return self.__print()

	def __repr__(self):
		return self.__print()

	def __print(self):
		if self.size == 0:
			return '[]'
		else:
			to_print = '['
			for i in range(0, self.size - 1):
				if isinstance(self.__arr[i], str):
					to_print += "'" + str(self.__arr[i]) + "'" + ', '
				else:
					to_print += str(self.__arr[i]) + ', '
			if isinstance(self.__arr[self.size - 1], str):
				to_print += "'" + str(self.__arr[self.size - 1]) + "'"
			else:
				to_print += str(self.__arr[self.size - 1])
			to_print += ']'
			return to_print

	def __resize(self):
		if self.capacity == 0:
			self.__arr = [None]
			self.capacity = 1
		elif self.size == self.capacity:
			self.__arr = list(self.__arr) + [None]*len(self.__arr)
			self.capacity *= 2

	def __insert(self, index, value):
		if index >= self.size:
			for _ in range(0, index + 1 - self.size):
				self.__resize()
				self.__arr[self.size] = None
				self.size += 1
				self.is_empty = False
		else:
			self.__resize()
			self.size += 1
		self.__arr = self.__arr[:index] + [value] + self.__arr[index:]
		self.is_empty = False

	def __delete(self, index):
		if self.size == 0:
			raise ValueError("Cannot remove from empty vector")
		value = self.__arr[index]
		self.__arr = self.__arr[:index] + self.__arr[index+1:]
		self.size -= 1
		if self.size == 0:
			self.is_empty = True
		return value

	def at(self, index):
		"""Returns value at index"""
		if index >= self.size:
			raise ValueError("Vector index out of bounds")
		return self.__arr[index]

	def print(self):
		"""Prints the vector"""
		print(self.__print())

	def append(self, value):
		"""Appends value to vector"""
		if isinstance(value, list):
			for v in value:
				self.__insert(self.size, v)
		else:
			self.__insert(self.size, value)

	def prepend(self, value):
		"""Prepends value to vector"""
		if isinstance(value, list):
			for v in value:
				self.__insert(0, v)
		else:
			self.__insert(0, value)

	def insert(self, index, value):
		"""Inserts value into vector at index"""
		self.__insert(index, value)

	def pop(self):
		"""Removes (pops) last value from vector"""
		return self.__delete(self.size - 1)

	def delete(self, index):
		"""Deletes value at index"""
		_ = self.__delete(index)

	def remove(self, value):
		"""Removes all instances of value"""
		if not value in self.__arr[:self.size - 1]:
			raise ValueError("Cannot remove value that is not present in vector")
		index = self.__arr[:self.size - 1].index(value)
		self.__delete(index)

	def index(self, value):
		"""Returns first index of value"""
		if value in self.__arr[:self.size - 1]:
			return self.__arr[:self.size - 1].index(value)
		return -1
