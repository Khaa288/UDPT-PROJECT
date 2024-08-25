from pymongo import MongoClient
from flask_marshmallow import Marshmallow

client = MongoClient('localhost', 27017)
db = client.get_database(name = 'RequestManagementServiceDb')

db_leave = db.get_collection('Leave')
db_leave_request = db.get_collection('LeaveRequest')
db_wfh = db.get_collection('WFH')
db_wfh_request = db.get_collection('WFHRequest')

ma = Marshmallow()