from urllib import request
import json

def get_weather_data(geolocation: dict):
    weather_url : str = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={geolocation['latitude']}&longitude={geolocation['longitude']}&"
        f"current=temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,wind_direction_10m,precipitation,weather_code,cloud_cover&"
        f"daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum&"
        f"hourly=temperature_2m,weather_code,precipitation,precipitation_probability&timezone=auto"
    )
    with request.urlopen(weather_url) as response:
        weather_data = json.load(response)

    return weather_data


WMO_description: dict[int, str] = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",

    45: "Fog",
    48: "Depositing rime fog",

    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",

    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",

    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",

    66: "Light freezing rain",
    67: "Heavy freezing rain",

    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",

    77: "Snow grains",

    80: "Slight rain shower",
    81: "Moderate rain shower",
    82: "Violent rain shower",

    85: "Slight snow shower",
    86: "Heavy snow shower",

    95: "Thunderstorm (slight or moderate)",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}

def get_weather_description(WMO_code : int):
    return WMO_description.get(WMO_code, "Unknow weather condition!")

def get_wind_direction(degree: float) -> str:
    directions = [
        "N", "NNE", "NE", "ENE", 
        "E", "ESE", "SE", "SSE", 
        "S", "SSW", "SW", "WSW", 
        "W", "WNW", "NW", "NNW"
    ]
    index = int((degree % 360) / 22.5 + 0.5) % 16
    return directions[index]

