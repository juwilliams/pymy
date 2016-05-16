"""

commands/migrate.py

description:
	Processes an input migration file and produces an output file

"""

import pymysql.cursors
import pymysql.converters

from json import dumps
from .base_command import BaseCommand

class Migrate(BaseCommand):
	def run(self):
		from lib.models import Migration
		from lib.models import GlobalConfig
		
		export = ()
		row_delimiter = '\r\n'
		col_delimiter = ', '

		# load the global config
		config = GlobalConfig.load()

		# deserialize migration file
		migration = Migration.load(self.options['MIGRATION_FILE'])

		# connect to mysql
		connection = pymysql.connect(host='localhost',
    		                     	user=config.mysql_username,
    		             			password=config.mysql_password,
                    		     	db=config.db,
                             		charset='utf8mb4',
                             		cursorclass=pymysql.cursors.DictCursor)

		try :
			# retrieve table rows
			with connection.cursor() as cursor:
				cols = self.getCols(migration)
								
				insert_sql = 'INSERT INTO {0} ({1}) VALUES ({2});'

				cursor.execute(migration.query)

				# iterate over rows and create insert statements
				result = cursor.fetchone()			
				while result is not None:
					vals = ()

					for mapping in migration.mappings:
						raw_val = result[mapping.field_from]
						if raw_val is None and mapping.default != '':
							raw_val = mapping.default

						encoded_val = pymysql.converters.escape_item(raw_val, 'utf-8').encode('ascii', 'xmlcharrefreplace')
						
						vals = vals + (encoded_val,)
						
					result = cursor.fetchone()

					export = export + (insert_sql.format(migration.table, col_delimiter.join(cols), col_delimiter.join(vals)),)
				# save json file and optionally produce a sql file for the output data
		finally:
			connection.close()
			migration.export = row_delimiter.join(export)
			migration.write()

	def getCols(self, migration):
		cols = ()

		for mapping in migration.mappings:
			cols = cols + (mapping.field_to,)

		return cols