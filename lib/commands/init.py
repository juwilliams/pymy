"""

commands/init.py

description:
	Generates a blank configuration file in the current directory

"""

from json import dumps
from .base_command import BaseCommand

class Init(BaseCommand):
	def run(self):
		from lib.models import GlobalConfig

		config = GlobalConfig(self.options)

		setup_webeoc = raw_input('Configure MySQL Connection? [yes/no]: ')
		if setup_webeoc == 'yes' or setup_webeoc == 'y':
			config.db = raw_input('MySQL Database: ')
			config.mysql_username = raw_input('MySQL Username: ')
			config.mysql_password = raw_input('MySQL Password: ')
		else:
			config.db = ''
			config.mysql_username = ''
			config.mysql_password = ''

		config.write()