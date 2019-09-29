import sys
import json

class TreeNode:
	"""
	Regular tree implementation
	"""
	def __init__(self, value):
		self.value = value
		self.children = []

	def __eq__(self, tn):
		return self.value == (None if tn == None else tn.value) and self.children == (None if tn == None else tn.children)

	def __lt__(self, tn):
		return self.value < tn.value

	def contains(self, value):
		return self.value == value or any(child.contains(value) for child in self.children)

	def total(self):
		if len(self.children) == 0:
			return 1
		return 1 + sum(child.total() for child in self.children)

	def print_tree(self):
		"""
		Recursively print a tree
		"""
		self.__print_tree('', True)

	def __print_tree(self, prefix, is_tail):
		print(prefix + ('└── ' if is_tail else '├── ') + str(self.value))
		for index in range(len(self.children) - 1):
			self.children[index].__print_tree(prefix + ('    ' if is_tail else '|   '), False)
		if len(self.children) > 0:
			self.children[-1].__print_tree(prefix + ('    ' if is_tail else '|   '), True)

class JSONTree:
	"""
	JSON-backed tree implementation
	"""
	def __init__(self, inputfile):
		self.inputfile = inputfile
		self.tree, self.nodes = JSONTreeNode(None).build_tree(inputfile)

	def __eq__(self, t):
		return self.tree == (None if t == None else t.tree)

	def print_tree(self):
		self.tree.print_tree(self.tree, self.nodes)

class JSONTreeNode:
	"""
	JSON-backed tree node implementation
	"""
	def __init__(self, value):
		self.value = value
		self.children = []

	def __eq__(self, tn):
		return self.value == (None if tn == None else tn.value) and self.children == (None if tn == None else tn.children)

	def __lt__(self, tn):
		return self.value < tn.value

	def contains(self, value):
		return self.value == value or any(child.contains(value) for child in self.children)

	def total(self):
		if len(self.children) == 0:
			return 1
		return 1 + sum(child.total() for child in self.children)

	def build_tree(self, inputfile):
		"""
		Build tree from a JSON file of edges and nodes
		"""
		with open(inputfile, 'r') as f:
			json_content = json.load(f)

		nodes = {node['id']: node['value'] for node in json_content['nodes']}
		edges = {edge['child']: edge['parent'] for edge in json_content['edges']}
		self.__validate_json_content(nodes, edges)
		remove = [edge for edge in edges if edges[edge] == ''][0]
		del edges[remove]

		forest = []
		for node, parent in edges.items():
			if len(forest) == 0:
				tn = JSONTreeNode(parent)
				tn.children += [JSONTreeNode(node)]
				forest += [tn]
				continue
			found = False
			for index, tree in enumerate(forest):
				nodes_to_process = [tree]
				while not len(nodes_to_process) == 0:
					node_in_question = nodes_to_process.pop()
					if not len(node_in_question.children) == 0:
						nodes_to_process += node_in_question.children
					if node_in_question.value == parent:
						node_in_question.children += [JSONTreeNode(node)]
						found = True
						break
				if found:
					break
			if not found:
				tn = JSONTreeNode(parent)
				tn.children += [JSONTreeNode(node)]
				forest += [tn]

		tree = self.merge_forest(forest)
		return tree, nodes

	def __validate_json_content(self, nodes, edges):
		assert len(list(nodes.keys())) == len(list(set(nodes.keys()))), "Invalid tree structure, found duplicate ids in 'nodes' field in JSON"
		assert len(list(nodes.keys())) == len(list(set(edges.keys()))), "Invalid tree structure, not enough edges in 'edges' field in JSON"
		assert len(list(edges.keys())) == len(list(set(edges.keys()))), "Invalid tree structure, found duplicates in 'edges' field in JSON"

	def merge_forest(self, forest):
		"""
		Merge a forest of trees into a single tree
		"""
		if len(forest) == 1:
			return forest[0]

		final_tree = forest.pop()
		trees_to_process = forest
		while not len(trees_to_process) == 0:
			tree_in_question = trees_to_process.pop(0)
			if final_tree.contains(tree_in_question.value):
				nodes_to_process = [final_tree]
				while not len(nodes_to_process) == 0:
					node_in_question = nodes_to_process.pop()
					if node_in_question.value == tree_in_question.value:
						node_in_question.children += [tree_in_question]
						break
					else:
						if not len(node_in_question.children) == 0:
							nodes_to_process += node_in_question.children
			else:
				trees_to_process += [final_tree]
				final_tree = tree_in_question
		return final_tree

	def print_tree(self, tree, nodes):
		"""
		Recursively print a tree
		"""
		self.__print_tree(tree, nodes, '', True)

	def __print_tree(self, tree, nodes, prefix, is_tail):
		print(prefix + ('└── ' if is_tail else '├── ') + nodes[tree.value])
		for index in range(len(tree.children) - 1):
			self.__print_tree(tree.children[index], nodes, prefix + ('    ' if is_tail else '|   '), False)
		if len(tree.children) > 0:
			self.__print_tree(tree.children[-1], nodes, prefix + ('    ' if is_tail else '|   '), True)

class BSTreeNode:
	"""
	Binary Search Tree (BST) implementation
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def __eq__(self, tn):
		return self.value == (None if tn == None else tn.value) and self.left == (None if tn == None else tn.left) and self.right == (None if tn == None else tn.right)

	def __str__(self):
		lines, _, _, _ = self.__display()
		return '\n'.join(lines)

	def __repr__(self):
		lines, _, _, _ = self.__display()
		return '\n'.join(lines)

	def insert(self, value):
		"""
		Insert a value into the BST
		"""
		if value > self.value:
			if self.right == None:
				self.right = BSTreeNode(value)
			else:
				self.right.insert(value)
		elif value < self.value:
			if self.left == None:
				self.left = BSTreeNode(value)
			else:
				self.left.insert(value)

	def __insert_tree(self, t):
		"""
		Insert a subtree into the BST
		"""
		if not t:
			return
		if t.value > self.value:
			if self.right == None:
				self.right = t
			else:
				self.right.__insert_tree(t)
		elif t.value < self.value:
			if self.left == None:
				self.left = t
			else:
				self.left.__insert_tree(t)

	def display(self):
		lines, _, _, _ = self.__display()
		for line in lines:
			print(line)

	def __display(self):
		"""Returns list of strings, width, height, and horizontal coordinate of the root"""
		# no child
		if self.right is None and self.left is None:
			line = '%s' % self.value
			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle

		# only left child
		if self.right is None:
			lines, n, p, x = self.left.__display()
			s = '%s' % self.value
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
			second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
			shifted_lines = [line + u * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

		# only right child
		if self.left is None:
			lines, n, p, x = self.right.__display()
			s = '%s' % self.value
			u = len(s)
			first_line = s + x * '_' + (n - x) * ' '
			second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
			shifted_lines = [u * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

		# two children
		left, n, p, x = self.left.__display()
		right, m, q, y = self.right.__display()
		s = '%s' % self.value
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
		second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
		if p < q:
			left += [n * ' '] * (q - p)
		elif q < p:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u, max(p, q) + 2, n + u // 2

	def print_tree_breadth_first(self):
		"""
		Print the tree level-by-level
		"""
		queue = []
		queue.append(self)
		queue.append(None)
		while len(queue) > 0:
			current = queue.pop(0)
			if current == None:
				print('')
				if len(queue) > 0:
					queue.append(None)
				continue
			print(str(current.value) + ' ', end='')
			if not current.left == None:
				queue.append(current.left)
			if not current.right == None:
				queue.append(current.right)

	def dfs(self, value):
		"""
		Depth first search (DFS) the BST
		"""
		return self.__dfs(self, value)

	def __dfs(self, treenode, value):
		if treenode == None:
			return False
		if treenode.value == value:
			return True
		return self.__dfs(treenode.left, value) or self.__dfs(treenode.right, value)

	def sorted_traversal(self):
		"""
		Print the tree in sorted order via DFS
		"""
		self.__sorted_traversal(self)

	def __sorted_traversal(self, treenode):
		if not treenode.left == None:
			self.__sorted_traversal(treenode.left)
		print(treenode.value)
		if not treenode.right == None:
			self.__sorted_traversal(treenode.right)

	def get_smallest_element(self, n=1):
		"""
		Get the kth smallest element
		"""
		stack = [self]
		smallest = None
		count = 0
		while count < n and stack:
			item = stack.pop()
			if isinstance(item, BSTreeNode):
				if not item.right == None:
					stack.append(item.right)
				stack.append(item.value)
				if not item.left == None:
					stack.append(item.left)
				continue
			count += 1
			smallest = item
		if count < n:
			return None
		return smallest

	def count_nodes(self):
		"""Get the number of nodes in the tree"""
		return self.__count_nodes(self)

	def __count_nodes(self, treenode):
		if treenode == None:
			return 0
		return 1 + self.__count_nodes(treenode.left) + self.__count_nodes(treenode.right)

	def get_height(self):
		"""Get the height of the tree"""
		return self.__get_height(self)

	def __get_height(self, treenode):
		if treenode == None:
			return 0
		return 1 + max(self.__get_height(treenode.left), self.__get_height(treenode.right))

	def get_min(self):
		"""Get smallest value in tree"""
		if self.left:
			return self.left.get_min()
		return self.value

	def get_max(self):
		"""Get largest value in tree"""
		if self.right:
			return self.right.get_max()
		return self.value

	def remove(self, value):
		"""Removes value from tree, if it exists"""
		self.__remove(self, value, None)

	def __remove(self, treenode, value, previous):
		if treenode == None:
			return None
		if value < treenode.value:
			return self.__remove(treenode.left, value, treenode)
		elif value > treenode.value:
			return self.__remove(treenode.right, value, treenode)
		else:
			if treenode.left:
				temp = treenode.left.right
				treenode.value = treenode.left.value
				treenode.left = treenode.left.left
				treenode.right.__insert_tree(temp)
			elif treenode.right:
				treenode.value = treenode.right.value
				treenode.right = treenode.right.right
			else:
				if previous.right:
					if previous.right.value == value:
						previous.right = None
				if previous.left:
					if previous.left.value == value:
						previous.left = None
			return value

	def get_successor(self, value):
		"""Get the next biggest value in the tree"""
		stack = [self]
		current = None
		previous = None
		while not previous == value and stack:
			item = stack.pop()
			if isinstance(item, BSTreeNode):
				if item.right:
					stack.append(item.right)
				stack.append(item.value)
				if item.left:
					stack.append(item.left)
				continue
			previous = current
			current = item
		return current if previous == value else None

class AVLTreeNode(BSTreeNode):
	# TODO
	def __init__(self):
		return

class BubbleTree:
	def __init__(self, path, value=None):
		self.path = path
		self.value = value
		self.children = []

	def __str__(self):
		return self.__print_tree('', True, '')

	def __repr__(self):
		return self.__print_tree('', True, '')

	def __print_tree(self, prefix, is_tail, result):
		result += prefix + ('└── ' if is_tail else '├── ') + str(self.path) + (f' ({self.value})' if self.value else '') + '\n'
		for index in range(len(self.children) - 1):
			result = self.children[index].__print_tree(prefix + ('    ' if is_tail else '|   '), False, result)
		if len(self.children) > 0:
			result = self.children[-1].__print_tree(prefix + ('    ' if is_tail else '|   '), True, result)
		return result

	def insert(self, path, value=None):
		"""Provide a full path to be inserted"""
		items = path.strip('/').split('/')
		assert items[0] == self.path, 'Invalid insert path in tree'
		self.insert_at_path(items[-1], items[:-1], value)

	def insert_at_path(self, path, tree_path, value):
		"""Insert new value at a specific path"""
		self.__insert_at_path(self, path, tree_path, value)

	def __insert_at_path(self, treenode, path, tree_path, value):
		if len(tree_path) == 1:
			if treenode.path == tree_path[0]:
				treenode.children.append(BubbleTree(path, value=value))
			else:
				raise ValueError('Invalid insert path in tree')
		else:
			if len(tree_path) > 1:
				try:
					index = next(i for i, child in enumerate(treenode.children) if child.path == tree_path[1])
					self.__insert_at_path(treenode.children[index], path, tree_path[1:], value)
				except StopIteration:
					treenode.children.append(BubbleTree(tree_path[1]))
					self.__insert_at_path(treenode.children[-1], path, tree_path[1:], value)
			else:
				raise ValueError('Invalid insert path in tree')

	def bubble(self):
		"""Bubble up values in the tree and prune congruent subtrees"""
		self.__bubble(self)

	def __bubble(self, treenode):
		if not treenode.children:
			return
		for child in treenode.children:
			self.__bubble(child)
		if all(child.value == treenode.children[0].value for children in treenode.children):
			treenode.value = treenode.children[0].value
			treenode.children = []

	def flatten(self):
		"""Flatten the tree into key-value pairs"""
		return self.__flatten(self, '', {})

	def __flatten(self, treenode, prefix, result):
		if treenode.value:
			result['/'.join([prefix, treenode.path])] = treenode.value
		else:
			for child in treenode.children:
				result = self.__flatten(child, '/'.join([prefix, treenode.path]), result)
		return result

class Trie:
	"""
	trie implementation
	"""
	def __init__(self, key, value):
		self.root = TrieNode(None, None)
		self.root.insert(key, value)

	def insert(self, key, value):
		self.root.insert(key, value)

	def get(self, key):
		return self.root.get(key)

	def print_trie(self):
		self.root.print_trie(self.root)

class TrieNode:
	"""
	trie node implementation
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.children = []

	def insert(self, key, value):
		self.__insert(key, value, key[1:])

	def __insert(self, key, value, substring):
		key_in_question = key.replace(substring, '', 1)
		if key_in_question in (val.key for val in self.children):
			if key_in_question == key:
				next(child for child in self.children if child.key == key_in_question).value = value
			else:
				next(child for child in self.children if child.key == key_in_question).__insert(key, value, substring[1:])
		else:
			self.children.append(TrieNode(key_in_question, value if key_in_question == key else None))
			if not key_in_question == key:
				next(child for child in self.children if child.key == key_in_question).__insert(key, value, substring[1:])

	def get(self, key):
		return self.__get(key, key[1:])

	def __get(self, key, substring):
		key_in_question = key.replace(substring, '', 1)
		if key_in_question in (val.key for val in self.children):
			if key_in_question == key:
				return next(child for child in self.children if child.key == key_in_question).value
			return next(child for child in self.children if child.key == key_in_question).__get(key, substring[1:])
		else:
			return None

	def print_trie(self, trienode):
		self.__print_trie('')

	def __print_trie(self, prefix):
		if self.key == None:
			label = ''
		else:
			label = f'{self.key} ({"" if self.value == None else self.value}) ' 
		print(f'{prefix}{label}--> {", ".join([val.key for val in self.children])}')
		for child in self.children:
			child.__print_trie(prefix+'    ')
