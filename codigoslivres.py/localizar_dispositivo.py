from geopy.geocoders import Nominatim

def get_device_location(ip_address):
    geolocator = Nominatim(user_agent="myapp")
    location = geolocator.geocode(ip_address)
    return location.latitude, location.longitude

ip_address = "186.193.200.76"  # Exemplo: Endereço IP
latitude, longitude = get_device_location(ip_address)
print(f"Latitude: {latitude}, Longitude: {longitude}")