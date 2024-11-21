## Displaying Comprehensive Information About Countries
This script uses the countryinfo library to display detailed and useful information about a country entered by the user. The functionality is explained below:
1. Importing the countryinfo library:
   - This library provides information about countries, such as their name, population, languages, and more.
2. Getting the country name from the user:
   - The script prompts the user to enter the name of a country, which is used as input for the CountryInfo object.
3. Creating a CountryInfo object:
   - An object country is created for the entered country, which retrieves all related data using the library.
4. Displaying country information:
- The following information is fetched using various methods of the country object and printed:
   - Country Name: The name() method displays the name of the country.
   - Capital: The capital() method returns the capital of the country.
   - Population: The population() method prints the population of the country.
   - Area: The area() method shows the area of the country in square kilometers.
   - Region and Subregion: The region() and subregion() methods provide the geographical region and subregion.
   - Demonym: The demonym() method gives the term used to describe the people of the country.
   - Currencies: The currencies() method displays the currencies used in the country.
   - Languages: The languages() method lists the languages spoken in the country.
   - Borders: The borders() method returns the countries sharing borders with the given country.
 
## Features
- User Interaction: The script interacts with the user by asking for a country name.
- Comprehensive Information: It provides detailed data such as capital, population, languages, and bordering countries.
- Ease of Use: The user only needs to enter a country name to retrieve all relevant information.

## Python Code
```python
from countryinfo import CountryInfo

# Get the country name from the user
country = CountryInfo(input("Enter Country Name:"))

# Display various information about the country
print("Country Name:", country.name())  # Print the name of the country
print("Capital:", country.capital())  # Print the capital of the country
print("Population:", country.population())  # Print the population of the country
print("Area (in square kilometers):", country.area())  # Print the area of the country in square kilometers
print("Region:", country.region())  # Print the region where the country is located
print("Subregion:", country.subregion())  # Print the subregion where the country is located
print("Demonym:", country.demonym())  # Print the demonym (term for the people) of the country
print("Currencies:", country.currencies())  # Print the currencies used in the country
print("Languages:", country.languages())  # Print the languages spoken in the country
print("Borders:", country.borders())  # Print the countries that share borders with the country
```
