class WeatherStation:
    counter = 0

    def __init__(self, station):
        self.__station = station
        self.__condition = []
    def add_observation(self, now_observe):
        self.__condition.append(now_observe)
        WeatherStation.counter += 1

    def latest_observation(self):
        return self.__condition[WeatherStation.counter-1]

    def number_of_observations(self):
        return WeatherStation.counter

    def __str__(self):
        return f'{self.__station}, {WeatherStation.counter} observations'


# DRIVER CODE
station = WeatherStation('Houston')
station.add_observation('Rain 10mm')
station.add_observation("Sunny")
print(station.latest_observation())
print("=================================")
station.add_observation("Thunderstorm")
print(station.latest_observation())
print("=================================")
print(station.number_of_observations())
print(station)