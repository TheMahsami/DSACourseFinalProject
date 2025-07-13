import random , re , sys  , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..')))
from datetime import datetime
from DataSets.HashTable import *
from DataSets.Trie import Trie
from Apps.Car import Car
from DataSets.BSTHash import HashTable
from DataSets.Array import Array
from Modules import read_city_codes , read_cars , read_users , read_plates , read_ownership_history , read_drivers , read_penalties

class Admin:
    def __init__(self , username='admin' , password = 'admin'):
        self.username = username
        self.password = password
        self.cars_database = read_cars()
        self.users_database = Trie()
        self.plates_database = read_plates()
        self.citycodes_database = read_city_codes()
        self.ownership_history = read_ownership_history()
        self.drivers_database =read_drivers()
        self.penalties_database = read_penalties()
    
        
    def plate_a_car(self , plate_number , id , car_color , car_name ,production_date):
        
            for item in self.cars_database.table:
                if item is not None and item != 'DELETED':
                    if item[1].plate_number == plate_number:
                        raise Exception('this car already has a license plate!! try with a deactive plate.')

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
                
            
            while True:
                plate = plate_number
                if re.fullmatch(r'\d{2}[a-zA-Z]\d{3}-\d{2}' , plate):
                    break
                else:
                    raise Exception ('Wrong Format For LicensePlate Number Plz try agin with form NNLNNN')
            
            car_id = ''.join(random.choices('0123456789' , k = 5))
            while True:
                plated_date = datetime.today().strftime('%Y-%m-%d')
                try:
                    production_year = int(production_date.split('/')[0])
                    plated_year = int(plated_date.split('/')[0])
                    if plated_year >= production_year:
                        break
                    else:
                        raise Exception('Plated Year Can Not Before Product Year!!')
                    
                except(ValueError):
                    return 'Invalid Date Format. Try yyyy/mm/dd'
                
            car_object = Car.Car(car_color , car_name , production_date , car_id , plate_number , id, plated_date )
            self.cars_database.Insert(car_id , car_object)
            
            plate_obj = self.plates_database.search(plate_number)
            if plate_obj:
                plate_obj.is_active = True
            else:
                raise Exception('LicencrPlate Number Not Found In System')
            yield f'Car {car_id} Added Succesfully'
        
    def show_all_cars(self):
        yield 'All Cars:'
        for data in self.cars_database.Traverse():
            car_data = data[1]
            yield f'Car Id: {car_data.id}\nCar Name: {car_data.car_name}\nCar Color: {car_data.car_color}\nProduction Year: {car_data.production_year}\nCar Owner: {car_data.owner_id}\nCar LicensePlate Number: {car_data.plate_number}'
            
            
    def show_all_users(self):
        yield 'All Users:'
        for data in self.users_database.Traverse():
            user_data = data[1]
            yield f'User Name: {user_data[0]}\nLast Name: {user_data[1]}\nNational ID: {user_data[2]}\nBirth Date: {user_data[3]}\nUser Hashed Password: {user_data[4]}'
            
    # tool       
    def _get_citycode_from_plate_number(self , number):
        citycode = number.split('-')[1]
        return citycode
        
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
        yield f'All LicensePlates in {city_name}:'
        for node in bst.traverse(bst.root):
            if node is not None:
                yield f'LicencePlate Number:{node.data.number} - {node.data.is_active}'
                
    def show_cars_of_a_city(self , city_name):
        city_code = self._get_citycode_from_cityname(city_name)
        yield f'All Cars in {city_name}:'
        for item in self.cars_database.table:
            if item is not None and item != 'DELETED':
                car_data = item[1]
                curr_car_citycode = car_data.plate_number.split('-')[1]
                if int(curr_car_citycode) == int(city_code):
                    yield f'Car ID: {car_data.id}\nCar Name: {car_data.car_name}\nCar Color: {car_data.car_color}\nProduction Year: {car_data.production_year}\nCar licencePlate Number: {car_data.plate_number}\nOwner: {car_data.owner_id}'
    
    def search_cars(self, start , end):    
        while True:
            if start == '':
                start = None
                break
            elif start.isdigit():
                start = int(start)
                break
            else:
                raise Exception('invalid format!')
        while True:
            if end == '':
                end  = None
                break
            elif end.isdigit():
                end = int(end)
                break
            else:
                raise Exception('invalid format!')
        
        any_found_flag = False
        yield f'All Cars From {start} to {end}:'
        for item in self.cars_database.table:
            if item is not None and item != 'DELETED':
                car_data = item[1]
                curr_car_product_yaer = int(car_data.production_year)
                
                
                if start is None and end is None:
                    yield f'Car Name: {car_data.car_name}\nProduction Year: {curr_car_product_yaer}\nCar Color: {car_data.car_color}\nLicencePlate Number: {car_data.plate_number}'
                    any_found_flag = True
                    
                elif start is None and curr_car_product_yaer <= end:
                    yield f'Car Name: {car_data.car_name}\nProduction Year: {curr_car_product_yaer}\nCar Color: {car_data.car_color}\nLicencePlate Number: {car_data.plate_number}'
                    any_found_flag = True
                    
                elif end is None and curr_car_product_yaer >= start:
                    yield f'Car Name: {car_data.car_name}\nProduction Year: {curr_car_product_yaer}\nCar Color: {car_data.car_color}\nLicencePlate Number: {car_data.plate_number}'
                    any_found_flag = True
                    
                elif start <= curr_car_product_yaer <= end:
                    yield f'Car Name: {car_data.car_name}\nProduction Year: {curr_car_product_yaer}\nCar Color: {car_data.car_color}\nLicencePlate Number: {car_data.plate_number}'
                    any_found_flag = True
            
            if not any_found_flag:
                yield 'No Car Found'
                return
    
    def show_car_owners_of_a_city(self , city_name):
        city_code = self._get_citycode_from_cityname(city_name)
        
        yield f'All Car Owners in {city_name}'
        for item in self.cars_database.table:
            if item is not None and item != 'DELETED':
                curr_car_citycode = item[1].plate_number.split('-')[1]
                if int(curr_car_citycode) == int(city_code):
                    owner_id = item[1].owner_id
                    owner_data = self.users_database.Search(owner_id)
                    yield f'Owner Name: {owner_data[0]}\nLast Name: {owner_data[1]}\nOwner National Code: {owner_data[2]}\nOwner Birth Date: {owner_data[3]}'
                    
    def update_username(self , id , new_name):
        if self.users_database.Search(id) :
            user_data = self.users_database.Search(id)
            new_user_data = (new_name , user_data[1], user_data[2] , user_data[3], user_data[4])
            self.users_database.Delete(id)
            self.users_database.Insert(id , new_user_data)
            yield f'User {id} Updated Successfully'
        else:
            raise Exception('user not found')
#_____ phase 3 functionality_____________________________________
    def show_ownership_history(self , car_id):
        yield f'Ownership History Of Car {car_id}: '
        for item in self.ownership_history.traverse():
            #items are Apps.History
            if item.car_id == car_id:
                yield f'Owner ID: {item.owner_id}\nStart Date: {item.start_date} End Date: {item.end_date}\nWith LicencePlate Number: {item.plate_number}'
    
    def show_all_drivers(self):
        yield "All Drivers Records:\n"
        for item in self.drivers_database.Traverse():
            driver_data = item[1]
            yield f"Driver NationalCode: {driver_data.national_id}\nDriver ID: {driver_data.driver_id} - Date of DriverLicence: {driver_data.license_date}\n"
            
    def change_plate_owner(self , car_id , plate_number , new_plate_number):
        car = self.cars_database.Search(car_id)
        #car is a car object from Apps.Car
        if car is None:
            print( f'Car {car_id} Not Exist.')
            return
        if not re.fullmatch(r'\d{2}[a-zA-Z]\d{3}-\d{2}' , plate_number):
                    raise Exception ('Wrong Format For LicensePlate Number Plz try agin with form NNLNNN')
        
        if re.fullmatch(r'\d{2}[a-zA-Z]\d{3}-\d{2}' , new_plate_number):
            
            new_plate = self.plates_database.search(new_plate_number)
            #new plate is a liceensePlate object from Apps.Plates
            if new_plate is None:
                yield "Your New LicencePlate Number not Exist. Plz Generate a Number From User Panel/Generate LicensePlate Number."
                return
            
            for item in self.cars_database.Traverse():
                #item[1] is  a car obj from Apps.Car
                if item[1].plate_number == new_plate_number:
                    yield('This LicensePlate Number Belongs to another Car!')
                    return

            car.plate_number = new_plate_number
            yield f"LicensePlate Number of {car_id} Updated to {new_plate_number} Successfully."
            
    # def task(self):
    #     for item in self.users_database.Traverse():
    #         user_id = item[1][2]
    #         user_plate_counter = 0
    #         for bst in self.plates_database.table:
    #             if bst is not None:
    #                 for node in bst.traverse(bst.root):
    #                     if node.data.owner == user_id:
    #                         user_plate_counter += 1
                        
    #         if user_plate_counter >= 3:
    #             yield f'\nUser With ID {user_id}'
                            
    # def task(self,start , end , no_plate):
    #     for item in self.users_database.Traverse():
    #         user_id = item[1][2]
    #         Birthday = item[1][3].split('-')
    #         birthyear = Birthday[0]
    #         this_year = datetime.today().strftime('%Y')
    #         user_age = int(this_year) - int(birthyear)
            
    #         if int(start) <= user_age <= int(end):
    #             counter = 0
    #             for bst in self.plates_database.table:
    #                 if bst is not None:
    #                     for node in bst.traverse(bst.root):
    #                         if node.data.owner == user_id:
    #                             counter += 1
                # if counter == int(no_plate):
                #     yield f"\nWe have User {user_id} with Age {user_age} and {counter} LicensePlate Numbers."
            
    def task(self, first_id , sec_id):
        first_date = Array(100)
        sec_date = Array(100)
        for item in self.cars_database.table:
            if item is not None and item != "DELETED":
                data = item[1]
                if data.owner_id == first_id:
                    first_date.appendlast(data.plated_date)
                    
                elif data.owner_id == sec_id:
                    sec_date.appendlast(data.plated_date)
                    
        # first_date.traverse()
                    
        for i in first_date.traverse():
            for j in sec_date.traverse():
                if i == j:
                    yield f"There is  a match in date {i} with users {first_id} and {sec_id}"
                
            

        
        
                
            
admin = Admin()

# admin.plate_a_car('33d754-11' , '1274437280')
# admin.show_all_cars()
# admin.show_plates_of_a_city('Tehran')
# admin.task()
# for message in admin.change_plate_owner('13638' , '28G206-44' , '59D327-71'):
#     print(message)
# for massage in admin.admin_login('admin' , "admin"):
#     print(massage)