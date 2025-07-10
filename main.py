import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Modules import read_cars, read_city_codes, read_drivers, read_ownership_history, read_penalties, read_plates, read_users
from Modules import generator
from DataSets.Array import Array
from DataSets.Trie import Trie
from DataSets.BSTHash import HashTable
from DataSets.HashTable import OpenHashTable
from DataSets.DoublyLinkedList import DoublyLinkedList
from Apps.Admin import Admin
from Apps.User import User

def initialize_system():
    yield "Loading system data..."
    
    admin = Admin()
    user = User()
    
    users = read_users()
    admin.users_database = users
    user.users_database = users
    
    cars = read_cars()
    admin.cars_database = cars
    user.car_database = cars
    
    plates = read_plates()
    admin.plates_database = plates
    user.plates_database = plates
    
    citycodes = read_city_codes()
    admin.citycodes_database = citycodes
    user.citycode_database = citycodes
    
    drivers = read_drivers()
    admin.drivers_database = drivers
    user.drivers_database = drivers
    
    penalties = read_penalties()
    admin.penalties_database = penalties
    user.penalties_database = penalties
    
    history = read_ownership_history()
    admin.ownership_history = history
    user.owner_ship_history = history
    
    yield "Data loaded successfully!"
    return admin, user

def save_to_files(admin, user):
    try:
        with open('tests/cars.txt', 'w', encoding='utf-8') as f:
            f.write("Car ID | Car Name | Production Date | Plate Number | Color | Owner ID\n")
            for item in admin.cars_database.table:
                if item is not None and item != 'DELETED':
                    car = item[1]
                    f.write(f"{car.id} | {car.car_name} | {car.production_year} | {car.plate_number} | {car.car_color} | {car.owner_id}\n")
        
        with open('tests/users.txt', 'w', encoding='utf-8') as f:
            f.write("National Code | First Name | Last Name | Birth Date | Password\n")
            for item in admin.users_database.table:
                if item is not None and item != 'DELETED':
                    user_data = item[1]
                    f.write(f"{user_data[2]} | {user_data[0]} | {user_data[1]} | {user_data[3]} | {user_data[4]}\n")
        
        with open('tests/test_plates.txt', 'w', encoding='utf-8') as f:
            for item in admin.plates_database.table:
                if item is not None and item != 'DELETED':
                    plate = item[1]
                    f.write(f"{plate.number} | {plate.owner} | {plate.is_active}\n")
        
        with open('tests/ownership_history.txt', 'w', encoding='utf-8') as f:
            for item in admin.ownership_history.traverse():
                f.write(f"{item.car_id} | {item.owner_id} | {item.start_date} | {item.end_date} | {item.plate_number}\n")
        
        with open('tests/drivers.txt', 'w', encoding='utf-8') as f:
            f.write("Driver ID | First Name | Last Name\n")
            for item in admin.drivers_database.table:
                if item is not None and item != 'DELETED':
                    driver = item[1]
                    f.write(f"{driver.id} | {driver.first_name} | {driver.last_name}\n")
        
        with open('tests/penalties.txt', 'w', encoding='utf-8') as f:
            f.write("Penalty ID | Driver ID | Plate Number | Date | Type | Amount\n")
            for item in admin.penalties_database.traverse():
                f.write(f"{item.id} | {item.driver_id} | {item.plate_number} | {item.date} | {item.type} | {item.amount}\n")
        
        with open('tests/city_codes.txt', 'w', encoding='utf-8') as f:
            f.write("City Name | City Code\n")
            for item in admin.citycodes_database.Traverse():
                if item is not None:
                    f.write(f"{item[0]} | {item[1]}\n")
        
        yield "Changes saved to files successfully."
    except Exception as e:
        yield f"Error saving to files: {str(e)}"
    
def display_menu(role):
    if role.lower() == 'admin':
        yield "\n=== Admin Menu ==="
        yield "1. Plate a Car"
        yield "2. Show All Cars"
        yield "3. Show All Users"
        yield "4. Show LicensePlate Numbers of a City"
        yield "5. Show Cars of a City"
        yield "6. Show Car Owners of a City"
        yield "7. Search Cars by Production Year"
        yield "8. Update a Username"
        yield "9. Show Ownership History of a Car"
        yield "10. Show Ownership History"
        yield "11. Show All Drivers"
        yield "12. Change Plate Owner"
        yield "13. Back to Main Menu"

        
    elif role.lower() == 'user':
        yield "\n=== User Menu ==="
        yield "1. Generate Licence Plate Number"
        yield "2. Show My Cars"
        yield "3. Show My License Plates"
        yield "4. Show My Negative Score"
        yield "5. Show Driver's Penalties Record"
        yield "6. Show LicensePlate Number's Penalties Record"
        yield "7. Show LicensePlate History"
        yield "8. Back to Main Menu"
        
    else: 
        yield "\n=== Main Menu ==="
        yield "1. Login as Admin"
        yield "2. Login as User"
        yield "3. Register as User"
        yield "4. Exit"

def admin_login(admin):
    yield "\n=== Admin Login ==="
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    if username == "admin" and password == "admin":
        yield "Admin login successful!"
        return admin
    else:
        yield "Invalid admin credentials!"
        return None

def admin_menu(admin):
    while True:
        for message in display_menu('admin'):
            yield message
        choice = input('\nEnter Your Choice: ')
        
        try:
            if choice == "1":
                owner_id = input("Enter Owner ID: ")
                plate_number = input("Enter LicencePlate Number: ")
                car_color = input('Enter Car Color: ')
                car_name = input('Enter Car Name: ')
                production_date = input("Enter The Production Year of Car: ")
                for message in admin.plate_a_car(plate_number, owner_id, car_color, car_name, production_date):
                    yield message
                
            elif choice == '2':
                for message in admin.show_all_cars():
                    yield message
            
            elif choice == '3':
                for message in admin.show_all_users():
                    yield message
                    
            elif choice == '4':
                city_name = input("Enter City Name: ")
                for message in admin.show_plates_of_a_city(city_name):
                    yield message
                    
            elif choice == '5':
                city_name = input("Enter City Name: ")
                for message in admin.show_cars_of_a_city(city_name):
                    yield message
                    
            elif choice == '6':
                city_name = input("Enter City Name: ")
                for message in admin.show_car_owners_of_a_city(city_name):
                    yield message

            elif choice == '7':
                start = input('Enter the starting point of your time period (space for skip): ')
                end = input('Enter the ending point of your time period: ')
                for message in admin.search_cars(start, end):
                    yield message
            
            elif choice == '8':
                user_id = input("Enter User's ID: ")
                new_name = input('Enter user\'s new name: ')
                for message in admin.update_username(user_id, new_name):
                    yield message
                    
            elif choice == '9':
                car_id = input("Enter Car ID: ")
                for message in admin.show_ownership_history(car_id):
                    yield message

            elif choice == '10':
                carid = input('Enter the Car ID: ')
                for message in admin.show_ownership_history(carid):
                    yield message
            elif choice == '11':
                for message in admin.show_all_drivers():
                    yield message
            
            elif choice == '12':
                carid = input('Enter the car ID: ')
                plate_number = input('Enter the Previous Plate Number: ')
                new_plate = input('Enter the new plate Number: ')
                for message in admin.change_plate_owner(carid,plate_number,new_plate):
                    yield message
            elif choice == '13':
                break
            
            else:
                yield 'Invalid Choice. Try Again!'
                
        except Exception as e:
            yield f"Error: {e}"

def user_menu(user, user_id):
    while True:
        for message in display_menu('user'):
            yield message
        choice = input('\nEnter Your Choice: ')
        
        try:
            if choice == "1":
                city_name = input("Enter City Name: ")
                driver_id = input('Enter Your id: ')
                for message in user.license_plate_generator(city_name, driver_id):
                    yield message
                
            elif choice == '2':
                for message in user.show_user_cars(user_id):
                    yield message
            
            elif choice == '3':
                for message in user.show_user_platelicenses(user_id):
                    yield message
                    
            elif choice == '4':
                national_code = input('Enter your national code: ')
                drive_id = input('Enter yout Drive ID: ')
                for message in user.show_users_negative_score(national_code,drive_id):
                    yield message
                    
            elif choice == '5':
                driver_id = input('Enter your driving ID: ')
                for message in user.show_users_penalties_based_driverid(driver_id):
                    yield message
                    
            elif choice == '6':
                id = input('Enter the ID of yours: ')
                plate_num = input("Enter the number of Plate: ")
                for message in user.show_users_penalties_based_platenumber(id,plate_num):
                    yield message

            elif choice == '7':
                plate = input("Enter the plate number: ")
                for message in user.history_of_licenseplate(plate):
                    yield message
                    
            elif choice == '8':
                break
            
            else:
                yield 'Invalid Choice. Try Again!'
                
        except Exception as e:
            yield f"Error: {e}"

def main():
    yield "=== Car License Plate Management System ==="
    
    try:
        admin, user = yield from initialize_system()
    except Exception as e:
        yield f"Error initializing system: {e}"
        return
    
    while True:
        for message in display_menu('main'):
            yield message
        choice = input('\nEnter your choice: ')
        
        try:
            if choice == '1': 
                admin_instance = None
                for message in admin_login(admin):
                    yield message
                    if "Admin login successful!" in message:
                        admin_instance = admin
                if admin_instance:
                    for message in admin_menu(admin_instance):
                        yield message
                
            elif choice == '2':  
                login_success_id = None
                user_instance = None
                id = input("Enter User Id: ")
                password = input('Enter Your Password: ')
                for message in user.user_login(id , password):
                    yield message
                    if 'Logged in Successfully' in message:
                        login_success_id = message.split()[0]
                        user_instance = user
                if login_success_id and user_instance:
                    for message in user_menu(user_instance, login_success_id):
                        yield message
 
            elif choice == '3':  
                for message in user.user_register():
                    yield message
            
            elif choice == '4': 
                for message in save_to_files(admin, user):
                    yield message
                yield "Thank you for using the system. Goodbye!"
                break
            
            else:
                yield "Invalid choice. Please try again!"
                
        except Exception as e:
            yield f"Error: {e}"

if __name__ == "__main__":
    for message in main():
        print(message)