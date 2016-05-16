"""

commands/init.py

description:
	Generates a blank configuration file in the current directory

"""

from json import dumps
from .base_command import BaseCommand

class Map(BaseCommand):
	def run(self):
		from lib.models import Mapping

		