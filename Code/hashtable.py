#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        '''Initialize this hash table with the given initial size.'''
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        '''Return a formatted string representation of this hash table.'''
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        '''Return a string representation of this hash table.'''
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        '''Return the bucket index where the given key would be stored.'''
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
           Running time: O(n^2)
           This is because we require a traversal not only of the list of the
           buckets, but of the list representing the data of the Nodes in each
           bucket (a LinkedList object).

        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
           Running time: O(n^2)
           Same reason as for the keys() method.
           In both of these methods, the best running time is traversing
           through a HashTable where the buckets contain Nodes pointing to
           non-primitive data types (not lists, tuples, dictionaries, etc).
           Otherwise, the running time would become O(n^3).

        """
        # Collect all values in each bucket
        all_values = list()
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
           Running time: O(n^2)
           The method itself only requires traversal of the buckets list, but
           because it invokes the LinkedList.items() method, there is also the
           hidden cost of having to traverse through the Nodes in each bucket.
           Therefore in all cases as the number of buckets, or the number of
           Nodes in each bucket increases, the running time of the method
           increases in quadratic time.

        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
           Running time: O(n^2)
           This method alone uses a constant operation.
           However, the hidden cost is using the self.items() method as a
           helper, which as explained above runs in quadratic time.

        """
        return len(self.items())

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
           Running time: O(n^2)
           The method itself requires a traversal of the buckets, and invokes
           the LinkedList.find() method as a helper n times, where n is the
           number of buckets in the HashTable object.

           In the best case, the LinkedList.find() methods takes only O(1)
           time, when the item we are looking for exists at the head node.
           In this scenario, the HashTable.contains() method would only take
           O(n) time, because now we only depend on traversing through the
           buckets until we find the one whose head node contains the key.

           On average, the HashTable.contains() method will still take O(n^2)
           running time, because in as number of buckets (and the number of
           Nodes in each bucket) increases, then we will most likely have to
           search multiple Nodes in a bucket to find if it contains the key.

           In the worst case, the key does not exist and we need O(n^2) running
           time because we traverse all Nodes in all the buckets of the
           HashTable instance.

        """
        for bucket in self.buckets:
            # Check if key-value entry exists in bucket
            if bucket.find(lambda data: data[0] == key) == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
