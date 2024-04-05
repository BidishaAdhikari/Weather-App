import requests
from bs4 import BeautifulSoup

def get_weather(city):
    # creating url and requests instance
    url = "https://www.google.com/search?q=" + "weather in" + city
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]


    return temp, time, sky
if __name__ == "__main__":
    # enter city name
    city = "Kolkata"
    temp, time, sky = get_weather(city) 
    print("City:", city)
    print("Temperature is", temp)
    print("Time:", time)
    print("Sky Description:", sky)