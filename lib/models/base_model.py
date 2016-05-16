"""
	Base Model
"""

import jsonpickle
import os

class BaseModel(object):
	def serialize(self):
		jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)
		self.json = jsonpickle.encode(self)
		return

	def deserialize(self, json):
		self = jsonpickle.decode(json)
		return

	def write(self):
		with open(self.path + '/' + self.type + '.json', 'w') as outfile:
			#	serialize self
			self.serialize()
			#	write output json
			outfile.write(self.json)
		return

	def createDir(self, path):
		#	create directory structure
		if not os.path.exists(path):
			os.makedirs(path)
			print 'Directory created > ' + path
		else:
			print 'Directory already exists ! ' + path
		return

	def removeDir(self, path):
		#	remove directory via shutil
		import shutil

		if confirm('This will remove ' + path + ' and all contents, are you sure?'):
			shutil.rmtree(path, ignore_errors=True)
		else:
			return


	def createFile(self, file_name, file_contents):
		#	create default empty collection of fields for new container
		with open(file_name, 'w') as outfile:
			outfile.write(file_contents)
			print 'File created > ' + file_name
		return 