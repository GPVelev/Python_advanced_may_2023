import unittest


def forecast(*city_and_weather):
    locations = {}

    for city, weather in city_and_weather:
        if city not in locations:
            locations[city] = weather
    sorted_result = {k: v for k, v in sorted(locations.items(), key=lambda x: (x[1], x[0]))}

    sunny = ""
    cloudy = ""
    rainy = ""

    for city, weather in sorted_result.items():
        if weather == "Sunny":
            sunny += f'{city} - {weather}\n'

        elif weather == "Cloudy":
            cloudy += f'{city} - {weather}\n'

        elif weather == "Rainy":
            rainy += f'{city} - {weather}\n'
    return sunny + cloudy + rainy


class Test(unittest.TestCase):
    def test_hourly_forecast(self):
        result = forecast(
            ("Sofia", "Sunny"),
            ("London", "Cloudy"),
            ("New York", "Sunny"))
        self.assertEqual(
            result.strip(),
            """New York - Sunny
Sofia - Sunny
London - Cloudy""")


if __name__ == '__main__':
    unittest.main()
