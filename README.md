# algos
Common algorithms and data structures for safe keeping

## Current progress
- [ ] [Sorting](#sorting)
  - [x] [Unsort](#unsort)
  - [ ] [Binary Search](#binary-search)
  - [x] [Bubble Sort](#bubble-sort)
  - [x] [Bubble Sort (Improved)](#bubble-sort)
  - [x] [Cocktail Shaker Sort](#cocktail-shaker-sort)
  - [x] [Insertion Sort](#insertion-sort)
  - [ ] [Merge Sort](#merge-sort)
  - [ ] [Shell Sort](#shell-sort)
  - [ ] [Quick Sort](#quick-sort)
  - [ ] [Selection Sort](#selection-sort)
  - [ ] [Heap Sort](#heap-sort)
  - [ ] [Radix Sort](#radix-sort)
  - [ ] [Bogo Sort](#bogo-sort)
- [x] [Arrays](#arrays)
  - [x] [Vector](#vector)
- [ ] [Trees](#trees)
  - [x] [Regular Tree](#regular-tree)
  - [x] [JSON Tree](#json-tree)
  - [x] [Binary Search Tree (BST)](#binary-search-tree)
  - [ ] [AVL Tree](#avl-tree)
  - [ ] [Bubble Tree](#bubble-tree)
  - [x] [Trie](#trie)
- [ ] [Linked Lists](#linked-lists)
  - [ ] [Regular Linked List](#regular-linked-list)
  - [ ] [Doubly Linked List](#doubly-linked-list)
  - [ ] [Circular Linked List](#circular-linked-list)
  - [ ] [Stack](#stack)
  - [ ] [Queue](#queue)
  - [ ] [Towers of Hanoi](#towers-of-hanoi)
- [ ] [Heaps](#heaps)
  - [ ] [Regular Heap](#regular-heap)
  - [ ] [Max Heap](#max-heap)
  - [ ] [Min Heap](#min-heap)
  - [ ] [Priority Queue](#priority-queue)
- [ ] [Graphs](#graphs)
  - [ ] [Graph](#graph)


## Sorting
<details>
<summary><a id="unsort">Unsort</a></summary>

### Unsort
To be implemented.

</details>

<details>
<summary><a id="binary-sort">Binary Search</a></summary>

### Binary Search
To be implemented.

</details>

<details>
<summary><a id="bubble-sort">Bubble Sort</a></summary>

### Bubble Sort
To be implemented.

</details>

<details>
<summary><a id="cocktail-shaker-sort">Cocktail Shaker Sort</a></summary>

### Cocktail Shaker Sort
To be implemented.

</details>

<details>
<summary><a id="insertion-sort">Insertion Sort</a></summary>

### Insertion Sort
To be implemented.

</details>

<details>
<summary><a id="merge-sort">Merge Sort</a></summary>

### Merge Sort
To be implemented.

</details>

<details>
<summary><a id="shell-sort">Shell Sort</a></summary>

### Shell Sort
To be implemented.

</details>

<details>
<summary><a id="quick-sort">Quick Sort</a></summary>

### Quick Sort
To be implemented.

</details>

<details>
<summary><a id="selection-sort">Selection Sort</a></summary>

### Selection Sort
To be implemented.

</details>

<details>
<summary><a id="heap-sort">Heap Sort</a></summary>

### Heap Sort
To be implemented.

</details>

<details>
<summary><a id="radix-sort">Radix Sort</a></summary>

### Radix Sort
To be implemented.

</details>

## Arrays
<details>
<summary><a id="vector">Vector</a></summary>

### Vector
A dynamically resizeable array. Implemented via the `Vector` class in `vector.py`.

*Create a new vector:*
```
>>> from vector import Vector
>>> v = Vector()
>>> v.size
0
>>> v.capacity
0
>>> v.is_empty
True
>>> v
[]
```

*Vector automatically doubles in size as its size exceeds its capacity:*
```
>>> v
[1, 2, 3]
>>> v.size
3
>>> v.capacity
4
>>> v.append([4, 5, 6])
>>> v
[1, 2, 3, 4, 5, 6]
>>> v.size
6
>>> v.capacity
8
```

*Access elements with `at`:*
```
>>> v
[1, 2, 3]
>>> v.at(1)
2
```

*Vectors are iterable:*
```
>>> v
[1, 2, 3]
>>> l = list(v)
>>> l
[1, 2, 3]
```

*Add to the vector with `prepend`, `append`, and `insert`:*
```
>>> v
[]
>>> v.append('end')
>>> v
['end']
>>> v.prepend('start')
>>> v
['start', 'end']
>>> v.insert(1, 'mid')
>>> v
['start', 'mid', 'end']
```

*`prepend` and `append` work with lists, too:*
```
>>> v
[]
>>> v.append([1, 2, 3])
>>> v
[1, 2, 3]
>>> v.prepend([1, 2, 3])
>>> v
[3, 2, 1, 1, 2, 3]
```

*Remove from the vector with `delete`, `remove`, and `pop`:*
```
>>> v
['a', 'b', 'c', 'd']
>>> v.delete(1)
>>> v
['a', 'c', 'd']
>>> v.remove('d')
>>> v
['a', 'c']
>>> v.pop()
'c'
>>> v
['a']
```

*You can search the vector, too:*
```
>>> v
['red', 'blue', 'green']
>>> v.index('red')
0
>>> v.index('yellow')
-1
```

</details>

## Trees
<details>
<summary><a id="regular-tree">Regular Tree</a></summary>
    
### Regular Tree
A basic tree data structure. Implemented via the `TreeNode` class in `trees.py`.

*Create standard trees and tree nodes:*
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
*Each `TreeNode` has a `value` field and a `children` field:*
```
>>> root = TreeNode(5)
>>> root.value
5
>>> root.children
[]
```
</details>

<details>
<summary><a id="json-tree">JSON Tree</a></summary>

### JSON Tree
A tree data structure that can be built from a JSON file containing a flattened tree represented by lists of nodes and edges. Implemented in the `JSONTree` and `JSONTreeNode` classes in `trees.py`.

*For larger trees, you can store them in a JSON file:*
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
</details>

<details>
<summary><a id="binary-search-tree">Binary Search Tree (BST)</a></summary>

### Binary Search Tree (BST)
A basic BST data structure. Implemented via the `BSTreeNode` class in `trees.py`.

*Construct a BST and insert nodes into it:*
```
>>> from trees import BSTreeNode
>>> root = BSTreeNode(3)
>>> root.insert(2)
>>> root.insert(5)
>>> root.insert(7)
>>> root.insert(1)
>>> root.insert(2.5)
```

*Pretty print the tree:*
```
>>> root.display()
  ___3  
 /    \ 
 2_   5 
/  \   \
1 2.5  7
```

*Print the tree level-by-level, via a breadth-first traversal:*
```
>>> root.print_tree_breadth_first()
3 
2 5 
1 2.5 7 
```

*Perform a depth first search:*
```
>>> root.dfs(5)
True
>>> root.dfs(10)
False
```

*Return a sorted list from the tree, via a depth-first traversal:*
```
>>> root.sorted_traversal()
1
2
2.5
3
5
7
```

*Return the nth smallest number in the tree:*
```
>>> root.get_smallest_element()
1
>>> root.get_smallest_element(n=3)
2.5
```

*Get the number of nodes in the tree:*
```
>>> root.count_nodes()
6
```

*Get the height of a tree:*
```
>>> root.get_height()
3
```

*Get the minimum and maximum values in the tree:*
```
>>> root.get_min()
1
>>> root.get_max()
7
```

*Remove a value from the tree:*
```
>>> root.remove(2)
>>> root.display()
 ___3  
/    \ 
1_   5 
  \   \
 2.5  7
```

*Get the next biggest value in the tree:*
```
>>> root.get_successor(2.5)
3
>>> root.get_successor(7)
None
```

</details>

<details>
<summary><a id="avl-tree">AVL Tree</a></summary>

### AVL Tree
To be implemented.

</details>

<details>
<summary><a id="bubble-tree">Bubble Tree</a></summary>

### Bubble Tree
To be implemented.

</details>

<details>
<summary><a id="trie">Trie</a></summary>
  

### Trie
A basic Trie data structure. Implemented via the `Trie` and `TrieNode` classes in `trees.py`.

*Build a standard trie:*
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

*Retrieve values, similar to a dictionary lookup:*
```
>>> root.get('tea')
3
>>> root.get('bleh')
None
```
</details>

## Linked Lists
<details>
<summary><a id="regular-linked-list">Regular Linked List</a></summary>

### Regular Linked List
To be implemented.

</details>

<details>
<summary><a id="doubly-linked-list">Doubly Linked List</a></summary>

### Doubly Linked List
To be implemented.

</details>

<details>
<summary><a id="circular-linked-list">Circular Linked List</a></summary>

### Circular Linked List
To be implemented.

</details>

<details>
<summary><a id="stack">Stack</a></summary>

### Stack
To be implemented.

</details>

<details>
<summary><a id="queue">Queue</a></summary>

### Queue
To be implemented.

</details>

<details>
<summary><a id="towers-of-hanoi">Towers of Hanoi</a></summary>

### Towers of Hanoi
To be implemented.

</details>

## Heaps
<details>
<summary><a id="regular-heap">Regular Heap</a></summary>

### Regular Heap
To be implemented.

</details>

<details>
<summary><a id="max-heap">Max Heap</a></summary>

### Max Heap
To be implemented.

</details>

<details>
<summary><a id="min-heap">Min Heap</a></summary>

### Min Heap
To be implemented.

</details>

<details>
<summary><a id="priority-queue">Priority Queue</a></summary>

### Priority Queue
To be implemented.

</details>

## Graphs
<details>
<summary><a id="graph">Graph</a></summary>

### Graph
To be implemented.

</details>
