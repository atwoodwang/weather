from urllib import request
import sys
import json
from datetime import date, timedelta

base_url = "http://api.worldweatheronline.com/free/v2/weather.ashx"

codes = {'113': 'iconSunny',
         '116': 'iconPartlyCloudy',
         "119": 'iconCloudy',
         '122': 'iconVeryCloudy',
         '143': 'iconFog',
         '176': 'iconLightShowers',
         '179': 'iconLightSleetShowers',
         '182': 'iconLightSleet',
         '185': 'iconLightSleet',
         '200': 'iconThunderyShowers',
         '227': 'iconLightSnow',
         '230': 'iconHeavySnow',
         '248': 'iconFog',
         '260': 'iconFog',
         '263': 'iconLightShowers',
         '266': 'iconLightRain',
         '281': 'iconLightSleet',
         '284': 'iconLightSleet',
         '293': 'iconLightRain',
         '296': 'iconLightRain',
         '299': 'iconHeavyShowers',
         '302': 'iconHeavyRain',
         '305': 'iconHeavyShowers',
         '308': 'iconHeavyRain',
         '311': 'iconLightSleet',
         '314': 'iconLightSleet',
         '317': 'iconLightSleet',
         '320': 'iconLightSnow',
         '323': 'iconLightSnowShowers',
         '326': 'iconLightSnowShowers',
         '329': 'iconHeavySnow',
         '332': 'iconHeavySnow',
         '335': 'iconHeavySnowShowers',
         '338': 'iconHeavySnow',
         '350': 'iconLightSleet',
         '353': 'iconLightShowers',
         '356': 'iconHeavyShowers',
         '359': 'iconHeavyRain',
         '362': 'iconLightSleetShowers',
         '365': 'iconLightSleetShowers',
         '368': 'iconLightSnowShowers',
         '371': 'iconHeavySnowShowers',
         '374': 'iconLightSleetShowers',
         '377': 'iconLightSleet',
         '386': 'iconThunderyShowers',
         '389': 'iconThunderyHeavyRain',
         '392': 'iconThunderySnowShowers',
         '395': 'iconHeavySnowShowers'
         }

icons = {
    'iconSunny': [
        '\033[38;5;226m    \\   /    \033[0m',
        '\033[38;5;226m     .-.     \033[0m',
        '\033[38;5;226m  ― (   ) ―  \033[0m',
        '\033[38;5;226m     `-’     \033[0m',
        '\033[38;5;226m    /   \\    \033[0m'],
    'iconPartlyCloudy': [
        "\033[38;5;226m   \\  /\033[0m      ",
        "\033[38;5;226m _ /\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m   \\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "             "],
    'iconCloudy': [
        "             ",
        "\033[38;5;250m     .--.    \033[0m",
        "\033[38;5;250m  .-(    ).  \033[0m",
        "\033[38;5;250m (___.__)__) \033[0m",
        "             "],
    'iconVeryCloudy': [
        "             ",
        "\033[38;5;240;1m     .--.    \033[0m",
        "\033[38;5;240;1m  .-(    ).  \033[0m",
        "\033[38;5;240;1m (___.__)__) \033[0m",
        "             "],
    'iconLightShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;111m     ‘ ‘ ‘ ‘ \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m"],
    'iconHeavyShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m",
        "\033[38;5;21;1m   ‚‘‚‘‚‘‚‘  \033[0m",
        "\033[38;5;21;1m   ‚’‚’‚’‚’  \033[0m"],
    'iconLightSnowShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;255m     *  *  * \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m"],
    'iconHeavySnowShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m",
        "\033[38;5;255;1m    * * * *  \033[0m",
        "\033[38;5;255;1m   * * * *   \033[0m"],
    'iconLightSleetShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;111m     ‘ \033[38;5;255m*\033[38;5;111m ‘ \033[38;5;255m* \033[0m",
        "\033[38;5;255m    *\033[38;5;111m ‘ \033[38;5;255m*\033[38;5;111m ‘  \033[0m"],
    'iconThunderyShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;111m     ‘ ‘ ‘ ‘ \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m"],
    'iconThunderyHeavyRain': [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;21;1m  ‚‘ \033[38;5;21;25m‘‚ \033["
        "38;5;21;25m‚‘   \033[0m",
        "\033[38;5;21;1m  ‚’‚’ \033[38;5;21;25m’‚’   \033[0m"],
    'iconThunderySnowShowers': [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;255m     *\033[38;5;228;5m⚡\033[38;5;255;25m *\033[38;5;228;5m⚡\033[38;5;255;25m * \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m"],
    'iconLightRain': [
        "\033[38;5;250m     .-.     \033[0m",
        "\033[38;5;250m    (   ).   \033[0m",
        "\033[38;5;250m   (___(__)  \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m",
        "\033[38;5;111m   ‘ ‘ ‘ ‘   \033[0m"],
    'iconHeavyRain': [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;21;1m  ‚‘‚‘‚‘‚‘   \033[0m",
        "\033[38;5;21;1m  ‚’‚’‚’‚’   \033[0m"],
    'iconLightSnow': [
        "\033[38;5;250m     .-.     \033[0m",
        "\033[38;5;250m    (   ).   \033[0m",
        "\033[38;5;250m   (___(__)  \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m",
        "\033[38;5;255m   *  *  *   \033[0m"],
    'iconHeavySnow': [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;255;1m   * * * *   \033[0m",
        "\033[38;5;255;1m  * * * *    \033[0m"],
    'iconLightSleet': [
        "\033[38;5;250m     .-.     \033[0m",
        "\033[38;5;250m    (   ).   \033[0m",
        "\033[38;5;250m   (___(__)  \033[0m",
        "\033[38;5;111m    ‘ \033[38;5;255m*\033[38;5;111m ‘ \033[38;5;255m*  \033[0m",
        "\033[38;5;255m   *\033[38;5;111m ‘ \033[38;5;255m*\033[38;5;111m ‘   \033[0m"],
    'iconFog': [
        "             ",
        "\033[38;5;251m _ - _ - _ - \033[0m",
        "\033[38;5;251m  _ - _ - _  \033[0m",
        "\033[38;5;251m _ - _ - _ - \033[0m",
        "             "],
    'iconUnknown': [
        "    .-.      ",
        "     __)     ",
        "    (        ",
        "     `-’     ",
        "      •      "]
}

windDir = {
    "N":   "\033[1m↓\033[0m",
    "NNE": "\033[1m↓\033[0m",
    "NE":  "\033[1m↙\033[0m",
    "ENE": "\033[1m↙\033[0m",
    "E":   "\033[1m←\033[0m",
    "ESE": "\033[1m←\033[0m",
    "SE":  "\033[1m↖\033[0m",
    "SSE": "\033[1m↖\033[0m",
    "S":   "\033[1m↑\033[0m",
    "SSW": "\033[1m↑\033[0m",
    "SW":  "\033[1m↗\033[0m",
    "WSW": "\033[1m↗\033[0m",
    "W":   "\033[1m→\033[0m",
    "WNW": "\033[1m→\033[0m",
    "NW":  "\033[1m↘\033[0m",
    "NNW": "\033[1m↘\033[0m",
}

# When weather description is too long and influence the display, abbreviate it.
weatherAbbre = {
    "Patchy light rain in area with thunder":"Rain with thunder",
    "Moderate or heavy rain shower":"Rain shower",
    "Patchy rain nearby":"Patchy rain",
    "Moderate or heavy rain in area with thunder":"Rain with thunder",
    "Thundery outbreaks in nearby":"Thundery outbreaks",
    "Patchy light drizzle":"Light drizzle"
}

class Query(object):
    def __init__(self, day, city):
        self.day = day
        self.time = [3,4,5,6]
        self.weatherCode = ''
        self.weather = ''
        self.date = ''
        self.hourly = ''
        self.tempC = 0
        self.winddir16Point = ''
        self.windspeedKmph = 0
        self.humidity = 0
        self.chanceofwater = 0
        self.city = city
        # Please input your API key before you run this script.
        self.key = "fa8b581c7f4845fe8b0213648161203"

    def query(self):
        url = base_url + "?key=%s&q=%s&num_of_days=3&format=json&lang=us" % (self.key, self.city)
        with request.urlopen(url) as f:
            if f.status!=200:
                return
            parsed_json = json.loads(f.read().decode('utf8'))
        data = parsed_json['data']              # acquire the whole data

        try:
            # Acquire the weather data. The number in [] represent the
            # day you want to query. '0' means today, and '1' means
            # tomorrow.
            self.weather = data['weather'][self.day]
        except KeyError:
            print("\033[1;31;49m" + "Please enter the correct city name or zip code！" + "\033[0m")
            sys.exit()
        self.date = self.weather['date']

    def detail(self, time):
        self.hourly = self.weather['hourly'][time]           # acquire the data in one hour.

        self.weatherCode = self.hourly['weatherCode']
        self.tempC = self.hourly['tempC']
        self.winddir16Point = self.hourly['winddir16Point']
        self.windspeedKmph = self.hourly['windspeedKmph']
        self.chanceofrain = self.hourly['chanceofrain']
        self.chanceofsnow = self.hourly['chanceofsnow']
        self.humidity = self.hourly['humidity']
        self.chanceofwater = int(self.chanceofrain) if int(self.chanceofrain) > int(self.chanceofsnow) else int(self.chanceofsnow)

    def printSingle(self):
        l1 = l2 = l3 = l4 = l5 = ''
        for time in self.time:
            self.detail(time)
            weather=self.hourly['weatherDesc'][0]['value']
            if(len(weather))>=18:
                weather=weatherAbbre[weather]
            l1 += '│' + icons[codes[self.weatherCode]][0] + weather
            if len(weather)<10:
                l1+='\t\t'
            elif len(weather)<18:
                l1+='\t'
            l2 += '│' + icons[codes[self.weatherCode]][1] + temp_color(int(self.tempC)) + \
                  "°C"+'\t\t'
            l3 += '│' + icons[codes[self.weatherCode]][2] + windDir[self.winddir16Point]+" "+ \
                  wind_color(int(self.windspeedKmph)) + "km/h" + '\t\t'
            l4 += '│' + icons[codes[self.weatherCode]][3] + "Precip:" + str(self.chanceofwater) + \
                  "%"
            l4 +='\t\t' if len(str(self.chanceofwater))<2 else '\t'
            l5 += '│' + icons[codes[self.weatherCode]][4] + "Humidity:" + str(self.humidity) + \
                  "%" + '\t'

        print(l1+"│")
        print(l2+"│")
        print(l3+"│")
        print(l4+"│")
        print(l5+"│")

    def printDay(self, delta):
        date_time= (date.today() + timedelta(days=delta)).strftime("%a, %d %b")

        line1 = "                                                         ┌─────────────┐                                                       "
        line2 = "┌───────────────────────────────┬────────────────────────| %s " \
                "|────────────────────────┬───────────────────────────────┐" % date_time
        line3 = "│           Morning             │             Noon       └──────┬──────┘    Evening             │            Night              │"
        line4 = "├───────────────────────────────┼───────────────────────────────┼───────────────────────────────┼───────────────────────────────┤"
        endline= "└───────────────────────────────┴───────────────────────────────┴───────────────────────────────┴───────────────────────────────┘"
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        self.printSingle()
        print(endline)


# change the temperature's color
def temp_color(temp):
    if temp >= 35 or temp <= -10:
        color = "\033[1;31;49m" + str(temp) + "\033[0m"
    elif (temp >= 25 and temp <35):
        color = "\033[1;33;49m" + str(temp) + "\033[0m"
    elif temp > 10 and temp < 25:
        color = "\033[1;32;49m" + str(temp) + "\033[0m"
    elif temp >-10 and temp <= 10:
        color = "\033[1;34;49m" + str(temp) + "\033[0m"
    return color


def wind_color(windspeed):
    if windspeed <= 5:
        color = "\033[1;32;49m" + str(windspeed) + "\033[0m"
    elif windspeed > 5 and windspeed <=10:
        color = "\033[1;33;49m" + str(windspeed) + "\033[0m"
    else:
        color = "\033[1;34;49m" + str(windspeed) + "\033[0m"
    return color


def main(argv):
    try:
        city=argv[1]
        city='+'.join(argv[1:])
    except IndexError:
        print("\033[1;31;49m" + "Enter city name or US zip code:" + "\033[0m")
        city = input()
        if city == '':
            sys.exit()
        city=city.replace(' ','+')
    day = [0,1,2]
    for i in day:
        query = Query(i,city)
        query.query()
        query.printDay(i)

if __name__ == "__main__":
    main(sys.argv)
