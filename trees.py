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

	@staticmethod
	def build_tree(inputfile):
		"""
		Build tree from a JSON file of edges and nodes
		"""
		with open(inputfile, 'r') as f:
			json_content = json.load(f)

		# TODO: define JSON schema
		nodes = {node['id']: node['value'] for node in json_content['nodes']}
		edges = {edge['child']: edge['parent'] for edge in json_content['edges']}
		TreeNode._validate_json_content(nodes, edges)
		remove = [edge for edge in edges if edges[edge] == ''][0]
		del edges[remove]

		forest = []
		for node, parent in edges.items():
			if len(forest) == 0:
				tn = TreeNode(parent)
				tn.children += [TreeNode(node)]
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
						node_in_question.children += [TreeNode(node)]
						found = True
						break
				if found:
					break
			if not found:
				tn = TreeNode(parent)
				tn.children += [TreeNode(node)]
				forest += [tn]

		tree = TreeNode.merge_forest(forest)
		return tree, nodes

	@staticmethod
	def _validate_json_content(nodes, edges):
		assert len(list(nodes.keys())) == len(list(set(nodes.keys()))), "Invalid tree structure, found duplicate ids in 'nodes' field in JSON"
		assert len(list(nodes.keys())) == len(list(set(edges.keys()))), "Invalid tree structure, not enough edges in 'edges' field in JSON"
		assert len(list(edges.keys())) == len(list(set(edges.keys()))), "Invalid tree structure, found duplicates in 'edges' field in JSON"

	@staticmethod
	def merge_forest(forest):
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

	@staticmethod
	def print_tree(tree, nodes):
		"""
		Recursively print a tree
		"""
		TreeNode._print_tree(tree, nodes, '', True)

	@staticmethod
	def _print_tree(tree, nodes, prefix, isTail):
		print(prefix + ('└── ' if isTail else '├── ') + nodes[tree.value])
		for index in range(len(tree.children) - 1):
			TreeNode._print_tree(tree.children[index], nodes, prefix + ('    ' if isTail else '|   '), False)
		if len(tree.children) > 0:
			TreeNode._print_tree(tree.children[-1], nodes, prefix + ('    ' if isTail else '|    '), True)

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
		return self._dfs(self, value)

	def _dfs(self, treenode, value):
		if treenode == None:
			return False
		if treenode.value == value:
			return True
		return self._dfs(treenode.left, value) or self._dfs(treenode.right, value)

	def sorted_traversal(self):
		"""
		Print the tree in sorted order via DFS
		"""
		self._sorted_traversal(self)

	def _sorted_traversal(self, treenode):
		if not treenode.right == None:
			self._sorted_traversal(treenode.right)
		print(treenode.value)
		if not treenode.left == None:
			self._sorted_traversal(treenode.left)

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
			if treenode.left == None and treenode.right == None:
				count += 1
			if count == index:
				return treenode.value
			if not treenode.left == None:
				stack.append(treenode.left)
			if not treenode.right == None:
				stack.append(treenode.right)

if __name__ == '__main__':
	# root = BSTreeNode(3)
	# root.insert(2)
	# root.insert(5)
	# root.insert(7)
	# root.insert(1)
	# root.insert(2.5)
	# root.print_tree_breadth_first()
	# print(root.dfs(1))
	# print(root.dfs(99))
	# root.sorted_traversal()
	# print(root.get_smallest_element(index=2))

	tree, nodes = TreeNode.build_tree('tree.json')
	TreeNode.print_tree(tree, nodes)



