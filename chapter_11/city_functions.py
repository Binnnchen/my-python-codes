def get_city_information(city,country,population=""):
    """返回城市信息"""
    if population:
        message=city.title()+", "+country.title()+" - population "+str(population)
        return message
    else:
        message=city.title()+", "+country.title()
        return message


