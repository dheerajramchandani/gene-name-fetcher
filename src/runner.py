import os
import sys
import pandas as pd

from client import UniprotClient
from cache import LRUCache


if __name__ == "__main__":
	cache = LRUCache(capacity=10000)
	client = UniprotClient(cache)
	if os.path.exists(cache.file):
		cache.load_from_disk()

	try:
		client.run(sys.argv[1])
	except IndexError:
		print("Please provide the input file.")
	except ConnectionError:
		cache.write_to_disk()	
	
	cache.write_to_disk()