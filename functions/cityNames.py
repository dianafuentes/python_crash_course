#call the function with atleast three city-country pairs, and print values that are returned. 

def cityCountry(city, country):
  cities = (f"{city.title()} is in {country.title()}.")
  print(cities)

cityCountry('Santiago', 'chile')
cityCountry('Leon', 'Guanajuato')
cityCountry('Dallas', 'Texas')

