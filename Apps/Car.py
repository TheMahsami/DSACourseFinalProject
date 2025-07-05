import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..')))
from DataSets.Array import Array
class Car:
    def __init__(self , car_color , car_name , production_yaer , car_id , plate_number , owner_id , plated_date ):
        self.car_color = car_color 
        self.car_name = car_name
        self.production_year = production_yaer
        self.id = car_id
        self.plate_number = plate_number
        self.owner_id = owner_id
        self.plated_date = plated_date
        
        
    def write_to_array():
        pass
    def get_car_owner():
        pass
    