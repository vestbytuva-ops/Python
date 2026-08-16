import requests

def get_weather(city):
    api_key =
    url = f"http://weatherapi.com{api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        city_data = response.json()
        return city_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


city_name = input("Enter your city here")
city_info(city_name)

if get_city_info: 
    print(f"{city_info["name"].capitalize()}")
    print(f"{city_info["weather"]}")
    print(f"{city_info["UV-Index"]}")
