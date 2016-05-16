"""

models/map.py

description:
	mapping between tables which exist in different database schema

"""

class Mapping(BaseModel):
	def __init__(self):
		self.field_from = ''
		self.field_to = ''
		self.tags = ''