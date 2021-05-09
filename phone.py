import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = "+919993455420"
ch_number = phonenumbers.parse(number, "CH")

country = geocoder.description_for_number(ch_number, "en")

service_number = phonenumbers.parse(number, "RO")

service_provider = carrier.name_for_number(service_number, "en") 

print(service_provider)

print(country)
