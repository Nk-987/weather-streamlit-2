API_key = "dd038d1fc8f86361f1da6e3ea73c2bce"
import requests

def get_data(place,forcast_days):
    # Url for getting data from website
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    
    # Requesting data using API key
    response = requests.get(url)
    data = response.json()
    
    # Filtering data
    filtered_data = data["list"]
    
    # We get weather for every 3 hour so , in 24 hour we get 8 temperatures
    n = 8*forcast_days
    filtered_data = filtered_data[:n]
    
    return filtered_data
    
if __name__ == "__main__":
    print(get_data("Tokyo",3))

