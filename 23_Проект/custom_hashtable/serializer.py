from .chain_hashtable import ChainHashTable
from .cuckoo_hashtable import CuckooHashTable
import pickle


class HashTableSerializer:

    @staticmethod
    def serialize(hashtable: ChainHashTable | CuckooHashTable, filename: str = 'hashtable.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(hashtable, f)

    @staticmethod
    def deserialize(filename: str = 'hashtable.pkl') -> ChainHashTable | CuckooHashTable:
        with open(filename, 'rb') as f:
            return pickle.load(f)
