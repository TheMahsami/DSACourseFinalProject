import random , re , sys  , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..')))
from datetime import datetime
from DataSets.HashTable import *
from DataSets.Trie import Trie
import Car
from DataSets.BSTHash import HashTable
from DataSets.Array import Array
from Modules import read_city_codes , read_cars , read_users

class Admin:
    def __init__(self):
        self.usename = 'admin'
        self.password = 'admin'
        self.cars_database = read_cars()
        self.users_database = read_users()
        self.plates_database = HashTable()
        self.citycodes_database = read_city_codes()
        
    def plate_a_car(self , plate_number , id):
        
            for item in self.cars_database.table:
                if item is not None and item != 'DELETED':
                    if item[1].plate_number == plate_number:
                        raise Exception('this car already has a license plate!! try with a deactive plate.')

            car_color = input('inter your car color: ')
            if car_color.lower() == 'white':
                car_color = 'WT'
            elif car_color.lower() == 'black':
                car_color = 'BC'
            elif car_color.lower() == 'red':
                car_color = 'RD'
            elif car_color.lower() == 'blue':
                car_color = 'BL'
            elif car_color.lower() == 'silver':
                car_color = ' GR'
                
            else:
                car_color = 'OT'
                
            car_name = input('inter your car name: ')
            while True:
                plate = plate_number
                if re.fullmatch(r'\d{2}[a-zA-Z]\d{3}-\d{2}' , plate):
                    break
                else:
                    raise Exception (' wrong format for plate number plz try agin in form NNLNNN')
            
            car_id = ''.join(random.choices('0123456789' , k = 5))
            while True:
                production_date = input("inter the prodoction year of your car: ")
                plated_date = datetime.today().strftime('%Y-%m-%d')
                try:
                    production_year = int(production_date.split('/')[0])
                    plated_year = int(plated_date.split('/')[0])
                    if plated_year >= production_year:
                        break
                    else:
                        return ' plated year can not before product year'
                except(ValueError):
                    return 'invalid date format. try yyy/mm/dd'
            car_object = Car.Car(car_color , car_name , production_date , car_id , plate_number , id, plated_date )
            self.cars_database.Insert(car_id , car_object)
            self.plates_database.search(plate_number).is_active = True
            return 'car added succesfully'
        
    def show_all_cars(self):
        for data in self.cars_database.Traverse():
            print(data)
            
    def show_all_users(self):
        for data in self.users_database.Traverse():
            print(data)
    # tool       
    def _get_citycode_from_plate_number(self , number):
        citycode = number.split('-')[1]
        
    def _get_citycode_from_cityname(self , cityname):
        city_code = None
        try:
            for i in range(len(self.citycodes_database.MainArray)):
                if self.citycodes_database.MainArray[i] is not None:
                    if self.citycodes_database.MainArray[i] == cityname.capitalize():
                        city_code = i
            return city_code
        except:
            raise Exception('city not founded')
        
    def show_plates_of_a_city(self , city_name):
        city_code = self._get_citycode_from_cityname(city_name)
        
        index = self.plates_database._hash_function(city_code)
        bst = self.plates_database.table[index]
        for node in bst.traverse(bst.root):
            if node is not None:
                print(node.data)
                
    def show_cars_of_a_city(self , city_name):
        city_code = self._get_citycode_from_cityname(city_name)
        for item in self.cars_database.table:
            if item is not None and item != 'DELETED':
                car_data = item[1]
                curr_car_citycode = car_data.plate_number.split('-')[1]
                if int(curr_car_citycode) == int(city_code):
                    print(f'{car_data.car_color} {car_data.car_name} {car_data.production_year} {car_data.plate_number} {car_data.id} {car_data.owner_id}')
    
    def search_cars(self):    
        while True:
            start = input('inter the starting point of your time period: ')
            if start == '':
                start = None
                break
            elif start.isdigit():
                start = int(start)
                break
            else:
                raise Exception('invalid format!')
        while True:
            end = input('inter the ending point of your time period: ')
            if end == '':
                end  = None
                break
            elif end.isdigit():
                end = int(end)
                break
            else:
                raise Exception('invalid format!')
        
        any_found_flag = False
        for item in self.cars_database.table:
            if item is not None and item != 'DELETED':
                car_data = item[1]
                curr_car_product_yaer = int(car_data.production_year)
                
                
                if start is None and end is None:
                    print(f' {car_data.car_name} {curr_car_product_yaer} {car_data.car_color} {car_data.plate_number}')
                    any_found_flag = True
                    
                elif start is None and curr_car_product_yaer <= end:
                    print(f' {car_data.car_name} {curr_car_product_yaer} {car_data.car_color} {car_data.plate_number}')
                    any_found_flag = True
                    
                elif end is None and curr_car_product_yaer >= start:
                    print(f' {car_data.car_name} {curr_car_product_yaer} {car_data.car_color} {car_data.plate_number}')
                    any_found_flag = True
                    
                elif start <= curr_car_product_yaer <= end:
                    print(f' {car_data.car_name} {curr_car_product_yaer} {car_data.car_color} {car_data.plate_number}')
                    any_found_flag = True
            
            if not any_found_flag:
                return None
    
    def show_car_owners_of_a_city(self , city_name):
        city_code = self._get_citycode_from_cityname(city_name)
        
        for item in self.cars_database.table:
            if item is not None and item != 'DELETED':
                curr_car_citycode = item[1].plate_number.split('-')[1]
                if int(curr_car_citycode) == int(city_code):
                    owner_id = item[1].owner_id
                    owner_data = self.users_database.Search(owner_id)
                    print(owner_data)
                    
    def update_username(self , id):
        if self.users_database.Search(id) :
            user_data = self.users_database.Search(id)
            new_name = input('inter users new name: ')
            new_user_data = (new_name , user_data[1], user_data[2] , user_data[3], user_data[4])
            self.users_database.Delete(id)
            self.users_database.Insert(id , new_user_data)
            return f'user {id} updated successfully'
        else:
            raise Exception('user not found')
admin = Admin()

# admin.plate_a_car('33d754-11' , '1274437280')
# admin.show_all_cars()
# admin.show_plates_of_a_city('Tehran')
admin.plate_a_car('21A763-71' , '1274437180')