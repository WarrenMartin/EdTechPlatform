import phonenumbers
from phonenumbers import geocoder

phone_number1=phonenumbers.parse(" 9552821329")

print(geocoder.description_for_number(phone_number1,"en"));