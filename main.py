import  sys  , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) , '..')))
from Modules import read_cars , read_city_codes , read_drivers , read_ownership_history , read_penalties , read_plates , read_users
from Modules import generator
from DataSets.Array import Array
from DataSets.Trie import Trie
from DataSets.BSTHash import HashTable
from DataSets.HashTable import OpenHashTable
from DataSets.DoublyLinkedList import DoublyLinkedList
from Apps.Admin import Admin
from Apps.User import User

def initialize_system():
    users = read_users()
    Admin().users_database = users
    User().users_database = users
    
    cars = read_cars()
    Admin().cars_database = cars
    User().car_database =  cars
    
    plates = read_plates()
    Admin().plates_database = plates
    User().plates_database = plates
    
    citycodes = read_city_codes()
    Admin().citycodes_database = citycodes
    User().citycode_database = citycodes
    
    drivers = read_drivers()
    # Admin(). = users
    User().drivers_database = drivers
    
    penalties = read_penalties()
    # Admin().pe_database = users
    User().penalties_database = penalties
    
    history = read_ownership_history()
    Admin().ownership_history = history
    User().owner_ship_history = history
    
    yield 'Data Loaded'
    
    
    
def display_menu(role):
    if role.lower() == 'admin':
        yield "\n Admin Menu:  "
        yield "1. Plate a Car"
        yield "2. Show All Cars"
        yield "3. Show All Users"
        yield "4. Show LicensePlate Numbers of a City"
        yield "5. Show Cars of a City"
        yield "6. Show Car Owners of a City"
        yield "7. Search Cars by Production Year"
        yield "8. Update a Username"
        yield "9. Show Ownership History of a Car"
        yield "10. Back to Main Menu"
        
    elif role.lower() == 'user':
        yield "\n User Menu: "
        yield "1. Generate Licence Plate Number"
        yield "2. Show My Cars"
        yield "3. Show My License Plates"
        yield "4. Show My Negative Score"
        yield "5. Show Driver's Penalties Record"
        yield "6. Show LicensePlate Number's Penalties Record"
        yield "7. Show LicensePlate History"
        yield "8. Back to Main Menu"
        
     #main display   
    else:
        yield "\n Main Menu "
        yield "1. Login as Admin"
        yield "2. Login as User"
        yield "3. Register as User"
        yield "4 Exit"
        
def admin_menu(admin):
    while True:
        yield from display_menu('admin')
            
        choise = input('\nEnter Your Choise: ')
        
        if choise == "1":
            owner_id = input("Enter Owner Id: ")
            plate_number = input("Enter LicencePlate Number: ")
            car_color = input('Enter Car Color: ')
            car_name = input('Enter Car Name: ')
            production_date = input("Enter The Production Year of Car: ")
            for massage in admin.plate_a_car(plate_number , owner_id , car_color , car_name , production_date):
                yield massage
            
        elif choise == '2':
            for massage in admin.show_all_cars():
                yield massage
        
        elif choise == '3':
            for massage in admin.show_all_users():
                yield massage
                
        elif choise == '4':
            city_name = input("enter City Name: ")
            for massage in admin.show_plates_of_a_city(city_name):
                yield massage
                
        elif choise == '5':
            city_name = input("enter City Name: ")
            for massage in admin.show_plates_of_a_city(city_name):
                yield massage
                
        elif choise == '6':
            city_name = input("enter City Name: ")
            for massage in admin.show_car_owners_of_a_city(city_name):
                yield massage

        elif choise =='7':
            start = input('inter the starting point of your time period(space for skip): ')
            end = input('inter the ending point of your time period: ')
            for massage in admin.search_cars(start , end):
                yield massage
        
        elif choise == '8':
            id = input("Enter User's ID: ")
            new_name = input('inter users new name: ')
            for massage in admin.update_username(id , new_name):
                yield massage
                
        elif choise == '9':
            car_id = input("Enter Car ID: ")
            for massage in admin.show_ownership_history(car_id):
                yield massage
                
        elif choise == '10':
            break
        
        else:
            yield 'Invalid Choise.Try Again!! '
            
def user_menu(user):
    while True:
        yield from display_menu('user')
        
        choise = input('\nEnter Your Choise: ')
        
        if choise == "1":
            id = input("Enter Your ID: ")
            city_name = input("Enter City Name: ")
            for massage in user.license_plate_generator(city_name , id):
                yield massage
            
        elif choise == '2':
            id = input("Enter Your ID: ")
            for massage in user.show_user_car():
                yield massage
        
        elif choise == '3':
            id = input("Enter Your ID: ")
            for massage in user.show_user_platelicenses():
                yield massage
                
        elif choise == '4':
            national_code = input('Enter Your National ID: ')
            driver_id = input('Enter Your Driver ID: ')
            for massage in user.show_users_negative_score(national_code , driver_id):
                yield massage
                
        elif choise == '5':
            driver_id = input('Enter Your Driver ID: ')
            for massage in user.show_users_penalties_based_driverid(driver_id):
                yield massage
                
        elif choise == '6':
            id = input('Enter Your National ID: ')
            plate_number = input('Enter Your LicensePlate Number: ')
            for massage in user.show_users_penalties_based_platenumber(id , plate_number):
                yield massage

        elif choise =='7':
            plate_number = input('Enter Your LicencePlate Number: ')
            for massage in user.history_of_licenseplate(plate_number):
                yield massage
                
        elif choise == '8':
            break
        
        else:
            yield 'Invalid Choise.Try Again!! '
        
        
    
            
                
for massage in admin_menu(admin='admin'):
    print(massage)
    
    
    
    
    
# if __name__ == "__main__":
#     initialize_system()