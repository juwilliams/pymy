"""

commands/map.py

description:
	Generates a blank configuration file in the current directory

"""

from json import dumps
from .base_command import BaseCommand

class Map(BaseCommand):
	def run(self):
		from lib.models import Mapping
		from lib.models import Migration

		migration = Migration.load(self.options['MIGRATION_FILE'])

		mapping = Mapping(self.options)

		migration.mappings.append(mapping)

		migration.write()