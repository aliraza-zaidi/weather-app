from django.shortcuts import render
import json
import urllib.request
from datetime import datetime

# Create your views here.
def index(request):    
    data = {}
    city = ''
    if request.method == "POST":
        city = request.POST['city']
        try:  
            res = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a823a0bc1ab19ef22e99e8f477af8c87'
            ).read()
            json_data = json.loads(res)
                        
            data = {
                'city': city,
                'country_code': str(json_data['sys']['country']),
                'coordinates': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                'temperature': str(round(float(str(json_data['main']['temp'])) - 273)) + ' C',
                'pressure': str(json_data['main']['pressure']) + ' Pa',
                'humidity': str(json_data['main']['humidity']) + ' %',            
            }

        except:            
            data['error'] = "City not found. Please enter a valid city name."

    return render(request, 'index.html', data)
