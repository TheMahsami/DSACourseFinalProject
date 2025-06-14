from Modules import read_city_codes

class User:
    def __init__(self,fname,lname,ncode,password):
        self.id = ncode
        self.ncode = ncode
        self.name = fname
        self.lastname = lname
        self.password = password
        self.cars = None
        
    def _license_plate_generator(request , citycode ):
        