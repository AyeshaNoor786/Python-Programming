from countryinfo import CountryInfo
count=input("Enter Country Name: ")
country = CountryInfo(count)
print("Capital: ",country.capital())
print("Currencies: ",country.currencies())
print("Languages: ",country.languages())
print("Borders: ",country.borders())
print("Other names: ",country.alt_spellings())