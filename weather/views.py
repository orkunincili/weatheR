from django.shortcuts import render
import http.client,json
from .forms import CityForm
# Create your views here.
def index(request):

    form = CityForm()
    city="ankara"
    if request.method =="POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city=form.cleaned_data['city']
    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 7pWscfZvQUT4Mg1xdChzXu:2OMTXkdUKTKBYwbqzQhvXG"
    }

    conn.request("GET", "/weather/getWeather?data.lang=en&data.city={}".format(city), headers=headers)

    res = conn.getresponse()
    data = res.read()
    weather_result = json.loads(data)

    weather = {
        'city':weather_result['city'],
        'results':weather_result['result'],


    }
    context = {
        'weather':weather,
        'form':form
    }
    return render(request,'weather/weather.html',context)