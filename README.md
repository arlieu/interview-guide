# Interview Guide

This repo is my guide for interview preparation. Feel free to use it as you see fit. It consists of common data structure and algorithm implementations and notes, complexity analyses, and interview questions I have come across. My implementations are done in Python for uniformity and convenience. However, the solutions that I provided to the interview questions are not necessarily done in Python. 

<br />

--------------------------------


## Data Structures

|**[Linked Lists](https://github.com/arlieu/interview-guide/wiki/Data-Structures#linked-lists)**|||
|:---|:---|:---|
|Singly Linked|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/linked_lists/singly_linked.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#singly-linked-list)|
|Doubly Linked|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/linked_lists/doubly_linked.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#doubly-linked-list)|
|**[Stacks](https://github.com/arlieu/interview-guide/wiki/Data-Structures#stacks)**|||
|LIFO|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/stacks/LIFO.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#stacks)|
|**[Queues](https://github.com/arlieu/interview-guide/wiki/Data-Structures#queues)**|||
|FIFO|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/queues/FIFO.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#fifo)|
|Deque|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/queues/deque.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#deque)|
|Priority Queue|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/queues/priority_queue.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#priority-queue)|
|**[Trees](https://github.com/arlieu/interview-guide/wiki/Data-Structures#trees)**|||
|BST|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/trees/bst.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#binary-search-tree-bst)|
|AVL|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/trees/avl.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#adelson-velskii-and-landis-avl-tree)|
|Red-Black|code|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#red-black-tree)|
|**[Hash Tables](https://github.com/arlieu/interview-guide/wiki/Data-Structures#hash-tables)**|||
|Open Addressing|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/hash_tables/open_addressing.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#open-addressing)|
|Separate Chaining|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/hash_tables/separate_chaining.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#separate-chaining)|
|**[Graphs](https://github.com/arlieu/interview-guide/wiki/Data-Structures#graphs)**|||
|Adjacency List|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/graphs/adjacency_list.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#adjacency-list)|
|Adjacency Matrix|[code](https://github.com/arlieu/interview-guide/blob/master/data_structures/graphs/adjacency_matrix.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Data-Structures#adjacency-matrix)|

<br />

-------------------------


## Algorithms

### Sorting 

|**[Bubblesorts](https://github.com/arlieu/interview-guide/wiki/Algorithms#bubblesorts)**|||
|:---|:---|:---|
|Bubblesort|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/sorting/bubble/bubblesort.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#bubblesorts)|
|**[Simple Sorts](https://github.com/arlieu/interview-guide/wiki/Algorithms#simple-sorts)**|||
|Insertion Sort|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/sorting/simple/insertion_sort.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#insertion-sort)|
|Selection Sort|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/sorting/simple/selection_sort.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#selection-sort)|
|**[Efficient Sorts](https://github.com/arlieu/interview-guide/wiki/Algorithms#efficient-sorts)**|||
|Merge Sort|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/sorting/efficient/merge_sort.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#merge-sort)|
|Quicksort|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/sorting/efficient/quicksort.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#quicksort)|
|Heapsort|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/sorting/efficient/heapsort.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#heapsort)|
|**[Distribution Sorts](https://github.com/arlieu/interview-guide/wiki/Algorithms#distribution-sorts)**|||
|Bucket Sort|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/sorting/distributed/bucket_sort.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#bucket-sort)|
|Counting Sort|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/sorting/distributed/counting_sort.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms/#counting-sort)|
|Radix Sort|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/sorting/distributed/radix_sort.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms/#radix-sort)|

### Graphing

|**[Greedy](https://github.com/arlieu/interview-guide/wiki/Algorithms#greedy)**|||
|:---|:---|:---|
|Kruskal's Algorithm|code|notes|
|Prim's Algorithm|code|notes|
|Huffman Coding|code|notes|
|**[Dynamic Programming](https://github.com/arlieu/interview-guide/wiki/Algorithms#dynamic-programming)**|||
|Bellman-Ford Algorithm|code|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#bellman-ford-algorithm)|
|Dijkstra's Algorithm|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/graphing/dynamic_programming/dijkstra.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#dijkstras-algorithm)|
|A* Search Algorithm|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/graphing/dynamic_programming/a_star_search.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#a-search-algorithm)|
|**[Breadth First Search](https://github.com/arlieu/interview-guide/wiki/Algorithms#breadth-first-search)**|||
|Breadth First Search|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/graphing/breadth_first_search/breadth_first_search.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#breadth-first-search)|
|**[Depth First Search](https://github.com/arlieu/interview-guide/wiki/Algorithms#depth-first-search)**|||
|Depth First Search|[code](https://github.com/arlieu/interview-guide/blob/master/algorithms/graphing/depth_first_search/depth_first_search.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Algorithms#depth-first-search)|

<br />

----------------------------------


## Interview Q&A

### Coding

|**Easy**|||
|:---|:---|:---|
|Balanced Delimiters|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/easy/balanced-delimiters.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Interview-Q&A#balanced-delimiters)|
|First Repeating Character|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/easy/first-repeating-character.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Interview-Q&A#first-repeating-character)|
|Add Reversed Linked Lists|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/easy/add-reversed-linked-list.py)|[notes](https://github.com/arlieu/interview-guide/wiki/Interview-Q&A#add-reversed-linked-lists)|
|Rectangle Overlap|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/easy/rectangle-overlap.cpp)|notes|
|Greatest Time|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/easy/greatest-time.py)|notes|
|Prime Numbers|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/easy/prime-numbers.py)|notes|
|Merge Sort|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/easy/merge-sort.py)|notes|
|BST|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/easy/bst.py)|notes|
|**Medium**|||
|NxN Board Game|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/medium/nxn-board-game.py)|notes|
|Longest Palindrome|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/medium/longest-palindrome.cpp)|notes|
|Product Seeds|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/medium/product-seeds.py)|notes|
|Iterative Inorder Traversal|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/medium/iterative-inorder-tree-traversal.py)|notes|
|Minimum Length Subarray|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/medium/minimum-length-unsorted-subarray.py)|notes|
|Linked List Palindrome|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/medium/linked-list-palindrome.py)|notes|
|k Most Frequent Elements|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/medium/k-most-frequent-elements.py)|notes|
|**Hard**|||
|Kth Nearest Point|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/hard/kth-nearest-point.cpp)|notes|
|Shortest Path with Obstacle Avoidance|[code](https://github.com/arlieu/interview-guide/blob/master/interview/coding/hard/shortest-path-obstacle-avoidance.py)|notes|
||code|notes|

### Brain Teasers
|**Easy**||
|:---|:--|
|Sudoku Sub-Grid|[Problem](https://github.com/arlieu/interview-guide/wiki/Interview-Q&A#sudoku-sub-grid)|
|10x10x10 Rubik's Cube|[Problem](https://github.com/arlieu/interview-guide/wiki/Interview-Q&A#10x10x10-rubiks-cube)|
|**Medium**||
|Three Wise Men|[Problem](https://github.com/arlieu/interview-guide/wiki/Interview-Q&A#three-wise-men-riddle)|
|**Hard**||

### Theory/Technology
