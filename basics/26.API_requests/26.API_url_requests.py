import requests

# API key: 11c0d3dc6093f7442898ee49d2430d20
def get_city():
    city = input('Please, inter your city: ')
    return(city)

def create_params(city):
    params = { "q": [city],
               "units": "metric",
               "appid": "11c0d3dc6093f7442898ee49d2430d20"
        }
    return params

url = "http://api.openweathermap.org/data/2.5/weather"

my_city = get_city()
my_params = create_params(my_city)

res = requests.get(url, params=my_params)
#print(res.status_code)
#print(res.headers['COntent-Type'])
#print(res.json())
data = res.json()
#print(data["main"])
print(f'Temperature in {my_city} is: {data["main"]["temp"]}. But it feels like {data["main"]["feels_like"]}' )
