from abc import ABC, abstractmethod
import os

class Client(ABC):

	@property
	@abstractmethod
	def base_url(self):
		pass

	@property
	def output_dir(self):
		return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/output/'

	@abstractmethod
	def run(self):
		pass


class Cache(ABC):

	@abstractmethod
	def put(self, key: str, value: str):
		pass

	@abstractmethod
	def get(self, key: str):
		pass

	@abstractmethod
	def evict(self):
		pass

	@abstractmethod
	def write_to_disk(self):
		pass

	@abstractmethod
	def load_from_disk(self):
		pass