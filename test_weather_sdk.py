from weather_sdk import WeatherSDK, API_KEY
import json

weather_sdk = WeatherSDK(API_KEY)

user_input = input("Введите названия городов через запятую: ")
cities = [city.strip() for city in user_input.split(",")]

weather_data_for_cities = {}


def format_weather_data(raw_data):
    return {
        "weather": {
            "main": raw_data["weather"][0]["main"],
            "description": raw_data["weather"][0]["description"],
        },
        "temperature": {
            "temp": raw_data["main"]["temp"],
            "feels_like": raw_data["main"]["feels_like"],
        },
        "visibility": raw_data["visibility"],
        "wind": {
            "speed": raw_data["wind"]["speed"],
        },
        "datetime": raw_data["dt"],
        "sys": {
            "sunrise": raw_data["sys"]["sunrise"],
            "sunset": raw_data["sys"]["sunset"]
        },
        "timezone": raw_data["timezone"],
        "name": raw_data["name"],
    }


for city_name in cities:
    try:
        raw_weather_data = weather_sdk.get_weather_by_city(city_name)
        formatted_weather_data = format_weather_data(raw_weather_data)
        weather_data_for_cities[city_name] = formatted_weather_data
        print(f"Данные о погоде для {city_name}:")
        print(formatted_weather_data)
    except Exception as e:
        print(f"Ошибка при получении данных для города {city_name}: {e}")

with open("weather_data_for_cities.json", "w") as json_file:
    json.dump(weather_data_for_cities, json_file, indent=4, ensure_ascii=False)

print("Данные о погоде для введенных городов сохранены в файле weather_data_for_cities.json")
