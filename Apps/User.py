import random
from Modules import read_city_codes
from DataSets.Array import Array

class User:
    def __init__(self,fname,lname,ncode,password):
        self.id = ncode
        self.ncode = ncode
        self.name = fname
        self.lastname = lname
        self.password = password
        self.cars = None
        
    def license_plate_generator(self , cityname ):
        all_city_codes = read_city_codes()
        city_code = all_city_codes.search(cityname)
        if not city_code:
            return 'this city is unknown please chiise a valid city'
        
        allowed_letters = 'ABCEFGHIJKLMNOQRSTUVWXYZ'
        letter = random.choice(allowed_letters)
        
        strnumbers =''
        valid_number_flag = False
        attempted_numbers_counter = 0
        while not valid_number_flag and attempted_numbers_counter <6:
            temp = ''.join(random.choic('0123456789' , k = 5))
            if self._is_valid_plate_nummber(temp , letter):
                strnumbers = temp
                valid_number_flag = True
                attempted_numbers_counter += 1
        
            if not valid_number_flag:
                continue
            
            new_plate = f'{city_code}{letter}{strnumbers}'
            
    def _is_valid_plate_nummber(self):
        pass