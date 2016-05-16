"""

commands/migrate.py

description:
	Processes an input migration file and produces an output file

"""

from json import dumps
from .base_command import BaseCommand

class Migrate(BaseCommand):
	def run(self):
		from lib.models import Migration
		from lib.models import GlobalConfig

		# deserialize migration file

		# connect to mysql

		# retrieve table rows

		# convert rows to json records

		# save json file and optionally produce a sql file for the output data

		return