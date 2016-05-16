"""

models/map.py

description:
	mapping between tables which exist in different database schema

"""

from .base_model import BaseModel

class Mapping(BaseModel):
	def __init__(self, options):
		self.field_from = options['FIELD_FROM']
		self.field_to = options['FIELD_TO']
		self.default = options['DEFAULT_VALUE']
		self.tags = ''