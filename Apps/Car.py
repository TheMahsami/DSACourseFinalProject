import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..')))
from DataSets.Array import Array
class Car:
    def __init__(self , car_color , car_name , production_yaer , car_id , plate_number , plated_date , owner_id):
        self.car_color = car_color 
        self.car_name = car_name
        self.production_year = production_yaer
        self.id = car_id
        self.plate_number = plate_number
        self.plated_date = plated_date
        self.owner_id = owner_id
        
        
    def write_to_array():
        pass
    def get_car_owner():
        pass
    