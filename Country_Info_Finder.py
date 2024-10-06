from countryinfo import CountryInfo

# دریافت نام کشور از کاربر
country = CountryInfo(input("Enter Country Name:"))

# نمایش اطلاعات مختلف درباره کشور
print("Country Name:", country.name())
print("Capital:", country.capital())
print("Population:", country.population())
print("Area (in square kilometers):", country.area())
print("Region:", country.region())
print("Subregion:", country.subregion())
print("Demonym:", country.demonym())
print("Currencies:", country.currencies())
print("Languages:", country.languages())
print("Borders:", country.borders())
