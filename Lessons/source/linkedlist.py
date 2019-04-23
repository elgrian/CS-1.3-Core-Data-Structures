#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # number of nodes
        
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list.
        We need to loop through all n nodes every time."""
        
        # Create an empty list for results
        results = []  # create a new list
        
        # Start at the head node
        node = self.head  # assigns variable reference
        
        
        # Loops til the node is None which is one node past the tail
        while node is not None: 
            # Append the node's data to the results list
            results.append(node.data)  #appends to a list
            node = node.next  # re assigns variable
        
        # results now has the data from all of the nodes
        return results

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        return self.size

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case runtime: O(1) - if index is the first one in list
        Worst case runtime: O(n) - if index is near or at the end of list
        """
        # Check if the index is out of range and raises an error if it is
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node at the given index and return its data

        results = ''

        # go through linked list, with counter decreasing with each iteration
        # when the counter is 0 or not in range, check if there is some data
        # if we find any data, we return the data, else: return nil

        node = self.head
        while index > 0 and node is not None:
            node = node.next
            index -= 1
        results = node.data
        return results

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case runtime: O(1) - If index is close to/at front of the linked list
        Worst case runtime: O(n) - Traverse through most of/entire linked list to get to index
        """
        # Checks if the index is not in the range and if it's not, throws an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert item after it

        if self.is_empty():                         # if the linked list is empty
            self.append(item)                      
        elif not self.is_empty() and index == 0:    # if items DOES exist, and we want to add item to front
            self.prepend(item)                      # add item to the front
        else:
            new_node = Node(item)                   # create new node with a new item
            node = self.head                        # starts at the front of list
            while index > 1 and node is not None:   # goes through list 
                node = node.next                    # goes on to next node 
                index -= 1                          # keeps track of where we are in the index
            new_node.next = node.next               # sets the pointer of the new node so it isn't broken by insert
            node.next = new_node                    # inserts our new node
            if new_node.next == None:               # if node is at the end
                self.tail = new_node                # update our tail
            self.size += 1                          # then update list length 
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case runtime: O(1) - just add item to end of the list, no traversal
        """
        # Create a new_node to hold the given item
        new_node = Node(item)
        # Check if this linkedlist is empty
        if self.is_empty():
            # Assign head to new_node
            self.head = new_node
        else:
            # Otherwise insert new_node after tail
            self.tail.next = new_node
        # Update tail to new_node regardless
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case runtime: O(1) - adds the item to front of the list
        """
        # Creates new_node to hold the item
        new_node = Node(item)
        
        # Check if linkedlist is empty
        if self.is_empty():
            
            # Assigns tail to the new_node
            self.tail = new_node
        else:
            # else put new_node before the head
            new_node.next = self.head
            
        # Changes the head to the new node
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  
        
        # Loop until node is None, which is one node beyond the tail
        while node is not None:  
            
            # Check if this nodes data satisfies the quality function
            if quality(node.data): 
                # Found data satisfies the function, so exits the while loop early
                return node.data 
            
            # Skips to the next node
            node = node.next
        # data does not satisfy quality function, so returns None
        return None  

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case runtime: O(1) - item is close to/at front of the list
        Worst case runtime: O(n) - item is close to/at end of the list, traverse
        linked list to get to item
        """
        # TODO: Find the node containing the given old_item and replace its
        # starts at the beginning of list
        node = self.head 
        # loops through the list
        while node != None:
            # if we find the item that we want to change
            if node.data == old_item:
                 # replaced the found item 
                node.data = new_item 
                return
            else:
                node = node.next       
        raise ValueError('The item was not found: {}'.format(old_item))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case runtime: O(1) - item we want to delete is close to or at the front of list
        Worst case runtime: O(n) - item we want to delete is close to or at the end of list and we need to go through the list to find it
        Worst case running time: ??? under what conditions? [TODO]"""
        # Starts at the head node
        node = self.head
        found = False
        previous = None
        
        
        # Loops until we find the item or the node is None
        while not found and node is not None:
            # Checking to see IF the nodes data matches the item
            if node.data == item:
                # The Data matches the item, Changed found to True
                found = True
            else:
                # Goes to the next node
                previous = node
                node = node.next
        self.size -= 1
        # IF we find the item or we did not and ended up at the tail
        if found:
            # IF we find a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                
                # Changes the previous node and skips over the found node
                previous.next = node.next
                # Unlinks the found node from the next node
                node.next = None
            # IF we find a node at the head
            if node is self.head:
                # Changes the head to the next node
                self.head = node.next
                # Unlinks the found node from mext node
                node.next = None
            # IF we find a node at the tail
            if node is self.tail:
                if previous is not None:
                    previous.next = None
                # Changes the tail to the previous tail
                self.tail = previous
        else:
            # Raisws Error and tells the user that the delete did not pass
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    ll.insert_at_index(0, 'A')
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    ll.insert_at_index(1, 'B')
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))
    print(ll)

    ll.replace('A', 'D')
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))
    print(ll)

if __name__ == '__main__':
    test_linked_list()