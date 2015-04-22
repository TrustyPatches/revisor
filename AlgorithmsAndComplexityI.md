# Algorithms and Complexity I #

## Questions ##

### ADTs and Data Structures ###

1. How would you distinguish between and ADT and a data structure?

### Trees, Including Binary Search Trees ### 

1. Given the following tree:

a 
|---b
|   |---d
|   |
|   |---e
|
|---c---f
        |---g
        |
        |---h

Write out and give the results of the following operations:
  a) Print pre-order
  b) Print post-order
  c) Print in-order

2. What is the ordering property of a binary search tree?

3. Give pseudocode for finding an element in a BST.

4. Give pseudocode for inserting an element in a BST.

5. How do we delete a node in a BST that has less than two children?

6. Given a node t with two children, briefly describe how to delete it from a BST.

7. Give a summary of the running times of some basic BST operations.

### Binary Search Trees: Deletion and Branching  ###

1. Give psuedocode for a recursive look-up function in a BST.

2. Give pseudocode for a recursive function in a BST to compute the sum of its values.

3. Give pseudocode for a recursive function in a BST to compute the number of nodes.

4. Give pseudocode for a recursive function in a BST to compute the height of the tree. 

### Binary Search Trees: Balancing and Augmentation ###

1. Why do we have to rebalance 'bad' trees?

2. Name three types of self-balancing BSTs.

3. Describe the property guaranteed by an AVL.

4. Describe the general strategy of an AVL tree.

5. What does it mean to 'augment' a binary search tree and why would we do it?

6. For a tree t, how can you maintain t.size during the following operations:
  a) Insert
  b) Delete
  c) Rotate left, rotate right



### Hash Tables and Hash Maps ###

1. Give three basic operations needed by a map ADT.

2. Give a one sentence description of a Hash table.

3. Give one advantage and one disadvantage of Hash tables.

4. Using a Hash map, describe an implementation of a multiset.


### Hash Tables: Internals ###

1. Using hash buckets, describe the basic internal structure of a hash table implementation.

2. Describe a hash function used to generate a key and give one essential quality. 

3. Is there a problem if more some items end up mapped to the same slot? 

4. What if *all* items share a slot, or almost all?

5. What is a good table size to use in a hash table implementation?

6. Briefly describe how hash functions used for hash tables differ to those used in cryptography?

7. Assume a table of capacity m, containing n randomly chosen items. What distribution of keys should we expect?

8. Describe two different methods for handling collisions.

### Heaps and Priority Queues ###

1. Describe the purpose of a priority queue and give three basic operations it should support.

2. Give an implementation of a priority queue without using heaps.

3. Give three advantages to using a heap-based implementation for priority queues.

4. Give a description of the dual nature of a heap and the 'heap tree' property

5. Describe how the logical heap tree is mapped into an array in memory

6. Describe how the heap primitives 'sift up' and 'sift down' work.

7. Give an overview of the heap operations 'min', 'insert', and 'deleteMin'.

### Heapsort ###

1. Give psuedocode for heapsort.

2. What is the worst-case time-complexity of heapsort?

### Complexity of Sorting  ###

1. How long does it *have* to take to sort n items?

2. What is the lower bound of a comparison sorting algorithm? Give a rough proof.

3. Draw out the decision tree for a three element list. Show the path it takes for ththe list [20, 30, 10]. How does this show us the largest running time? 

4. Given the bounds on comparison sorting algorithms, give three examples which are aymptotically optimal.

5. Give three non-comparison sorting algorithms and examples of their use cases.

6. Give a description and running times for the counting sort algorithm.

7. Is the counting sort a stable sorting algorithm? What does that mean?

8. 

    *     *     *     *     *


## Solutions ##

### Hash Tables and Hash Maps ###

1. 
  - get(key)
  - put(key, value)
  - find(value)

2.

3.

4.


### Hash Tables: Internals ###

1.
2.
3.
4.
5.
6.
7.
8.


### Heaps and Priority Queues ###

