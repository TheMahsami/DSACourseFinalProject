import os
from pathlib import Path
import sys
from DataSets.Array import Array




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
read_city_codes()