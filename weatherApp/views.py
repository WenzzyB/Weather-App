import requests
from django.shortcuts import render
from .models import Citys
from .forms import CityForm
# Create your views here.
def index(request):
    api_key = "1cee9480a1f1941f545c702d6f4ec3ac"
    url_req = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + api_key
    
    if (request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    
    cities = Citys.objects.all()
    all_cities_info = []
    for city in cities:
        res = requests.get(url_req.format(city.name)).json()
        city_info = {
            "city" : city.name,
            "temp" : res["main"]["temp"],
            "icon" : res["weather"][0]["icon"]
        }
        all_cities_info.append(city_info)

    context = {'cities' : all_cities_info, 'form' : form}
    print(city_info)
    return render(request, template_name = 'weatherApp/index.html', context = context)