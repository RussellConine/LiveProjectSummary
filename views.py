from django.shortcuts import render, redirect, get_object_or_404
from .forms import SkiForm
from .models import Ski
from rest_framework.exceptions import APIException
import requests


# weather check locations and urls
location_dict = {'Timberline Lodge': 'https://api.weather.gov/gridpoints/PQR/141,88/forecast',
                 'Paradise, WA (Mt. Rainier)': 'https://api.weather.gov/gridpoints/SEW/135,25/forecast'}

location_1 = location_dict['Timberline Lodge']


# ski homepage
def skis_home(request):
    return render(request, "Skis/skis_home.html")


# create skis via form on create_ski.html
def create_ski(request):
    form = SkiForm(data=request.POST or None)   # retrieve Ski Form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('create_ski')
    content = {'form': form}
    return render(request, 'Skis/create_ski.html', content)


# read all skis in database and display them in table on read_skis.html
def read_skis(request):
    entry = Ski.Skis.all()
    content = {'entry': entry}
    return render(request, 'Skis/read_skis.html', content)


# list detail for specific ski item, based on primary key of that ski item in database
def ski_details(request, pk):
    details = get_object_or_404(Ski, pk=pk)
    content = {'details': details}
    return render(request, 'Skis/ski_details.html', content)


def edit_ski(request, pk):
    pk = int(pk)
    item = get_object_or_404(Ski, pk=pk)
    form = SkiForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # if form is updated, send to details page of edited ski
            return redirect('details', pk)
        else:
            print(form.errors)
    else:
        return render(request, 'Skis/edit_skis.html', {'form': form, 'pk': pk})


def delete_ski(request, pk):
    pk = int(pk)
    item = get_object_or_404(Ski, pk=pk)
    print(item)
    if request.method == 'POST':
        item.delete()
        return redirect('read_all_skis')
    content = {'item': item, }
    return render(request, 'Skis/delete_skis.html', content)


# function to connect to national weather service's API, to look up weather for skiing at timberline lodge
def check_weather(request):
    try:
        response = requests.get(location_1)
    except:
        raise APIException("The connection to the API failed! Ensure the URL is correct.")
    weather_data = response.json()
    # save all the time periods available
    weather = weather_data['properties']['periods']
    # create blank dictionary that we'll build with time periods as key and forecast as value
    wx_dict = {}
    for timePeriod in weather:
        # build dictionary with time period's name (today, tonight, tomorrow, etc) as key and forecast as value
        wx_dict[timePeriod['name']] = timePeriod['detailedForecast']
    # nws.gov weather api reference: https://www.weather.gov/documentation/services-web-api
    print(wx_dict)
    content = {'wx_dict': wx_dict}
    return render(request, 'Skis/weather_check.html', content)
