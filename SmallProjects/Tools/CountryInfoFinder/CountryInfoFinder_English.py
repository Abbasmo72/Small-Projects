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
