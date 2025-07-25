# pyWeather
A weather app inside the terminal, no external library needed!

API Services Used:
 - Weather data & forecasts: open-meteo.com
 - City name to coordinates: nominatim.openstreetmap.org
 - IP adress to coordinates: ip-api.com

Requirement:
 - Python 3.8 or later
 - Windows 10 or later

How to use:
 - Option 1: Run main.py as a normal Python file: 
    python main.py
 - Option 2: Global terminal (Windows)
   To make it easily accessible by typing 'weather' in any terminal (or cmd)
   1. Edit the weather.cmd file:
      + Replace python "your_path_to_this_folder\Weather\main.py" with the path to your actual main.py file
   2. Add the folder to your system's PATH
   3. Now, open the terminal. You can now type in 'weather' to run the program
   + If you want another command name, change the name of the .cmd file to whatever you want it to be.

Features:
 - Auto-detect your location via IP (low accuracy)
 - Select a custom city
 - Set a default city
 - Interface with colors
 - No API keys or external library required
