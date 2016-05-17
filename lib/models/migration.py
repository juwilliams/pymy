"""

models/migration.py

description:
	contains details necessary to process a migration between databases and/or tables

"""

import jsonpickle

from .base_model import BaseModel

class Migration(BaseModel):
	def __init__(self, path):
		self.table = ''
		self.to_table = ''
		self.mappings = []
		self.type = ''
		self.path = path
		self.export = ''		

	@staticmethod
	def load(file_name):
		return jsonpickle.decode(Migration.openFile(file_name))

	@staticmethod
	def openFile(file_name):
		with open(file_name, 'r') as outfile:
			data = outfile.read()
			return data



