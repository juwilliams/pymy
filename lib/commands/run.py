"""

commands/run.py

description:
	Generates a blank configuration file in the current directory

"""

import sys
import pymysql.cursors

from json import dumps
from .base_command import BaseCommand

class Run(BaseCommand):
	def run(self):
		from lib.models import Migration
		from lib.models import GlobalConfig

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
				cursor.execute(migration.export)
			
			connection.commit()
		except Exception as e:			
   			print e
		finally:
			connection.close()