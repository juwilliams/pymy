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
		from lib.models import BaseModel
		
		rows = ()
		row_delimiter = '\r\n'
		col_delimiter = ','

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

		try:
			# retrieve table rows
			with connection.cursor() as cursor:
				cols = self.getCols(migration)
				cols = (col_delimiter.join(cols),)

				# add header row
				rows = rows + cols
				
				# get search cursor
				cursor.execute(migration.query)

				# iterate over rows and create insert statements
				result = cursor.fetchone()			
				while result is not None:
					vals = ()

					for mapping in migration.mappings:
						try:
							raw_val = result[mapping.field_from]
						except KeyError:
							raw_val = mapping.default if mapping.default is not None else '' 
						finally:
							if raw_val is None and mapping.default != '':
								raw_val = mapping.default

						encoded_val = pymysql.converters.escape_item(raw_val, 'utf-8').encode('ascii', 'xmlcharrefreplace')
						encoded_val = encoded_val.replace('"', '"""')
						encoded_val = encoded_val.replace(',', '","')

						vals = vals + (encoded_val,)
						
					result = cursor.fetchone()

					# add value row
					rows = rows + (col_delimiter.join(vals),)
		finally:
			connection.close()
			
			# write the output to csv
			BaseModel.writeRaw(migration.type + '.csv', row_delimiter.join(rows))

	def getCols(self, migration):
		cols = ()

		for mapping in migration.mappings:
			cols = cols + (mapping.field_to,)

		return cols