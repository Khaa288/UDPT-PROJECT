from pymongo import MongoClient
from flask_marshmallow import Marshmallow

client = MongoClient('localhost', 27017)
db = client.get_database(name = 'RewardServiceDb')

db_reward = db.get_collection('Reward')

ma = Marshmallow()