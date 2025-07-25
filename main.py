from frontend.terminal import Terminal
from backend.weather import get_weather_data
from frontend.UI import *
from data import config

if __name__ == '__main__':
    # Init tthe terminal
    terminal = Terminal()
    terminal.clear()

    # Get the default city from config
    default_city = config.load_default_city()
    print(default_city, "hihi")

    # Get the user geolocation
    geolocation = get_user_location(terminal, default_city)

    # Fetching weather data
    terminal.print("Pulling weather data...", foregr=color.CYAN)
    weather_data = get_weather_data(geolocation)


    terminal.clear()
    terminal.print("WEATHER REPORT", x=0, y=0, foregr=color.LIGHT_GREEN, bold=True)

    # Display the weather data
    display_current_weather(terminal, weather_data['current'], weather_data['current_units'], x_pos=0, y_pos=1)

    # Display the data's header
    display_data_header(terminal, geolocation, weather_data, x_pos=53, y_pos=2)

    # Manage the default city at the end
    terminal.print("\n\n")
    manage_default_city(terminal, default_city)

    # Have a good day!! To whom reading the code
    terminal.print("\nHave a good day!", foregr=color.PINK, end=' ')
    terminal.print("<3", foregr=color.RED)