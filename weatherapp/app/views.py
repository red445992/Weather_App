from django.shortcuts import render
import requests
from django.contrib import messages
# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kathmandu'
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=49587aa77601adceb3ec1565459ab112"
    param = {'units' : 'metric'}

    try:
        data = requests.get(url,param).json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        return render(request,'index.html',{'temp':temp,'city':city,'desc':desc,'icon':icon,'wind':wind,'humidity':humidity})
    except:
        data = requests.get(url,param).json()
        temp = 0
        desc = f"no city named {city}"
        messages.error(request,f"No city name {city}")
        return render(request,'index.html',{'temp':temp,'desc':desc,'city':city})