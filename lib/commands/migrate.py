"""

commands/migrate.py

description:
	Processes an input migration file and produces an output file

"""

import csv
import pymysql.cursors
import pymysql.converters

from json import dumps
from .base_command import BaseCommand

class Migrate(BaseCommand):
	def run(self):
		from lib.models import Migration
		from lib.models import GlobalConfig
		from lib.models import BaseModel
		
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
			with open(migration.type + '.csv', 'wb') as csvfile:
				csv_writer = csv.writer(csvfile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)

				# retrieve table rows
				with connection.cursor() as cursor:
					csv_writer.writerow(self.getCols(migration))
					
					# get search cursor
					cursor.execute(migration.query)

					# iterate over rows and create insert statements
					result = cursor.fetchone()

					while result is not None:
						vals = []

						for mapping in migration.mappings:
							
							try:
								raw_val = result[mapping.field_from]
							except KeyError:
								raw_val = mapping.default if mapping.default is not None else '' 
							finally:
								if raw_val is None and mapping.default != '':
									raw_val = mapping.default

							encoded_val = pymysql.converters.escape_item(raw_val, 'utf-8').encode('ascii', 'xmlcharrefreplace')
							encoded_val = encoded_val.replace('\\"', '"')
							encoded_val = encoded_val[1:-1]

							vals.append(encoded_val)
							
						result = cursor.fetchone()

						# add value row
						csv_writer.writerow(vals)
		except Exception as e:
			print e.message
		finally:
			connection.close()			

	def getCols(self, migration):
		cols = []

		for mapping in migration.mappings:
			cols.append(mapping.field_to)

		return cols