"""
usage:
    pymy -h | --help
    pymy migrate -f MIGRATION_FILE -o OUTPUT_FILE
    pymy init
    pymy create
    pymy map MIGRATION_FILE FIELD_FROM FIELD_TO

arguments:
	MIGRATION_FILE       The migration file to process
	FIELD_FROM           Map column from
	FIELD_TO             Map column to

options:
  	-h, --help           Show this screen
  	-f                   Migration file

examples:
  	pymy -m migrate_my_table.json


help:
  	For help using this tool, please open an issue on the Github repository:
  	https://github.com/juwilliams/pymy
"""

from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION

def main():
	"""Main CLI Entrypoint"""
	import commands
	from commands import BaseCommand

	options = docopt(__doc__, version=VERSION)

	# iterate over registered commands and attempt to find one matching the user input
	for k, v in options.iteritems():
		if hasattr(commands, k) and v:
			module = getattr(commands, k)
			commands = getmembers(module, isclass)
			command = [command[1] for command in commands if command[0] != 'BaseCommand'][0]
			command = command(options)
			command.run()
