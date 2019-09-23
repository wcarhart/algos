# algos
Common algorithms and data structures for safe keeping

## Trees
### Regular Tree
A basic tree data structure. Implemented via the `TreeNode` class in `trees.py`.

*Create standard trees and tree nodes*
```
>>> from trees import TreeNode
>>> root = TreeNode(5)
>>> root.children.append(TreeNode('abc'))
>>> root.children.append(TreeNode('def'))
>>> root.children[0].children.append(TreeNode('1.5'))
>>> root.print_tree()
└── 4
    ├── abc
    |   └── 1.5
    └── def
```
*Each `TreeNode` has a `value` field and a `children` field*
```
>>> root = TreeNode(5)
>>> root.value
5
>>> root.children
[]
```
<hr>

### JSON Tree
A tree data structure that can be built from a JSON file containing nodes and edges. Implemented in the `JSONTree` and `JSONTreeNode` classes in `trees.py`.

*For larger trees, you can store them in a JSON file*
```
>>> from trees import JSONTree, JSONTreeNode
>>> root = JSONTree('tree.json')
>>> root.print_tree()
└── first
    ├── second
    |   └── sixth
    ├── third
    └── fourth
        └── fifth
```
*See [`tree.json`](https://github.com/wcarhart/algos/blob/master/tree.json) for reference*
<hr>

### Binary Search Tree (BST)
A basic BST data structure. Implemented via the `BSTreeNode` class in `trees.py`.

*Construct a BST and insert nodes into it*
```
>>> from trees import BSTreeNode
>>> root = BSTreeNode(3)
>>> root.insert(5)
>>> root.insert(2)
```

*Print the tree level-by-level, via a breadth-first traversal*
```
>>> root.root.print_tree_breadth_first()
3 
2 5 
```

*Perform a depth first search*
```
>>> root.dfs(5)
True
>>> root.dfs(7)
False
```

*Return a sorted list from the tree, via a depth-first traversal*
```
>>> root.sorted_traversal()
2
3
5
```

*Return the nth smallest number in the tree*
```
>>> root.insert(7)
>>> root.insert(1)
>>> root.get_smallest_element()
1
>>> root.get_smallest_element(index=3)
3
```
<hr>

### Trie
A basic Trie data structure. Implemented via the `Trie` and `TrieNode` classes in `trees.py`.

*Build a standard trie*
```
>>> from trees import Trie, TrieNode
>>> root = Trie('to', 5)
>>> root.insert('tea', 3)
>>> root.insert('A', 15)
>>> root.insert('inn', 9)
>>> root.insert('ted', 4)
>>> root.insert('to', 7)
>>> root.insert('i', 11)
>>> root.insert('in', 5)
>>> root.insert('ten', 12)
>>> root.print_trie()
--> A, t, i
    A (15) --> 
    t () --> to, te
        to (7) --> 
        te () --> tea, ted, ten
            tea (3) --> 
            ted (4) --> 
            ten (12) --> 
    i (11) --> in
        in (5) --> inn
            inn (9) --> 
```

*Retrieve values, similar to a dictionary lookup*
```
>>> root.get('tea')
3
>>> root.get('bleh')
None
```

## Linked Lists
To be implemented.

## Heaps
To be implemented.
