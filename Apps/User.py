import sys , os
sys.path.append(os.path.abspath('.'))
import random
from Modules import read_city_codes
from DataSets.Array import Array
from DataSets.Trie import Trie

class User:
    def __init__(self,fname="",lname="",ncode="",password=''):
        self.id = ncode
        self.ncode = ncode
        self.name = fname
        self.lastname = lname
        self.password = password
        self.cars = None
        self.users_database = Trie()
        
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
            temp = ''.join(random.choice('0123456789' , k = 5))
            if self._is_valid_plate_nummber(temp , letter):
                strnumbers = temp
                valid_number_flag = True
                attempted_numbers_counter += 1
        
            if not valid_number_flag:
                continue
            
            new_plate = f'{city_code}{letter}{strnumbers}'
            
    def _is_valid_plate_nummber(self , number , letter):
        if self._has_repeated_digit(number) == 5:
            return False
        
        #barresi soodi
        strnumber = str(number)
        ascendig_flag = True
        for i in range(len(strnumber) - 1):
            if int(strnumber[i+1]) != int(strnumber[i]) + 1:
                ascendig_flag = False
                break
            
        if ascendig_flag:
            return False
        #barresi nozooli boodan
        descendinf_flag = True
        for i in range(len(strnumber) - 1):
            if int(strnumber[i+1]) != int(strnumber[i]) - 1:
                descendinf_flag = False
                break
        if descendinf_flag:
            return False
        
        if letter == 'X':
            for digit in number:
                if int(digit) % 2 == 0:
                    return False
        
        return True
    
    def _has_repeated_digit(self,number):
        number = str(number)
        count = 0
        for i in range(len(number)):
            for j in range(i+1 , len(number)):
                
                if number[i] == number[j]:
                    count +=1
                    break
        return count

    def User_login(self, id , password):
        