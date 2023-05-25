from collections import OrderedDict
import pickle
import os

from interfaces import Cache

class LRUCache(Cache):

	def __init__(self, capacity: int = 2000, file: str = os.path.expanduser('~/.gene_cache')) -> None:
		self.data = OrderedDict()
		self.file = file
		self.capacity = capacity
		self.size = len(self.data)
	
	def get(self, key: str):
		value = -1
		if key in self.data:
			value = self.data[key]
			self.recently_used(key)
		return value
	
	def put(self, key: str, value: str):
		if key in self.data:
			self.data[key] = value
			self.recently_used(key)
		else:
			self.data[key] = value
			self.size += 1
			if self.size > self.capacity:
				self.evict()
				self.size -= 1
	
	def evict(self):
		self.data.popitem(last = False)
	
	def recently_used(self, key: str):
		value = self.data[key]
		del self.data[key]
		self.data[key] = value
	
	def write_to_disk(self):
		fh = open(self.file, 'wb')
		pickle.dump(self.data, fh)
		fh.close()

	def load_from_disk(self):
		fh = open(self.file, 'rb')
		self.data = pickle.load(fh)
		fh.close()
		self.size = len(self.data)