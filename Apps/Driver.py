import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..')))
from DataSets.Array import Array

class Driver:
    def __init__(self , national_id , driver_id , license_date):
        self.national_id = national_id
        self.driver_id = driver_id 
        self.license_date = license_date