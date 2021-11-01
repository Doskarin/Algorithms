'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.

'''
#Doubly Linked List class in order to
#keep track of recently used items
class ListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache:
    #Initialize LRU cache with dictionary
    #as well as dummy head and tail
    def __init__(self, capacity: int):
        self.LRU = { }
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        
        

    def get(self, key: int) -> int:
        #If key is already in our cache
        #we remove the node from the tail
        #and insert it to the head so that if become the most recently used item
        #then return its value
        if key in self.LRU:
            node = self.LRU[key]
            self.removeFromList(node)
            self.insertToHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #If the key is already in our dictionary
        #we first remove it from the list
        #and insert to the head
        #then update its value
        if key in self.LRU:
            node = self.LRU[key]
            self.removeFromList(node)
            self.insertToHead(node)
            node.value = value
        else:
            #otherwise we check if LRU cache is already full
            #if it is full -> we just remove 'the least' used element from its tail
            if len(self.LRU) >= self.capacity:
                self.removeFromTail()
            #Then we create new node to be inserted
            #put it into the dictionary and insert it to the head
            #since it's the most recent one
            node = ListNode(key, value)
            self.LRU[key] = node
            self.insertToHead(node)
    
    
    #Remove from list method
    #here we reassign pointers of the node to previous
    #and next nodes so that the node remains in void space
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    #Method for inserting the node in front
    #of the dummy head we created in a constructor
    def insertToHead(self, node):
        nextNode = self.head.next
        node.next = nextNode
        node.prev = self.head
        self.head.next = node
        nextNode.prev = node
    #Method to delete the node from its tail   
    def removeFromTail(self):
        if len(self.LRU) == 0:
            return
        tail_node = self.tail.prev
        del self.LRU[tail_node.key]
        self.removeFromList(tail_node)