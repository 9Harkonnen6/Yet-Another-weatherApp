# libraries
import requests
# main loop
while True:
    # API, Wroclav's ID
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?id=3081368&units=metric&appid=a89a223e85afb3a8c1c8433ec5f055e5')

    # if anything goes wrong that will inform you
    if r.status_code != 200:
        print(f'Whoops, something went wrong, {r.status_code}')

    print(f'[temperature]: {int(r.json()["main"]["temp"])} *C')
    print(f'[feels like]: {int(r.json()["main"]["feels_like"])} *C')

    refreshOrExit = input('Press ENTER to refresh...')   