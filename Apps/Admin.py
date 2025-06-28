import random , re
from DataSets.HashTable import OpenHashTable
from DataSets.Trie import Trie
import Car

class Admin:
    def __init__(self):
        self.usename = 'admin'
        self.password = 'admin'
        self.cars_database = OpenHashTable()
        self.users_database = Trie()
        
    def plate_a_car(self , plate_number , id):

            car_color = input('inter your car color: ')
            if car_color.islower() == 'white':
                car_color = 'WT'
            elif car_color.islower() == 'black':
                car_color = 'BC'
            elif car_color.islower() == 'red':
                car_color = 'RD'
            elif car_color.islower() == 'blue':
                car_color = 'BL'
            elif car_color.islower() == 'silver':
                car_color = ' GR'
                
            else:
                car_color = 'OT'
                
            car_name = input('inter your car name: ')
            while True:
                plate = plate_number
                if re.fullmatch(r'\d{2}[a-zA-Z]\d{3}-\d{2}' , plate):
                    break
                else:
                    return ' wrong format for plate number plz try agin in form NNLNNN'
            
            car_id = ''.join(random.choice('0123456789' , k = 5))
            while True:
                production_date = input("inter the prodoction year of your car: ")
                plated_date = input('inter todays date(yyyy/mm/dd): ')
                try:
                    production_year = int(production_date.split('/')[0])
                    plated_year = int(plated_date.split('/')[0])
                    if plated_year >= production_year:
                        break
                    else:
                        return ' plated year can not before product year'
                except(ValueError):
                    return 'invalid date format. try yyy/mm/dd'
            car_object = Car(car_color , car_name , production_date , car_id , plate_number , plated_date , id)
            self.cars_database.Insert(car_id , car_object)
            return 'car added succesfully'