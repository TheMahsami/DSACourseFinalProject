
import sys , os , re
sys.path.append(os.path.abspath('.'))
import random
from Modules import read_city_codes
from DataSets.Array import Array
from DataSets.Trie import Trie
from Apps.Plates import LicencePlste
from DataSets.BSTHash import HashTable
from DataSets.HashTable import OpenHashTable

class User:
    def __init__(self,fname="",lname="",ncode="",password=''):
        self.id = ncode
        self.ncode = ncode
        self.name = fname
        self.lastname = lname
        self.password = password
        self.car_database = OpenHashTable()
        self.users_database = Trie()
        self.plstes_database = HashTable()
        
    def license_plate_generator(self , cityname , id ):
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
    # is_loged_in_flag = None
    def user_login(self):
        id = input("id or national code: ")
        
        if_exist = self.users_database.Search(id)
        
        if if_exist is None:
            return 'this id not exist in system plz sighn in first!' ,None
        
        while True:
            password = input("password (or exit for exit): ")
            if password.lower == 'exit':
                return 'loging in was canceled'
            
            hashed_password = self._password_hash_function(password)
            if if_exist['password'] == hashed_password:
                return f'{id} loged in successfully'
        
            else:
                return 'wrong passwprd error... plz try again(or exit for exit)'
    
    def _password_hash_function(self, password):
        salt = 'MystaticSalt0106'
        temp = password + salt
        hashed = 0
        for i , char in enumerate(temp):
            hashed += (i+1) * ord(char)
            
        return hashed #or we can use hex(hashed)
        
    def user_register(self):
        
        name = input("Your first name:")
        lname = input("Your last name: ")
        ncode = input("our national coed:")
        day_of_birth = input("Day of your birth(yyy/mm/dd): ")
        password = input("Your password: ")
        
        if_user_exixt_flag= self.users_database.Search(ncode)
        if if_user_exixt_flag is not None:
            return  f'this user {ncode} alreday have an account'
        
        #ncode cheacker:
        if not ncode.isdigit() or len(ncode) != 10:
            return "invalid format for national code. plz try again."
        
        #password cheacker:
        if len(password) < 8:
            return ' password most have 8 character at least'
        if not re.search('[a-zA-Z]', password) or not re.search('[0-9]' , password):
            return False
        hashed_password = self._password_hash_function(password)
        
        user_data = (name , lname , ncode, day_of_birth , hashed_password)
        self.users_database.Insert(ncode, user_data)
        return f'user {ncode} added successfully'
    
    def show_user_cars(self , id):
        for item in self.car_database.Traverse():
            key , car = item
            if car.owner_is == id:
                print(car)
                
    def show_user_platelicenses(self , id):
        for bst in self.plstes_database.table:
            if bst is not None:
                for node in bst.traverse(bst.root):
                    if node.data.owner == id:
                        print(node.data)
user = User()
# user.user_login()
# u.insert(number, data)ser._password_hash_function('mahsa')
