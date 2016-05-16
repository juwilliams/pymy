"""

models/field.py

description:
	field mapping for incoming/outgoing data between systems

	from_field > input data
	to_field > output data

"""

import jsonpickle

from .base_model import BaseModel

class Migration(BaseModel):
	def __init__(self, path):
		self.table = ''
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



