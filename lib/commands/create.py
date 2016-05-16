"""

commands/init.py

description:
	Generates a blank configuration file in the current directory

"""

from json import dumps
from .base_command import BaseCommand

class Create(BaseCommand):
	def run(self):
		from lib.models import Migration

		migration = Migration('.')

		migration.type = raw_input('Migration name: ')

		setup_migration = raw_input('Setup migratio now? [yes/no]: ')
		if setup_migration == 'yes' or setup_webeoc == 'y':
			migration.query = raw_input('Migration Query: ')
			migration.generate_sql = True if raw_input('Generate SQL? [yes/no]: ') == 'yes' else False
		else:
			migration.query = ''
			migration.generate_sql = False

		migration.write()