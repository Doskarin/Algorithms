'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3
 

Constraints:

0 <= capacity <= 10^4
0 <= key <= 10^5
0 <= value <= 10^9
At most 2 * 10^5 calls will be made to get and put.


'''
#Class node to create
#DLL node with freq initialized
#at 1
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.freq = 1

#DLL node to help us
#create LRU cache at each freq level

class DLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def append(self, node):
        #As in LRU cache
        #we append the most recent
        #element to the head
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        
        self._size += 1
        
    def pop(self, node = None):
        if self._size == 0:
            return
        
        #If there is no specific node
        #to delete - we pop from tail
        if not node:
            node = self.tail.prev
            
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        
        return node

class LFUcache:
    
    #LFU cache initialized with 'capacity'
    #and newly created hashmap where
    #key is a frequency and value is DLL
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._node = { }
        self._freq = defaultdict(DLinkedList)
        
        #IMPORTANT : keep track of minimum freq value
        self._minfreq = 0
        
    def _update(self, node):
        #While updating we first
        #need to get node's frequency
        #then pop it from corresponding
        #frequency DLL
        freq = node.freq
        self._freq[freq].pop(node)
        #if there is nothing left at our current min freq
        #level we increase minfreq by 1
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        #Since node's frequency increased
        #we need to update its value
        node.freq += 1
        freq = node.freq
        #Append node to the corresponding freq in
        #the hashmap
        self._freq[freq].append(node)
        

    def get(self, key: int) -> int:
        if key not in self._node:
            return -1
        
        node = self._node[key]
        #Update node once used
        self._update(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return
        
        #If key is already in the _node
        #hashmap, just update the node
        #and update node's value
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.value = value
        else:
            #if LFU size is already full
            #pop node from its current freq
            #delete it from _node hashmap
            #and decrease size by 1
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
                
            #Create new node
            #Assign this node to the key
            #in the _node hashmap
            #Append this node to freq 1
            #since it's been used only once
            #update min freq to 1
            #and increase size by 1
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1