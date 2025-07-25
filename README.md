# pyWeather
**A weather app inside the terminal, no external library needed!**

### API Services Used:
 - Weather data & forecasts: [open-meteo.com](https://open-meteo.com/)
 - City name to coordinates: [nominatim.openstreetmap.org](https://nominatim.openstreetmap.org/)
 - IP adress to coordinates: [ip-api.com](https://ip-api.com/)

### Requirement:
 - __Python__ 3.8 or later
 - __Windows__ 10 or later

### How to use:
 - __Option 1__: Run main.py as a normal Python file:
   ```bash
    python main.py
 - __Option 2__: Global terminal (Windows)
   To make it easily accessible by typing __'weather'__ in any terminal (or cmd)
   1. Edit the weather.cmd file:
      + Replace __python "your_path_to_this_folder\Weather\main.py"__ with the path to your actual main.py file
   2. Add the folder to your __system's PATH__
   3. Now, open the terminal. You can now type in __'weather'__ to run the program
   + If you want __another command name__, change the name of the .cmd file to whatever you want it to be.

### Features:
 - Auto-detect your location via IP (low accuracy)
 - Select a custom city
 - Set a default city
 - Interface with colors
 - No API keys or external library required
