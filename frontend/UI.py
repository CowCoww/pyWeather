from .terminal import Terminal
from datetime import datetime
from . import color
from . import icons
from backend import weather
from backend import location
from data import config


def confirm_action(terminal: Terminal, prompt: str) -> bool:
    response = terminal.input(prompt=prompt, prompt_foregr=color.YELLOW, input_foregr=color.EMERALD).strip().lower()
    return response in ['y', 'yes', 'yep', 'yeah', 'ya', 'yup', 'sure', 'ok']

def get_user_location(terminal: Terminal, default_city: str | None) -> dict:
    terminal.print("Leave blank", foregr=color.LIGHT_GRAY, end=' ')
    terminal.print("for IP detection." if (not default_city) else f"to choose {default_city}.", foregr=color.LIGHT_GRAY)
    city_name: str = terminal.input("City name: ", prompt_foregr=color.EMERALD)

    result: dict

    if not city_name:
        if not default_city:
            terminal.print("Approximating your location via IP address...", foregr=color.CYAN)
            result = location.get_IP_location()
        else:
            terminal.print("Locating your city...", foregr=color.CYAN)
            result = location.get_city_location(default_city)
    else:
        terminal.print("Locating your city...", foregr=color.CYAN)
        result = location.get_city_location(city_name)

    if result['code'] == 404:
        terminal.print("Something went wrong! We cannot get your location!", foregr=color.RED)
        raise ValueError(result['status'])

    return result

def display_data_header(
        terminal: Terminal, location: dict, weather_report, \
        x_pos: int = 0, y_pos: int = 0) -> None:
    # The city
    terminal.print_text_line([
        (f"│ City     : ", color.WHITE),
        (f"{location['city']}", color.LIGHT_BLUE)
    ], x=x_pos, y=y_pos)

    # Latitude and Longitude
    terminal.print_text_line([
        (f"│ Lat - Lon: ", color.WHITE),
        (f"(", color.LIGHT_BLUE),
        (f"{weather_report['latitude']:.3f}", color.YELLOW),
        (", ", color.LIGHT_BLUE),
        (f"{weather_report['longitude']:.3f}", color.YELLOW),
        (f")", color.LIGHT_BLUE)
    ], x=x_pos, y=y_pos + 1)

    # Time when weather data are last updated by openmeteo.com
    dt = datetime.fromisoformat(weather_report['current']['time'])
    terminal.print_text_line([
        ("│ Data time: ", color.WHITE),
        (f"{dt.strftime('%A, %b %d')}", color.LIGHT_BLUE),
        ("; ", color.WHITE),
        (f"{dt.strftime('%H:%M')}", color.YELLOW)
    ], x=x_pos, y=y_pos + 2)

    # Time zone of the location weather data is gotten
    terminal.print_text_line([
        (f"│ Time zone: ", color.WHITE),
        (f"{weather_report['timezone_abbreviation']} ", color.LIGHT_GREEN),
        (f"(", color.WHITE),
        (f"{weather_report['timezone']}", color.LIGHT_BLUE),
        (f")", color.WHITE)
    ], x=x_pos, y=y_pos + 3)

def display_current_weather(
        terminal: Terminal, current, units, \
        x_pos: int, y_pos: int) -> None:
    x_text: int = x_pos + 15

    # Print side border
    for i in range(4):
        terminal.print('│', x=x_pos, y=y_pos+i+1)

    # Get weather code icon
    icons.get_icon(terminal, x=x_pos+1, y=y_pos, code=current['weather_code'])

    # Weather code
    terminal.move_cursor(x_text + 1, y_pos)
    terminal.print(weather.get_weather_description(current['weather_code']), foregr=color.LIGHT_BLUE)
    
    # Temperature
    current_temp: float = current['temperature_2m']
    apparent_tmp: float = current['apparent_temperature']
    
    terminal.print_text_line([
        (f"│ Temp: ", color.WHITE),
        (f"{current_temp:.1f} ", color.get_temperature_color(current_temp)),
        (f"{units['temperature_2m']} ", color.WHITE),
        (f"(apr: ", color.WHITE),
        (f"{apparent_tmp:.1f} ", color.get_temperature_color(apparent_tmp)),
        (f"{units['apparent_temperature']})", color.WHITE)
    ], x=x_text, y=y_pos + 1)

    # Wind speed and direction
    terminal.print_text_line([
        (f"│ Wind: ", color.WHITE),
        (f"{current['wind_speed_10m']:.1f} ", color.LIGHT_BLUE),
        (f"{units['wind_speed_10m']} (dir: ", color.WHITE),
        (f"{weather.get_wind_direction(current['wind_direction_10m'])}", color.LIGHT_BLUE),
        (f" : ", color.WHITE),
        (f"{current['wind_direction_10m']}", color.LIGHT_BLUE),
        (f"{units['wind_direction_10m']})", color.WHITE)
    ], x=x_text, y=y_pos + 2)

    # Precipitation
    precip = current['precipitation']
    terminal.print_text_line([
        (f"│ Precip: ", color.WHITE),
        (f"{precip:.2f} ", color.get_precip_color(precip)),
        (f"{units['precipitation']}", color.WHITE)
    ], x=x_text, y=y_pos + 3)

    terminal.print_text_line([
        ("│ Humidity: ", color.WHITE),
        (f"{current['relative_humidity_2m']} ", color.LIGHT_BLUE),
        ("%", color.WHITE)
    ], x=x_text, y=y_pos + 4)

def manage_default_city(terminal: Terminal, default_city: str | None) -> None:
    if default_city is None:
        terminal.print("Do you want to set a default city for faster experience?", foregr=color.GRAY)
        terminal.print("Type your default here, or leave blank to skip: ", foregr=color.GRAY, end='')
    else:
        terminal.print("Do you want to edit your default city?", foregr=color.GRAY)
        terminal.print("Type your new default, or leave blank to skip: ", foregr=color.GRAY, end='')

    city_name: str = terminal.input(prompt="", input_foregr=color.YELLOW)

    if city_name:
        if confirm_action(terminal, "Are you sure? ([Y]es / [N]o) "):
            config.save_default_city(city_name.title())
            terminal.print(f"Changes saved! Your default city is now {city_name.title()}!", foregr=color.LIGHT_GREEN)
        else:
            terminal.print(f"Input implied as [N]o, action canceled!", foregr=color.RED)
    else:
        terminal.print("No changes then!", foregr=color.LIGHT_PURPLE)

