
import sys , os , re
sys.path.append(os.path.abspath('.'))
import random
from DataSets.Array import Array
from DataSets.Trie import Trie
from Apps.Plates import LicencePlste
from DataSets.BSTHash import HashTable
from DataSets.HashTable import OpenHashTable
from Modules import read_drivers ,read_users, read_penalties , read_plates , read_ownership_history , read_cars

class User:
    def __init__(self,fname='',lname='',ncode='',password=''):
        self.id = ncode
        self.ncode = ncode
        self.name = fname
        self.lastname = lname
        self.password = password
        self.car_database = read_cars()
        self.users_database = read_users
        self.plates_database = read_plates()
        self.citycode_database = Array(100)
        self.drivers_database = read_drivers()
        self.penalties_database = read_penalties()
        self.owner_ship_history = read_ownership_history()
        
         
    def license_plate_generator(self , cityname , id ):
        cityname = cityname.capitalize()
        city_code = self.citycode_database.search(cityname)
        if city_code is None:
            return 'This City is Unknown Please Choose a Valid City'
        
        allowed_letters = 'ABCEFGHIJKLMNOQRSTUVWXYZ'
        letter = random.choice(allowed_letters)
        
        strnumbers =''
        valid_number_flag = False
        attempted_numbers_counter = 0
        while not valid_number_flag and attempted_numbers_counter <6:

            temp = ''.join(random.choices('0123456789' , k = 5))

            if self._is_valid_plate_nummber(temp , letter):
                strnumbers = temp
                valid_number_flag = True
                attempted_numbers_counter += 1
        
            if not valid_number_flag:
                continue
            # new_plate = f'{city_code}{letter}{strnumbers}
            new_plate = f'{temp[:2]}{letter}{temp[2:5]}-{city_code}'
            plate_object = LicencePlste(new_plate , id)
            self.plates_database.insert(new_plate , plate_object)
            
            
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
    
    def user_login(self, id , password):
        
        if_exist = self.users_database.Search(id)
        if if_exist is None:
            yield 'This User ID Doesnt Exist in System Plz Sign in First!'
            return
    
        # while True:
        #     password = input("password (or type exit for exit): ")
        #     if password.lower() == 'exit':
        #         yield 'Login Was Canceled'
        #         return
            
        hashed_password = self._password_hash_function(password)
        if if_exist[4] == hashed_password:
                yield f'{id} Logged in Successfully'
        
        else:
            yield 'Wrong Password Error...'
    
    def _password_hash_function(self, password):
        salt = 'MystaticSalt0106'
        temp = password + salt
        hashed = 0
        for i , char in enumerate(temp):
            hashed += (i+1) * ord(char)
            
        return hashed #or we can use hex(hashed)
        
    def user_register(self):
        
        name = input("Enter Your First Name:")
        lname = input("Enter Your Last Name: ")
        ncode = input("Enter Your National Code: ")
        day_of_birth = input("Enter Day of Your Birth(e.g. yyyy-mm-dd): ")
        password = input("Enter Your Password: ")
        
        if_user_exixt_flag= self.users_database.Search(ncode)
        if if_user_exixt_flag is not None:
            yield  f'User {ncode} Already Exists'
            return
        
        #ncode cheacker:
        if not ncode.isdigit() or len(ncode) != 10:
            yield "Invalid National Code Format"
            return
        
        #password cheacker:
        if len(password) < 8:
            yield 'Password Most be at least 8 Character'
            return
        if not re.search('[a-zA-Z]', password) or not re.search('[0-9]' , password):
            yield 'Password Most Include both Letters and Numbers'
            return
        
        hashed_password = self._password_hash_function(password)
        
        user_data = (name , lname , ncode, day_of_birth , hashed_password)
        self.users_database.Insert(ncode, user_data)
        yield f'User {ncode} Added Successfully'
    
    def show_user_cars(self , id):
        for item in self.car_database.Traverse():
            key , car = item
            if car.owner_is == id:
                yield str(car)
                
    def show_user_platelicenses(self , id):
        for bst in self.plates_database.table:
            if bst is not None:
                for node in bst.traverse(bst.root):
                    if node.data.owner == id:
                        yield str(node.data.number)
        
#_____phase 3 functionality__________________________________________________
    def show_users_negative_score(self , national_code , driver_id):
        while True:
            driver_data = self.drivers_database.Search(national_code)
            if driver_data.national_id == national_code and driver_data.driver_id == driver_id:
                break
            else:
                raise Exception("Driver ID Not Found!")
        
        sum = 0
        for item in self.penalties_database.traverse():
            if item[1] == driver_id:
                if item[4] == 'Low':
                    sum += 10
                elif item[4] == 'Medium':
                    sum += 30
                elif item[4] == 'High':
                    sum += 50
        yield f'Negative Score For Driver {driver_id}:'
        yield sum
    
    def show_users_penalties_based_driverid(self, driver_id):
        founded_flag = False
        
        yield f'Penalties For Driver {driver_id}:'
        for item in self.penalties_database.traverse():
            #item is a penalty object from App.Penalty
            if item.driver_id == driver_id:
                founded_flag = True
                yield f'Penalty Date: {item.penalty_date} For LicensePlate Number {item.plate_number}.\nLevel: {item.level}\nDescription: {item.description}'
        
        if not founded_flag:
            yield f'Driver {driver_id} Has No Penalties.'
    
    def show_users_penalties_based_platenumber(self , id , plate_number):
        while True:
                
                if not re.fullmatch(r'\d{2}[a-zA-Z]\d{3}-\d{2}' , plate_number):
                            raise ValueError('Wrong Format For LicensePlate Number!!!')
                
                plate_data = self.plates_database.search(plate_number)
                if plate_data is None:
                        raise Exception('LicensePlate Not Found!')

                if plate_data.owner != id:
                        raise Exception("National ID and LicensePlate Number Dosen't Match")
                break
            
        founded_flag = False
        yield f'Penalties For PlateNumber {plate_number}:'
        for item in self.penalties_database.traverse():
            if item.plate_number == plate_number:
                founded_flag = True
                yield f'Penalty Date: {item.penalty_date} For LicensePlate Number: {item.plate_number}.\nLevel: {item.level}\nDescription: {item.description}'
                
        
        if founded_flag == False:
            yield f'LicensePlate Number {plate_number} Has No Penalties.'
        
    def history_of_licenseplate(self , plate_number):
        if not re.fullmatch(r'\d{2}[a-zA-Z]\d{3}-\d{2}' , plate_number):
            raise ValueError('Wrong Format For LicensePlate Number!!!')
            
        yield f"{plate_number}'s History:"
        for item in self.owner_ship_history.traverse():
            if item.plate_number == plate_number:
                car_id = item.car_id
                start = item.start_date
                end = item.end_date
                car_data = self.car_database.Search(car_id)
                yield f'Car Data: \nCar ID: {car_data.id}\nCar Name: {car_data.car_name}\nCar Color{car_data.car_color}\nCar Production Year: {car_data.production_year}\nOwnership Data: \nStart Date: {start}\nEnd Date: {end}'
                    
user = User()
# user.user_login()
# u.insert(number, data)ser._password_hash_function('mahsa')
# print(f' this is password {user._password_hash_function('my123')}')
# print(user.show_users_negative_score())
# user.license_plate_generator('tehran' ,'2078610709')
