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

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
           Running time: O(n) because we have to go through and count all the
           nodes in the list, until we reach the last node
        """
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def start_with_first_node(self, new_node):
        """Add the first node to the LinkedList.
           Param: new_node(Node): the node to be added
        """
        self.head = self.tail = new_node
        self.head.next = self.tail.next = None

    def append(self, item):
        """Insert the given item at the tail of this linked list.
           Running time: O(1) because either we have to make a new node to
           begin the list, or we go straight to the tail and add a new node.
           No matter the case, we know exactly where in the list we have to go.
        """
        new_node = Node(item)
        if self.is_empty() is True:
            self.start_with_first_node(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
           Running time: O(1) because we always have to locate the head
           or we initialize it, which is one operation because head is always
           at the start of the list.
        """
        new_head = Node(item)
        if self.is_empty() is not True:
            old_head = self.head
            self.head = new_head
            self.head.next = old_head
        else:
            self.start_with_first_node(new_head)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
           Best case running time: O(1) because if we find the node that
           satisfies the quality at self.head, then we exit after just
           one iteration.
           Worst case running time: O(n) because if no node matches with the
           given quality, then we will have to check every node in the list
           before completing this method.
        """
        node = self.head
        while node is not None:
            # this node matches
            if quality(node.data) is True:
                return node.data
            # this node does not match, move on to the next
            else:
                node = node.next
        # no matches in the list
        else:
            return None
        '''
        list = [Node(item) for item in self.items()]
        if list is not None:
            for item in list:
                if item.data == quality:
                    return item
                elif quality(item.data) is True:
                    return item
            else:  # the item is not in the list
                return None
        else:  # the list has no items
            return None
        '''

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
           TODO: Best case running time: O(???) Why and under what conditions?
           TODO: Worst case running time: O(???) Why and under what conditions?
        """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        node = self.head
        node_before = None
        # discover if the data we are looking for exists in the list
        is_inside = self.find(lambda data: data == item) == item
        # item does not exist
        if is_inside is False:
            raise ValueError(f'Item not found: {item}')
        # item does exist in the list
        else:
            # find the node with the data to delete
            while not node.data == item:
                node_before = node
                node = node.next
            # only one node left in the list
            if self.head.next is None:
                self.head = self.tail = None
            # item to delete is the head of the list
            elif (self.head.data == node.data and
                  self.head.next == node.next):
                self.head = self.head.next
            # the node being deleted is the tail
            elif (self.tail.data == node.data and
                  self.tail.next == node.next):
                node_before.next = None
                self.tail = node_before
            # shift the nodes left so they no longer include the deleted node
            else:
                node_before.next = node.next

        '''
        node = self.head
        node_before = None
        # discover if the data we are looking for exists in the list
        data_to_match = self.find(lambda data: data == item)
        if data_to_match is not None:  # avoiding AttributeError
            data_to_match = data_to_match
        # item does not exist
        if data_to_match is None:
            raise ValueError(f'Item not found: {item}.')
        # item does exist in the list
        else:
            # find the node with the data to delete
            while not node.data == data_to_match:
                node_before = node
                node = node.next
            # only one node left in the list
            if self.head.next is None:
                self.head = self.tail = None
            # item to delete is the head of the list
            elif self.head.data == data_to_match:
                self.head = self.head.next
            # the node being deleted is the tail
            elif self.tail.data == data_to_match:
                node_before.next = None
                self.tail = node_before
            # shift the nodes left so they no longer include the deleted node
            elif node_before is not None:
                node_before.next = node.next
        '''
        '''
        previous_nodes = list()
        node = self.head
        i = 0
        while node is not None:
            # if the node matches, and choosing the scenario it matches with
            if item == node.data:
                # there is only one node in the list
                if node == self.head and node == self.tail:
                    node = None
                # the node is the head only
                elif node.data == self.head.data:
                    self.head = node.next
                else:
                    node_before = previous_nodes[i - 1]
                    # the node is the tail only
                    if node.data == self.tail.data:
                        self.tail = node_before
                        self.tail.next = None
                    # the node is neither the head or tail (it's in between)
                    else:
                        node_after = node.next
                        node_before.next = node_after
            # if the node doesn't match, move on to the next
            else:
                previous_nodes.append(node)
                i += 1
                node = node.next
        # if the item could not be found in the entire list
        else:
            raise ValueError(f'Item not found: {item}.')
        '''
        '''
        try:
            # create a list of Node objects all stored in a list
            nodes = [Node(item) for item in self.items()]
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            # look for the node matching the item
            for i in range(len(nodes)):
                node = nodes[i]
                # check if this is the node, and if it is the tail
                if node.data == item:
                    if node == self.tail:
                        # move the tail back one
                        node_before = nodes[i - 1]
                        self.tail = node_before
                        node_before.next = None
                    # remove both head and tail because there is only one node
                    elif len(nodes) == 1:
                        self.head = self.tail = None
                    # if the matching node is the head
                    elif node == self.head:
                        node_after = nodes[i + 1]
                        self.head = node_after
                    # if the matching node is between head and tail
                    else:
                        node_after = nodes[i + 1]
                        node_before = nodes[i - 1]
                        node_before.next = node_after
        except ValueError:
            raise ValueError(f'Item not found: {item}.')
            '''


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
