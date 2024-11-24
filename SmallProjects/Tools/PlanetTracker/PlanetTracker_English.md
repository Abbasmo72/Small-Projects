## Astronomical Planet Position Calculator Using Astropy
This program is designed to determine the current position of a specific planet relative to Earth’s location (specifically from the Greenwich Observatory). It utilizes the Astropy library, which provides tools for working with astronomical data. Here's an explanation of its functionality:
1. Getting the Current Time: The program uses the astropy.time module to fetch the current time in a format suitable for astronomical calculations.
2. Setting Earth’s Location: The Earth's location is retrieved using a function that fetches the coordinates of the Greenwich Observatory. These coordinates are used as a reference for determining the planet's position.
3. Selecting the Planet: The user enters the name of the desired planet. The name is converted to lowercase to match the standard format required by the library.
4. Calculating the Planet’s Position: Using the get_body function from the astropy.coordinates module, the program calculates the planet’s position at the current time relative to Earth. The position includes two key values:
   - Right Ascension (RA): The angular coordinate of the planet along the celestial equator.
   - Declination (Dec): The angular coordinate of the planet along the celestial meridian.
5. Displaying the Result: The calculated position, including RA and Dec in celestial coordinates, is displayed. The planet's name is automatically capitalized for better readability.

## Use Case:
This program allows astronomy enthusiasts to view the precise position of a planet at the current time, as observed from Earth and based on a specific reference location (Greenwich). It is simple, practical, and serves as an educational tool for understanding how to work with astronomical data.

## Python Code
```python
from astropy.coordinates import get_body, EarthLocation  # Import necessary modules for determining planetary positions
from astropy.time import Time  # Import the time module to get the current time

now = Time.now()  # Get the current time

# Get the location of Earth from the Greenwich site
location = EarthLocation.of_site('greenwich')

# Get the name of the planet from the user and convert it to lowercase
planet_name = input("Enter the name of the planet: ").lower()

# Get the planet's position at the current time relative to Earth's location (Greenwich site)
planet_position = get_body(planet_name, now, location)

# Display the planet's position, including Right Ascension (RA) and Declination (Dec)
print(f"{planet_name.capitalize()} "  # Display the planet's name with the first letter capitalized
      f"Position: RA = {planet_position.ra}, "  # Display the Right Ascension (RA)
      f"Dec = {planet_position.dec}")  # Display the Declination (Dec)

```
