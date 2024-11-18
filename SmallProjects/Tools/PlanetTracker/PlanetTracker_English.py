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
