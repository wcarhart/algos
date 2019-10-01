from linkedlists import LinkedListNode

class Stack:
	def __init__(self, value=None):
		if isinstance(value, list):
			self.top = LinkedListNode(value[0])
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
		result = []
		while top:
			result.append(top.value)
			top = top.next
		for value in result[::-1]:
			yield value

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
		return 'top --> ' + '\n        '.join(result)

	def clone(self):
		"""Deep clone a stack"""
		if self.height == 0:
			return Stack()
		temp = Stack()
		clone = Stack()
		for value in self:
			temp.push(value)
		for value in temp:
			clone.push(value)
		return clone

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
	def __init__(self, disks=3, starting_tower='a'):
		assert disks > 0, 'Too few disks'
		assert disks < 1000, 'Too many disks'
		self.tower_a = Stack()
		self.tower_b = Stack()
		self.tower_c = Stack()
		self.__configure_towers(disks, starting_tower)

	def __configure_towers(self, disks, starting_tower):
		if starting_tower.lower() == 'a':
			for index in range(disks, 0, -1):
				self.tower_a.push(f'Disk {index}')
		elif starting_tower.lower() == 'b':
			for index in range(disks, 0, -1):
				self.tower_b.push(f'Disk {index}')
		elif starting_tower.lower() == 'c':
			for index in range(disks, 0, -1):
				self.tower_c.push(f'Disk {index}')
		else:
			raise ValueError('Invalid starting tower')

	def __str__(self):
		return self.__print_tower()

	def __repr__(self):
		return self.__print_tower()

	def print_tower(self):
		"""Print the tower"""
		print(self.__print_tower())

	def __print_tower(self):
		tower_a = self.tower_a.clone()
		tower_b = self.tower_b.clone()
		tower_c = self.tower_c.clone()
		result = '    |         |         |    \n'
		height = max(tower_a.height, tower_b.height, tower_c.height)
		while height > 0:
			stra = strb = strc = '    |    '
			if tower_a.height == height:
				val = tower_a.pop()
				stra = f' {val}{"" if len(val) > 7 else " " if len(val) > 6 else "  "}'
			if tower_b.height == height:
				val = tower_b.pop()
				strb = f' {val}{"" if len(val) > 7 else " " if len(val) > 6 else "  "}'
			if tower_c.height == height:
				val = tower_c.pop()
				strc = f' {val}{"" if len(val) > 7 else " " if len(val) > 6 else "  "}'
			layer = f'{stra} {strb} {strc}'
			result += layer + '\n'
			height -= 1
		
		result += '========= ========= ========='
		result += '\n    A         B         C    '
		return result

	def move(self, source, destination):
		"""Move a disk"""
		source_disk = getattr(self, source).peek()
		assert source_disk, f"Illegal move, can't move from an empty tower!"
		dest_disk = getattr(self, destination).peek()
		if dest_disk:
			if int(dest_disk.split()[-1]) < int(source_disk.split()[-1]):
				raise ValueError(f"Illegal move, can't move {source_disk} to tower {destination.split('_')[-1].upper()} because {source_disk} is bigger than the {dest_disk}")
		source_disk = getattr(self, source).pop()
		getattr(self, destination).push(source_disk)

	def solve(self, show_steps=False, show_towers=False):
		"""Solve the Towers of Hanoi"""
		height_a = self.tower_a.height
		height_b = self.tower_b.height
		height_c = self.tower_c.height
		n = -1
		if height_a:
			assert not height_b, "tower B isn't empty!"
			assert not height_c, "tower C isn't empty!"
			n = height_a
			source = 'tower_a'
			destination = 'tower_c'
			other = 'tower_b'
		elif height_b:
			assert not height_a, "tower A isn't empty!"
			assert not height_c, "tower C isn't empty!"
			n = height_b
			source = 'tower_b'
			destination = 'tower_c'
			other = 'tower_a'
		elif height_c:
			assert not height_a, "tower A isn't empty!"
			assert not height_b, "tower B isn't empty!"
			n = height_c
			source = 'tower_c'
			destination = 'tower_a'
			other = 'tower_b'
		assert n, "All the towers are empty!"

		moves = self.__solve(n, source, destination, other, 0, show_steps, show_towers)
		if show_towers:
			print()
			print(self)
		return moves

	def __solve(self, n, source, destination, other, moves, show_steps, show_towers):
		if n == 0:
			return moves
		moves = self.__solve(n-1, source, other, destination, moves, show_steps, show_towers)
		if show_towers:
			print()
			print(self)
		if show_steps:
			print(f"Moving disk from {source.split('_')[-1].upper()} to {destination.split('_')[-1].upper()}")
		self.move(source, destination)
		moves += 1
		moves = self.__solve(n-1, other, destination, source, moves, show_steps, show_towers)
		return moves

if __name__ == '__main__':
	t = TowersOfHanoi()
	t.solve(show_steps=True)
	print(t)
	# moves = t.solve(show_towers=True)
	# print(moves)
	# # print(t)
