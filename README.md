# algos
Common algorithms and data structures for safe keeping

## Current progress
- [ ] [Sorting](#sorting)
  - [x] [Unsort](#unsort)
  - [x] [Binary Search](#binary-search)
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
  - [x] [Bubble Tree](#bubble-tree)
  - [x] [Trie](#trie)
- [ ] [Linked Lists](#linked-lists)
  - [x] [Regular Linked List](#regular-linked-list)
  - [ ] [Doubly Linked List](#doubly-linked-list)
  - [ ] [Circular Linked List](#circular-linked-list)
  - [x] [Stack](#stack)
  - [ ] [Queue](#queue)
  - [x] [Towers of Hanoi](#towers-of-hanoi)
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
Shuffle an array using the [Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher–Yates_shuffle).
```
>>> from sorting import unsort
>>> arr = list(range(0, 20))
>>> unsort(arr)
[4, 19, 18, 9, 13, 17, 12, 16, 7, 8, 10, 3, 5, 0, 14, 15, 6, 11, 1, 2]
```
* *Best case:* `O(n)`
* *Average case:* `O(n)`
* *Worst case:* `O(n)`

</details>

<details>
<summary><a id="binary-search">Binary Search</a></summary>

### Binary Search
Basic binary search implementation. We continuously halve the input array, which we assume is sorted. If the value at our midpoint is our search target, we return true. Otherwise, we search the upper half of the array if the value at our midpoint is less than our search target or the lower half of the array if the value of our midpoint is greater than our search target. We continue until we've exhausted the whole array.
```
>>> from sorting import binarysearch
>>> arr = list(range(0, 20, 2))
>>> binarysearch(arr, 12)
6
>>> binarysearch(arr, 15)
-1
```
* *Best case:* `O(1)`
* *Average case:* `O(log n)`
* *Worst case:* `O(log n)`

</details>

<details>
<summary><a id="bubble-sort">Bubble Sort</a></summary>

### [Bubble Sort](https://www.youtube.com/watch?v=Cq7SMsQBEUw)
Basic bubble sort implementation. We iterate through each item in the array. If the item is bigger than the item directly to the right of it, we swap the two elements. This causes the smallest elements to "bubble" up to the front of the array.
```
>>> from sorting import bubblesort, unsort
>>> arr = unsort(list(range(0, 20)))
>>> print(arr)
[1, 5, 0, 10, 18, 15, 17, 13, 9, 16, 4, 2, 12, 14, 19, 6, 8, 11, 7, 3]
>>> bubblesort(arr)
>>> print(arr)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

### Bubble Sort (Improved)
Bubble sort implementation with a slight improvement. Bubble sort iterates through the whole array over and over. With each iteration, we can observe that the greatest element gets slotted into the correct index, until the whole array is sorted. Thus, for an unsorted array of n numbers, we only need to compare the first n-1 numbers; we can shrink the end index by one during each iteration.
```
>>> from sorting import bubblesort_improved, unsort
>>> arr = unsort(list(range(0, 20)))
>>> print(arr)
[0, 19, 18, 11, 4, 10, 7, 12, 14, 13, 8, 5, 15, 3, 17, 16, 1, 9, 6, 2]
>>> bubblesort_improved(arr)
>>> print(arr)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```
* *Best case:* `O(n)`
* *Average case:* `O(n^2)`
* *Worst case:* `O(n^2)`
</details>

<details>
<summary><a id="cocktail-shaker-sort">Cocktail Shaker Sort</a></summary>

### [Cocktail Shaker Sort](https://www.youtube.com/watch?v=njClLBoEbfI)
A variation of bubble sort - a double bubble sort. Improving on [Bubble Sort (Improved)](#bubble-sort), we can use the same strategy with the start index, so the elements of the array bubble up and down with each iteration, effectively shrinking our unsorted portion on both ends.
```
>>> from sorting import cocktailshakersort, unsort
>>> arr = unsort(list(range(0, 20)))
>>> print(arr)
[4, 6, 10, 9, 18, 7, 14, 13, 1, 5, 19, 16, 8, 3, 2, 15, 11, 0, 12, 17]
>>> cocktailshakersort(arr)
>>> print(arr)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```
* *Best case:* `O(n)`
* *Average case:* `O(n^2)`
* *Worst case:* `O(n^2)`

</details>

<details>
<summary><a id="insertion-sort">Insertion Sort</a></summary>

### Insertion Sort
Basic insertion sort implementation. We segment the array into two portions: sorted and unsorted. Initially, the sorted section is just the first element in the array. Then, we take an element from the unsorted section and "insert" it into the sorted section. We do this by removing the element from the array (creating a slot), and then shifting the sorted portion up by one before inserting the element back into its correct index.
```
>>> from sorting import insertionsort, unsort
>>> arr = unsort(list(range(0, 20)))
>>> print(arr)
[10, 2, 0, 9, 6, 5, 16, 17, 1, 12, 4, 19, 18, 7, 8, 13, 11, 14, 15, 3]
>>> insertionsort(arr)
>>> print(arr)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```
* *Best case:* `O(n)`
* *Average case:* `O(n^2)`
* *Worst case:* `O(n^2)`

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

<details>
<summary><a id="bogo-sort">Bogo Sort</a></summary>

### Bogo Sort
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
>>> print(root)
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
>>> from trees import JSONTree
>>> root = JSONTree('tree.json')
>>> print(root)
└── first
    ├── second
    |   └── sixth
    ├── third
    └── fourth
        └── fifth
```

*Tree can be specified as flattened lists of nodes and edges via JSON:*
```
{
	"nodes": [
		{
			"id": "1",
			"value": "first"
		},
		{
			"id": "2",
			"value": "second"
		},
		{
			"id": "3",
			"value": "third"
		},
		{
			"id": "4",
			"value": "fourth"
		},
		{
			"id": "5",
			"value": "fifth"
		},
		{
			"id": "6",
			"value": "sixth"
		}
	],
	"edges": [
		{
			"parent": "",
			"child": "1"
		},
		{
			"parent": "1",
			"child": "2"
		},
		{
			"parent": "1",
			"child": "3"
		},
		{
			"parent": "1",
			"child": "4"
		},
		{
			"parent": "4",
			"child": "5"
		},
		{
			"parent": "2",
			"child": "6"
		}
	]
}
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
>>> print(root)
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
>>> print(root)
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
A tree structure that _bubbles up_ common values and prunes congruent subtrees. Used for storing key value pairs, where keys are Linux paths and values are any data structure that is comparable. Implemented via the `BubbleTreeNode` class in `trees.py`.

*Build a Bubble Tree:*
```
>>> from trees import BubbleTreeNode
>>> bt = BubbleTreeNode('root')
```

*Insert nodes into the tree via absolute Linux paths:*
```
>>> bt.insert('/root/dir0/dir00/file000.txt', value=10)
>>> bt.insert('/root/dir0/file00.txt', value=10)
>>> bt.insert('/root/dir1/file10.txt', value=5)
>>> bt.insert('/root/dir2/file20.txt', value=10)
>>> bt.insert('/root/dir2/file21.txt', value=15)
>>> bt.insert('/root/dir3/dir30/file300.txt', value=15)
>>> bt.insert('/root/dir3/file30.txt', value=10)
```

*Bubble up common values to prune the tree:*
```
>>> print(bt)
└── root
    ├── dir0
    |   ├── dir00
    |   |   └── file000.txt (10)
    |   └── file00.txt (10)
    ├── dir1
    |   └── file10.txt (5)
    ├── dir2
    |   ├── file20.txt (10)
    |   └── file21.txt (15)
    └── dir3
        ├── dir30
        |   └── file300.txt (15)
        └── file30.txt (10)
>>> bt.bubble()
>>> print(bt)
└── root
    ├── dir0 (10)
    ├── dir1 (5)
    ├── dir2
    |   ├── file20.txt (10)
    |   └── file21.txt (15)
    └── dir3
        ├── dir30 (15)
        └── file30.txt (10)
```

*Flatten the tree into a dictionary of key-value pairs:*
```
>>> bt.flatten()
{
  '/root/dir0': 10,
  '/root/dir1': 5,
  '/root/dir2/file20.txt': 10,
  '/root/dir2/file21.txt': 15,
  '/root/dir3/dir30': 15,
  '/root/dir3/file30.txt': 10
}
```

</details>

<details>
<summary><a id="trie">Trie</a></summary>
  

### Trie
A basic Trie data structure. Implemented via the `Trie` and `TrieNode` classes in `trees.py`.

*Build a standard trie:*
```
>>> from trees import Trie
>>> root = Trie('to', 5)
>>> root.insert('tea', 3)
>>> root.insert('A', 15)
>>> root.insert('inn', 9)
>>> root.insert('ted', 4)
>>> root.insert('to', 7)
>>> root.insert('i', 11)
>>> root.insert('in', 5)
>>> root.insert('ten', 12)
>>> print(root)
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
A basic linked list data structure. Implemented via the `LinkedList` and `LinkedListNode` classes in `linkedlists.py`.

*Create a linked list:*
```
>>> from linkedlists import LinkedList
>>> l = LinkedList('start')
>>> print(l)
'start' --> 
>>> l.length
1
>>> l.is_empty
False
```

*Get the value at a specific position:*
```
>>> print(l)
'start' -->
>>> l.get_value(0)
'start'
```

*Iterate over the list:*
```
>>> print(l)
'a' --> 'b' --> 'c'
>>> for item in l:
...     print(item)
...
a
b
c
```

*Add to the list with `append`, `prepend`, `insert`, and `replace`:*
```
>>> print(l)
'start' --> 
>>> l.append('new value')
>>> print(l)
'start' --> 'new value' --> 
>>> l.prepend('new start')
>>> print(l)
'new start' --> 'start' --> 'new value' -->
>>> l.insert(2, 'inserted value')
>>> print(l)
'new start' --> 'start' --> 'inserted value' --> 'new value' -->
>>> l.replace('start', 'new start')
>>> print(l)
'new start' --> 'new start' --> 'inserted value' --> 'new value' -->
>>> l.replace('new start', 'test', count=2)
>>> print(l)
'test' --> 'test' --> 'inserted value' --> 'new value' -->
```

*Remove from the list with `delete`, `pop`, and `remove`:*
```
>>> print(l)
'first' --> 'second' --> 'second' --> 'fourth' --> 'second' --> 'fifth'
>>> l.delete(3)
'fourth'
>>> print(l)
'first' --> 'second' --> 'second' --> 'second' --> 'fifth'
>>> l.remove('second')
'second'
>>> print(l)
'first' --> 'second' --> 'second' --> 'fifth'
>>> l.remove('second', count=2)
'second'
>>> print(l)
'first' --> 'fifth'
>>> l.pop()
'fifth'
>>> print(l)
'first' --> 
```

*Reverse the list in place:*
```
>>> print(l)
1 --> 2 --> 3 -->
>>> l.reverse()
>>> print(l)
3 --> 2 --> 1 --> 
```

*Count the number of times a value occurs in the list:*
```
>>> print(l)
'a' --> 'a' --> 'b' --> 'a' --> 'c' --> 
>>> l.count('a')
3
>>> l.count('d')
0
```

*Perform set-like operations, like `intersection`, `union`, `difference_merge`, `zip`, `split`, and `remove_duplicates`:*
```
>>> l1 = LinkedList([1, 2, 3, 4, 5, 6])
>>> l2 = LinkedList([3, 4, 5, 6, 7, 8])
>>> l3 = l1 + l2
>>> print(l3)
1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 -->
>>> l3.remove_duplicates()
print(l3)
1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 -->
>>> l3.intersection(l1)
>>> print(l3)
1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 
>>> l3.union(l2)
>>> print(l3)
1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 -->
>>> l3.difference_merge(l1)
>>> print(l3)
7 --> 8 -->
>>> l1.zip(l2)
>>> print(l1)
1 --> 3 --> 2 --> 4 --> 3 --> 5 --> 4 --> 6 --> 5 --> 7 --> 6 --> 8 -->
>>> l4 = l1.split()
3 --> 4 --> 5 --> 6 --> 7 --> 8 -->
>>> print(l1)
1 --> 2 --> 3 --> 4 --> 5 --> 6 -->
```

*Detect loops:*
```
>>> l1 = LinkedList([1, 2, 3, 4, 5])
>>> l1.contains_loop()
False
>>> l1.head.next.next.next.next = l1.head
>>> l1.contains_loop()
True
```

*Sort the list:*

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
A basic stack data structure. Implemented via the `Stack` class in `stack.py` and `LinkedListNode` class in `linkedlists.py`.

*Build a new stack:*
```
>>> from stack import Stack
>>> s = Stack(1)
>>> print(s)
top --> 1
>>> stack.height
1
>>> stack.is_empty
False
```

*Push to the stack:*
```
>>> print(s)
top --> 1
>>> s.push(2)
>>> s.push(3)
>>> print(s)
top --> 3
        2
	1
```

*Pop off the stack, or peek at the top:*
```
>>> print(s)
top --> 4
        3
        2
	1
>>> s.peek()
4
>>> s.pop()
4
>>> s.pop()
3
>>> print(s)
top --> 2
        1
```

*Add stacks together:*
```
>>> print(s)
top --> 3
        2
	1
>>> s += Stack([4, 5, 6])
>>> print(s)
top --> 6
        5
        4
        3
        2
	1
```

*Iterate over the stack:*
```
>>> print(s)
top --> 3
        2
	1
>>> for value in s:
...	print(s)
...
3
2
1
```

</details>

<details>
<summary><a id="queue">Queue</a></summary>

### Queue
To be implemented.

</details>

<details>
<summary><a id="towers-of-hanoi">Towers of Hanoi</a></summary>

### [Towers of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)
A simple game that utilizes stacks. The goal of the game is to move all of the disks from tower A to tower C, where no disk can be placed on a smaller disk and only one disk can be moved at a time. Implemented via the `TowersOfHanoi` class in `stack.py`.

*Build a Towers of Hanoi instance*
```
# default number of disks is 3, starting on tower A
>>> towers = TowersOfHanoi()
```

*Print the towers*
```
>>> print(towers)
    |         |         |    
 Disk 1       |         |    
 Disk 2       |         |    
 Disk 3       |         |    
========= ========= =========
    A         B         C    
```

*Move disks*
```
>>> towers.move('tower_a', 'tower_b')
>>> print(towers)
    |         |         |    
 Disk 2       |         |    
 Disk 3    Disk 1       |    
========= ========= =========
    A         B         C  
```

*Solve the puzzle completely*
```
>>> print(towers)
    |         |         |    
 Disk 1       |         |    
 Disk 2       |         |    
 Disk 3       |         |    
========= ========= =========
    A         B         C    

>>> moves = towers.solve(show_steps=True)
Moving disk from A to C
Moving disk from A to B
Moving disk from C to B
Moving disk from A to C
Moving disk from B to A
Moving disk from B to C
Moving disk from A to C
>>> moves
7
>>> print(towers)
    |         |         |    
    |         |      Disk 1  
    |         |      Disk 2  
    |         |      Disk 3  
========= ========= =========
    A         B         C    
```

*Supports up to 999 disks, if you have the memory for it!*
```
>>> towers = TowersOfHanoi(disks=999, starting_tower='a')
>>> towers.solve(show_towers=True)
```

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
