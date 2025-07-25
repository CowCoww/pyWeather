from urllib import request, parse
import json

# Get geolocation based on user's IP address
# This method is inacurrate, and is completely unusable if the user use VPN services
def get_IP_location() -> dict:
    with request.urlopen("http://ip-api.com/json/") as response:
        result = json.load(response)

    if not result:
        return {
            'code': 404,
            'status': 'At: get_IP_location(): Server error!'
        }
    
    return {
        'code': 200,
        'status': 'OK',
        'city': result['city'],
        'latitude': float(result["lat"]),
        'longitude': float(result["lon"])
    }

# Get geolocation based on city name
def get_city_location(city_name: str) -> dict:
    if not city_name:
        raise ValueError("At: get_city_location(): city_name is not provided!")
    
    base_url: str = "https://nominatim.openstreetmap.org/search"
    params: dict = {
        'q': city_name,
        'format': 'json',
        'limit': 1,
        # 'addressdetails': 1
    }
    
    url: str = f"{base_url}?{parse.urlencode(params)}"

    headers: dict = {
        'User-Agent': 'weather-terminal/1.0'
    }

    req = request.Request(url, headers=headers)
    with request.urlopen(req) as response:
        data = json.loads(response.read().decode())

    if not data:
        return {
            'code': 404,
            'status': 'At: get_city_location(): Server error or city not found!'
        }
    
    result = data[0]
    address = result.get('address', {})
    
    city = (
        address.get('city') or
        address.get('town') or
        address.get('village') or
        address.get('hamlet') or
        city_name
    )

    return {
        'code': 200,
        'status': 'OK',
        'city': city.title(),
        'latitude': float(result["lat"]),
        'longitude': float(result["lon"])
    }