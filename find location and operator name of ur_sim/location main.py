# pls add your Phone NUmber on test1.py file 
import phonenumbers
from test1 import number

# To check the location
from phonenumbers import geocoder
ch_num = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_num, "en"))

# To check the sim operator of your number
from phonenumbers import carrier
serv_num = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(serv_num, "en"))
