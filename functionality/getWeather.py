import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {
    "callback":"test",
    "id":"2172797",
    "units":"%22metric%22 or %22imperial%22",
    "mode":"xml%2C html",
    "q":"London%2Cuk"
}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "52df80241emsh656a6b3eb2ac34ap13e4ccjsn09d896deb0ab"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)