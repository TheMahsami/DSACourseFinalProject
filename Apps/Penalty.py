class Penalty:
    def __init__(self , id , driver_id , plate_number , penalty_date , penalty_level , disc):
        self.penalty_id = id
        self.driver_id = driver_id 
        self.plate_number = plate_number
        self.penalty_date = penalty_date
        self.level = penalty_level
        self.decription = disc