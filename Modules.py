import os
from pathlib import Path
import sys
from DataSets.Array import Array
from DataSets.HashTable import OpenHashTable
from DataSets.BSTHash import HashTable
from Apps.Car import Car
from DataSets.Trie import Trie
from Apps.Driver import Driver
from Apps.Penalty import Penalty
from Apps.Plates import LicencePlste
from Apps.History import HistoryData
from DataSets.DoublyLinkedList import DoublyLinkedList




def read_city_codes(filepath='tests/citycode.txt'):
    city_codes = Array(100)
    with open(filepath , 'r') as f:
        next(f , None)
        for line in f:
                #this ia a tuple
            parts = line.strip().split(' | ')
            citycoded = parts[0].strip()
            cityname = parts[1].strip()
            if cityname and citycoded:
                city_codes.insert(citycoded , cityname)

    return city_codes

def read_cars(filepath='tests/cars.txt'):
    cars = OpenHashTable()
    with open(filepath , 'r') as f:
        next(f , None)
        for line in f:
            parts = line.strip().split(' | ')
            if len(parts) < 6:
                continue
            car_id = parts[0].strip()
            car_name = parts[1].strip()
            product_date = parts[2].strip()
            plate_number = parts[3].strip()
            color = parts[4].strip()
            owner_id = parts[5].strip()
            car_obj = Car(color , car_name , product_date , car_id , plate_number , owner_id , plated_date=None )
            cars.Insert(car_id , car_obj)
    return cars

def read_users(filepath='tests/users.txt'):
    from Apps.User import User
    User_panel = User()
    users = Trie()
    with open(filepath , 'r') as f:
        next(f , None)
        for line in f:
            parts = line.strip().split(' | ')
            first_name = parts[1].strip()
            last_name = parts[2].strip()
            national_code = parts[0].strip()
            birth_date = parts[3].strip()
            password = User_panel._password_hash_function(parts[4].strip())
            user_data = (first_name , last_name , national_code , birth_date , password)
            users.Insert(national_code ,user_data)
    return users

#phase 3 functionality
def read_drivers(filepath='tests/drivers.txt'):
    drivers = Trie()
    with open(filepath , 'r') as f:
        next(f , None)
        for line in f:
            parts = line.strip().split(' | ')
            driver_data = Driver(parts[0] , parts[1] , parts[2])
            drivers.Insert(parts[0] , driver_data)
    return drivers

def read_penalties(filepath='tests/penalties.txt'):
    penalties = DoublyLinkedList()
    with open(filepath , 'r') as f:
        next(f , None)
        for line in f:
            parts = line.strip().split(' | ')
            penalty_data = Penalty(parts[0] , parts[1] , parts[2] , parts[3], parts[4] , parts[5])
            penalties.insert(penalty_data)
    
    return penalties

def read_ownership_history(filepath='tests/ownership_history.txt'):
    ownership_history = DoublyLinkedList()
    with open(filepath , 'r') as f:
        for line in f:
            parts = line.strip().split(' | ')
            data = HistoryData(parts[0] , parts[1] , parts[2], parts[3] , parts[4])
            ownership_history.insert(data)
            
    return  ownership_history

#________________________________________________________________________
def read_plates(filepath='tests/test_plates.txt'):
    plates = HashTable()
    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split(' | ')
            number = parts[0].strip()
            owner = parts[1].strip()
            is_active = parts[2].strip().capitalize() == 'True' if len(parts) > 2 else False
            plate_data = LicencePlste(number=number, owner=owner, is_active=is_active)
            plates.insert(number, plate_data)

    return plates
#___________________________________________________________________________________________
             
#failed try
# class generator:
#     def __init__(self , generator):
#         self.generator = generator
    
#     def __str__(self):
#         res = ''
#         for output in self.generator:
#             res += output + '\n'
#         yield res
    
# read_city_codes()