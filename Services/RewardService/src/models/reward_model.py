from dataclasses import dataclass
import math
from src.models.employee_model import Employee
from src.models.gift_model import Gift
from src.models.brand_model import Brand
from src.models import db_reward
from src.services.urbox_service import UrboxService 
from flask import jsonify
import uuid

@dataclass
class Reward():
    Employee: Employee # type: ignore
    TotalPoint: int
    Gifts: [] # type: ignore
    
    def __init__(self, employee, totalPoint):
        self.Employee = employee
        self.TotalPoint = totalPoint
        self.Gifts = []

    def send_point(send_point_info):
        sender_id = int(send_point_info["SenderId"])
        receiver_id = int(send_point_info["ReceiverId"])
        point = int(send_point_info["Point"])

        sender = db_reward.find_one({'Employee.EmployeeId': sender_id})
        receiver = db_reward.find_one({'Employee.EmployeeId': receiver_id})

        if (sender['TotalPoint'] - point < 0):
            return False
        
        db_reward.update_one(
            {'Employee.EmployeeId': sender_id}, 
            {'$set': {'TotalPoint': sender['TotalPoint'] - point}}
        )

        db_reward.update_one(
            {'Employee.EmployeeId': receiver_id}, 
            {'$set': {'TotalPoint': receiver['TotalPoint'] + point}}
        )

        return True
    
    def exchange_gift(exchange_gift_info):
        gift_id = int(exchange_gift_info["GiftId"])
        employee_id = int(exchange_gift_info["EmployeeId"])
        brand_id = int(exchange_gift_info["BrandId"])
        
        urbox_gift = UrboxService.get_gift_by_id(gift_id)
        employee_reward = db_reward.find_one({'Employee.EmployeeId': employee_id})

        # empty urbox gift
        if urbox_gift is None:
            return False
        
        # Not enough point
        if (employee_reward["TotalPoint"] - int(urbox_gift["data"]["price"])) < 0:
            print(employee_reward["TotalPoint"] - int(urbox_gift["data"]["price"]))
            return False
        
        brand_title = ''
        # unknow brand
        if urbox_gift["data"]["brand"] is False:
            brand_title = 'Unknown'
        else:
            brand_title = urbox_gift["data"]["brand"]["title"]
        
        # Process gift before adding to db
        my_gift = Gift(
            giftId=gift_id,
            name=urbox_gift["data"]["title"],
            brand= Brand(
                id=brand_id,
                title=brand_title
            )
        )

        my_gift.Detail.append({
            'Id': urbox_gift["data"]["id"],
            'Price': urbox_gift["data"]["price"],
            'PriceFormat': urbox_gift["data"]["price_format"],
        })

        # Exchange reward and update point
        db_reward.update_one(
            {'Employee.EmployeeId': employee_id},
            {'$push': {'Gifts': jsonify(my_gift).json} }
        )
        db_reward.update_one(
            {'Employee.EmployeeId': employee_id},
            {'$set': {'TotalPoint': employee_reward["TotalPoint"] - int(urbox_gift["data"]["price"]) }}
        )

        return True
    
    def list_employees():
        return db_reward.find({}, {'Employee':True, '_id':0})

    def get_reward_employee(employee_id):
        return db_reward.find_one({'Employee.EmployeeId': int(employee_id) })

    def list_employee_gifts(employee_id):
        reward = db_reward.find_one({'Employee.EmployeeId': int(employee_id)})

        if reward is None:
            return []

        return reward["Gifts"]
    
    def add_monthly_points():
        reward = db_reward.find({})
        monthly_points = 500000

        db_reward.update_many(
            # update all
            { },
            { "$inc": { "TotalPoint": monthly_points}  }
        )