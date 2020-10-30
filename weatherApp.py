# libraries
import PySimpleGUI as sg
import requests

# is it working?! git test

def get_temps():
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?id=3081368&units=metric&appid=a89a223e85afb3a8c1c8433ec5f055e5')
    r = r.json()
    return r
r = get_temps()
# theme config
sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND': '#eeeeee',
                                        'TEXT': 'black',
                                        'INPUT': 'black',
                                        'TEXT_INPUT': '#cccccc',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('#eeeeee', '#222222'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }
sg.theme('MyNewTheme')
layout = [[sg.Text("Wroclaw", key='-city-', background_color="#CDD0D5")],
          [sg.Frame("Temperature", [[sg.Column([[sg.Text('official:'), sg.Text(f"{round(r['main']['temp'])} °C", key='-official-', background_color="#CDD0D5")],[sg.Text('feels like:'),sg.Text(f"{round(r['main']['feels_like'])} °C", key='-feels_like-', background_color="#CDD0D5")]], element_justification='right')]]), sg.Button('Refresh')],
          [sg.Button('Exit')]]
# window initialization
window = sg.Window('weatherApp', layout)
# main loop
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Refresh':
        r = get_temps()
        window['-official-'].update(f"{round(r['main']['temp'])} °C")
        window['-feels_like-'].update(f"{round(r['main']['feels_like'])} °C")
window.Close()