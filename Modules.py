import os
import sys
from DataSets.Array import Array

# def Read_From_Text(filepath):
#     array = []
#     try:
#         with open(filepath , 'r' , encoding='utf-8') as file:
#             for line in file:
#                 array.append(line.strip("-"))
#                 print(array)
#     except Exception as e:
#         print(f'errpr reading file')
        
        
# filename = "tests/Doctors.txt"
# print(Read_From_Text(filename))
    
#addres dahi qer mostaqim
address = "./tests/Doctors.txt"
try:
    f = open(address , "r")
    print(f)
    f.close()
except:
    print("hello")
    
    
    
def read_cityy_codes(filepath = "test/citycode.txt"):
    city_codes = Array(100)
    # try:
    with open(filepath , 'r') as f:
        next(f , None)
        for line in f:
                #this ia a tuple
            parts = line.strip().split('|')
            citycoded = parts[0]
            cityname = parts[1]
            print(parts)
            
read_cityy_codes()