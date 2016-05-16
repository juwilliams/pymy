"""

commands/unmap.py

description:
	Generates a blank configuration file in the current directory

"""

from json import dumps
from .base_command import BaseCommand

class Unmap(BaseCommand):
	def run(self):	
		from lib.models import Mapping
		from lib.models import Migration

		migration = Migration.load(self.options['MIGRATION_FILE'])

		migration.mappings = [x for x in migration.mappings if x.field_from != self.options['FIELD_FROM']]

		migration.write()