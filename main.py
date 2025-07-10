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
    
        gnrt = display_menu('admin')
        display = generator(gnrt).__str__()
        # output = str(display)
admin_menu(admin='admin')
    
    
    
    
    
# if __name__ == "__main__":
#     initialize_system()