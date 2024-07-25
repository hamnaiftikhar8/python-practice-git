def country_cap(a):
    countries = {}
    for key, value in a.items():
        country = key.capitalize()
        countries[country] = value

    return countries 

country = {'Pakistan':'Islamabad', 'India':'Mumbai', 'Turkey':'Istanbul'}

print(country_cap(country))
