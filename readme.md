# Open Weather SDK

Этот SDK позволяет легко получать данные о погоде для заданных городов, используя API сервиса OpenWeatherMap.

## Установка

Для использования SDK, клонируйте этот репозиторий и установите необходимые зависимости, активируйте виртуальное окружение:

```bash
git clone https://github.com/Starlight19973/sdk_open_weather.git
cd test_kameloon
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```

# API OpenWeather

Перейдите на официальный сайт: https://home.openweathermap.org/api_keys и сгенерируйте API_KEY
Далее создайте в корневой папке проекта файл с названием .env и поместите в него API_KEY в формате
API_KEY=ваш_ключ_api


# Применение

После установки всех зависимостей и подключения API_KEY:

Запустите файл test_weather_sdk.py командой python test_weather_sdk.py
В консоль выведется сообщение: Введите названия городов через запятую.
Введите назване города на Английском языке. В консоль выведется ответ в формате json, также данные будут записаны в json файл.


# Обратная связь

Если у вас есть вопросы, вы можете связаться со мной через...

* Telegram: @minin2728
* Email: mininnikita030@gmail.com


