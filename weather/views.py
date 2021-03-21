from django.shortcuts import render
import http.client,json
from .forms import CityForm
from .classes import Weat
# Create your views here.
def index(request):

    form = CityForm()
    city=Weat.default_city
    if request.method =="POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city=form.cleaned_data['city']

    conn=Weat.create_connection()

    weather_result=Weat.req_and_res(conn,city)

    weather = {
        'city':weather_result['city'],
        'results':weather_result['result'],


    }
    context = {
        'weather':weather,
        'form':form
    }
    return render(request,'weather/weather.html',context)