import os
from pathlib import Path
import sys
from DataSets.Array import Array
from DataSets.HashTable import OpenHashTable
from Apps.Car import Car
from DataSets.Trie import Trie




def read_city_codes(filepath='tests/citycode.txt'):
    city_codes = Array(100)
    # try:
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

