from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import UserDetails
from .forms import UserLoginForm
import requests
# Create your views here.
def login_view(request):
    form = UserLoginForm(request.POST or None)        
    context = {
        'form': form
        }

    return render(request, "login.html", context)

def ValidateLoginView(request):
    userName = request.POST['userName']
    password = request.POST['password']
    userLoginDetails = UserDetails.objects.get()
    if userLoginDetails.userName == userName and userLoginDetails.Password == password:
               return render(request,"dashboard.html",{})
    else:
        return HttpResponse("Invalid username or password.")

def DisplayMapView(request):
    return render(request,"home.html",{})

def DisplayDublinBusData(request):
    #response=route_list(self,None)
    response = requests.get('https://data.dublinked.ie/cgi-bin/rtpi/routelistinformation')
    dublinbus=response.json()
    dublinbus['results']
    print( dublinbus['results'])
    context = {
        "data" : dublinbus['results']
        }
    #RTPI_API.route_list(operator= None):
    return render(request,"dublinbus.html",{})

def DisplayEventsData(request):
    city="dublin"
    response = requests.get('https://www.eventbriteapi.com/v3/events/search/?location.address='+city+'&location.within=10km&expand=venue&token=NL3IVYPNAYASG6QYJSMF')
    events=response.json()
    context = {
        "data" : events['results']
        }
    return render(request,"event.html",{})


def DisplayPollutionData(request):
    response = requests.get('http://erc.epa.ie/real-time-air/www/aqindex/aqih_json.php')
    pollution = response.json()
    dict1 = dict()
    for i in range(0, len(pollution['aqihsummary'])):
        if '_' in pollution['aqihsummary'][i]['aqih-region']:
            region = pollution['aqihsummary'][i]['aqih-region'].split('_')[0] + " " + pollution['aqihsummary'][i]['aqih-region'].split('_')[1]
        else:
            region = pollution['aqihsummary'][i]['aqih-region']
        dict1[region] = pollution['aqihsummary'][i]['aqih']
        
    context = {
        "data" : dict1
        }
    return render(request, "pollution.html", context)

def DisplayDublinBusData(request):
    response = requests.get('https://data.dublinked.ie/cgi-bin/rtpi/routelistinformation')
    dublinbus=response.json()
    
    context = {
        "data" : dublinbus['results']
        }
    return render(request,"BusRouteInfo.html",context)

def DisplayEventsData(request):
    city="dublin"
    response = requests.get('https://www.eventbriteapi.com/v3/events/search/?location.address='+city+'&location.within=10km&expand=venue&token=NL3IVYPNAYASG6QYJSMF')
    events=response.json()
    context = {
        "data" : events['events']
        }
    return render(request,"events.html",context)

    

