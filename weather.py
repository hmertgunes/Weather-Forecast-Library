import requests


class Weather:
    """
    Creates a Weather object getting an apikey as input and either a city name or lat-lon coordinates.
    Shows user date-time, temperature, weather condition, city and country

    # If user wants to extend quantities which program shows;
    # Should analyze what the self.Content made of step by step and update "def next_12_simplified(self):"

    Package use example:

    # Apikey written in below may be broken so,
    # User should get the own api key from openweathermap.org
    # Create a Weather object using a city name:
    # Set units variable as you please such as "metric"
    >>> weather1 = Weather(units="metric", apikey="97a2d427c6085137b8517556f659a506",city="istanbul")

    # If you want to create a Weather object using lat-lon coordinates:
    # You can give random coordinates and easily can see which country and city is that
    >>> weather2 = Weather(units="imperial", apikey="97a2d427c6085137b8517556f659a506", lat=10, lon=42)

    # Get simplified weather data in form of list for the next 12 hours in every 3 hours
    >>> weather1.next_12_simplified()

    # Print simplified weather data in form of list for the next 12 hours in every 3 hours
    >>> print(weather1.next_12_simplified())  #  User can "pprint" for better looking
    """

    def __init__(self, units, apikey, city=None, lat=None, lon=None):
        self.city = city
        self.units = units  # Standard, metric, imperial
        self.apikey = apikey  # Unique key
        self.lat = lat  # latitude
        self.lon = lon  # longitude

        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={self.city}&" \
                  f"appid={self.apikey}&units={self.units}"
            req = requests.get(url)
            self.content = req.json()

        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&" \
                  f"lon={self.lon}&appid={self.apikey}&units={self.units}"
            req = requests.get(url)
            self.content = req.json()  # json() because we want to data in form of dictionary

        else:  # Raising error due to calling attention to warning which written below
            raise TypeError("You have to provide either city or lat-lon coordinates.")

    def next_12_simplified(self):
        list_all = []
        for i in range(1, 6):
            time = self.content["list"][i]["dt_txt"]
            temp = self.content["list"][i]["main"]["temp"]
            description = self.content["list"][i]["weather"][0]["description"]
            city = self.content["city"]["name"]
            country = self.content["city"]["country"]
            icon = self.content["list"][i]["weather"][0]["icon"]
            list_of = [time, temp, description, city, country, icon]  # Separated to 5 lists by every 3 hour
            list_all.append(list_of)
        return list_all
