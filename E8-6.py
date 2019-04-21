def city_country(city_name, country_name):
    fullname = '"'+ city_name + ' '+ country_name+ '"'
    return fullname.title()


a = city_country('santiago', 'chile')
print(a)
