import requests
from django.shortcuts import render
from django.http import HttpResponse
from .forms import cityform
# Create your views here.
def index(request):
	if request.method=='POST':
		url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=cf4d5bdc6f70e14a3bc9c5029d0b4bd0'
		city=request.POST.get("city")

		result=requests.get(url.format(city)).json()

		weather={
		'city': city,
		'temperature': result['main']['temp'],
		'description': result['weather'][0]['description'],
		'icon': result['weather'][0]['icon'],
		}

		context={'weather':weather}

		return render(request=request,template_name="main.html",context={"weather":weather})

	else:
		return render(request=request,template_name="main.html")		