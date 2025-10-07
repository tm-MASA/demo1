import requests
import time


def get_weather(city):
    api_key = "d9baa9b5f368abf028a2fec35e5469fc"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # cache-busting timestamp to avoid intermediate caches
    ts = int(time.time() * 1000)
    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    }
    complete_url = f"{base_url}q={city}&lang=es&appid={api_key}&units=metric&t={ts}"
    try:
        response = requests.get(complete_url, headers=headers, timeout=10)
    except Exception:
        return None

    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        wind = data.get('wind', {})
        weather_description = data.get('weather', [{}])[0].get('description', '')

        # Obtener latitud y longitud para consultar radiación
        lat = data.get('coord', {}).get('lat')
        lon = data.get('coord', {}).get('lon')

        radiation = None
        uv_index = None

        # Consultar radiación solar y UV sólo si tenemos coordenadas
        if lat is not None and lon is not None:
            radiation_url = f"https://api.openweathermap.org/data/3.0/solar_radiation?lat={lat}&lon={lon}&appid={api_key}&t={ts}"
            try:
                rad_response = requests.get(radiation_url, headers=headers, timeout=10)
                if rad_response.status_code == 200:
                    rad_data = rad_response.json()
                    radiation = rad_data.get('radiation', rad_data.get('data', None))
            except Exception:
                radiation = None

            uv_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={api_key}&t={ts}"
            try:
                uv_response = requests.get(uv_url, headers=headers, timeout=10)
                if uv_response.status_code == 200:
                    uv_data = uv_response.json()
                    uv_index = uv_data.get('current', {}).get('uvi', None)
            except Exception:
                uv_index = None

        return {
            'temperature': main.get('temp'),
            'pressure': main.get('pressure'),
            'humidity': main.get('humidity'),
            'wind_speed': wind.get('speed'),
            'description': weather_description,
            'radiation': radiation,
            'uv_index': uv_index
        }
    else:
        return None


# weather = get_weather("Santiago")
# print(weather)