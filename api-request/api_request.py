import requests
api_key = "e6487c547d0f23a291fc3b13300052f9"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

# def fetch_data():
#     print("Fetching data from Weatherstack API...")
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
#         print("API request successful.")
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"API request failed: {e}")
#         raise
        
# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-10-12 00:21', 'localtime_epoch': 1760228460, 'utc_offset': '-4.0'}, 'current': {'observation_time': '04:21 AM', 'temperature': 16, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '07:04 AM', 'sunset': '06:20 PM', 'moonrise': '10:34 PM', 'moonset': '01:49 PM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 69}, 'air_quality': {'co': '137.85', 'no2': '10.55', 'o3': '67', 'so2': '4.95', 'pm2_5': '6.85', 'pm10': '7.85', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 24, 'wind_degree': 77, 'wind_dir': 'ENE', 'pressure': 1022, 'precip': 0, 'humidity': 72, 'cloudcover': 75, 'feelslike': 16, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}