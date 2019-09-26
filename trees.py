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
		return self.value == tn.value
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

	def __print_tree(self, prefix, isTail):
		print(prefix + ('└── ' if isTail else '├── ') + str(self.value))
		for index in range(len(self.children) - 1):
			self.children[index].__print_tree(prefix + ('    ' if isTail else '|   '), False)
		if len(self.children) > 0:
			self.children[-1].__print_tree(prefix + ('    ' if isTail else '|   '), True)

class JSONTree:
	"""
	JSON-backed tree implementation
	"""
	def __init__(self, inputfile):
		self.inputfile = inputfile
		self.tree, self.nodes = JSONTreeNode(None).build_tree(inputfile)

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
		return self.value == tn.value
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

	def __print_tree(self, tree, nodes, prefix, isTail):
		print(prefix + ('└── ' if isTail else '├── ') + nodes[tree.value])
		for index in range(len(tree.children) - 1):
			self.__print_tree(tree.children[index], nodes, prefix + ('    ' if isTail else '|   '), False)
		if len(tree.children) > 0:
			self.__print_tree(tree.children[-1], nodes, prefix + ('    ' if isTail else '|   '), True)

class BSTreeNode:
	"""
	Binary Search Tree (BST) implementation
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		"""
		Insert a value into the BST
		"""
		if value < self.value:
			if self.right == None:
				self.right = BSTreeNode(value)
			else:
				self.right.insert(value)
		elif value > self.value:
			if self.left == None:
				self.left = BSTreeNode(value)
			else:
				self.left.insert(value)

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
			if not current.right == None:
				queue.append(current.right)
			if not current.left == None:
				queue.append(current.left)

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
		if not treenode.right == None:
			self.__sorted_traversal(treenode.right)
		print(treenode.value)
		if not treenode.left == None:
			self.__sorted_traversal(treenode.left)

	def get_smallest_element(self, index=1):
		self.___get_smallest_element(self, 0, index)

	def ___get_smallest_element(self, treenode, count, index):
		# TODO: finish this, there's a bug!
		if not treenode.right == None:
			self._sorted

	def get_smallest_element(self, index=1):
		"""
		Get the nth smallest element in the tree
		"""
		stack = []
		item = None
		count = 0
		stack.append(self)
		while not len(stack) == 0:
			treenode = stack.pop()
			print(f'count: {count}')
			print(f'tn value: {treenode.value}')
			if treenode.left == None and treenode.right == None:
				count += 1
			if count == index:
				return treenode.value
			if not treenode.right == None:
				stack.append(treenode.right)
			if not treenode.left == None:
				stack.append(treenode.left)

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

# if __name__ == '__main__':
# 	root = BSTreeNode(3)
# 	root.insert(2)
# 	root.insert(5)
# 	root.insert(7)
# 	root.insert(1)
# 	root.insert(2.5)
# 	root.print_tree_breadth_first()
# 	print(root.dfs(1))
# 	print(root.dfs(99))
# 	root.sorted_traversal()
# 	print(root.get_smallest_element(index=0))

# 	tree, nodes = TreeNode.build_tree('tree.json')
# 	TreeNode.print_tree(tree, nodes)

# 	root = Trie('A', 15)
# 	root.insert('to', 7)
# 	root.insert('tea', 3)
# 	root.insert('ted', 4)
# 	root.insert('ten', 12)
# 	root.insert('i', 11)
# 	root.insert('in', 5)
# 	root.insert('inn', 9)
# 	root.print_trie()
# 	print(root.get('inn'))
# 	root.insert('inn', 10)
# 	print(root.get('inn'))



