
from db_connection import DBConnection
import os 
import glob
from endpoint import runEndpoint

def bootstrap():
    print("Beginning bootstrap procedure...")
    db = DBConnection()
    print("Established connection to db...")

    db.createSensorTables()
    print("Created database tables")

    # iterate through backup csv folder and add them to database
    for csvFile in glob.glob('/usr/backups/*.csv'):
      db.insertSensorData(csvFile)
    print("Bootstrap procedure complete")

if __name__ == '__main__':
  bootstrap()
  runEndpoint()