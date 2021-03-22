from hashlib import sha256

class Merkle:
    def __init__(self, transactions):
        # e.g transactions = ['a', 'b', 'c', 'd']
        self.transactions = transactions
        self.tree = []

    def generate_merkle_root(self):
        for tx in self.transactions:
            print(sha256(tx.encode('utf-8')).hexdigest())
            
        """ 
        [h(h(h(12)),h(34)), h(h(h(5)))]
        [h(h(12)),h(34),h(h(5))]
        [h(1),h(2),h(3),h(4),h(5)]
        [1,2,3,4,5] 
        """

    def hashPair(self, first, second):
        concat = first + second
        return someFunction(concat)

