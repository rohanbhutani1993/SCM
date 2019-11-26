from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import UserDetails
from .forms import UserLoginForm
from django.core.paginator import Paginator
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
    userLoginDetails = UserDetails.objects.filter(userName = userName, Password = password)
    if userLoginDetails:
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
    else:
        return HttpResponse("Invalid username or password.")

def DisplayMapView(request):
    return render(request,"TrafficMap.html",{})


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
    
    
    page= request.GET.get('page',1)
    paginator = Paginator(dublinbus['results'], 20)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {
        "data": data
        }    
    return render(request,"BusRouteInfo.html",context)

def DisplayEventsData(request):
    
    response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?countryCode=IE&apikey=u2MCIW0dPwxqAZMCssL2PrGWWfdkGedj')
    events=response.json()
    dict1 = dict()
    for i in range(0 , len(events['_embedded']['events'])):
        
        dict1[events['_embedded']['events'][i]['id']] = {'name':events['_embedded']['events'][i]['name'],
                                                        'dateTime': events['_embedded']['events'][i]['dates']['start']['localTime'] + " " + 
                                                        events['_embedded']['events'][i]['dates']['start']['localDate'],
                                                        'location': "Latitude - " + events['_embedded']['events'][i]['_embedded']['venues'][0]['location']['latitude'] + " " +
                                                        "Longitude - " + events['_embedded']['events'][i]['_embedded']['venues'][0]['location']['longitude']
                                                        
                                                         }
                                                        

    context = {
        "data" : dict1
        }
    return render(request,"events.html",context)


def DisplayDublinBikesData(request):
    response= requests.get(' https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=77cf7ab00377c7f4cc621765273db0e7daf18f82')
    dublinbikes=response.json()

    page= request.GET.get('page',1)
    paginator = Paginator(dublinbikes, 20)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    context = {
        "data" : data
        }
    return render(request,"dublinbikes.html", context)


def push_notify(request):
    from pusher_push_notifications import PushNotifications

    beams_client = PushNotifications(
        instance_id='422713b7-8870-499a-8534-5553787dc86c',
         secret_key='6DACD3113B8FF98826AB73E91EB1BF4EADC216BBB8567B562A065F4BD1E71C60',
    )
    response = beams_client.publish_to_interests(
    interests=['hello'],
    publish_body={
        'apns': {
            'aps': {
                'alert': 'Notification form Dashboard!'
            }
        },
        'fcm': {
            'notification': {
                'title': 'Notification from Dashboard!',
                'body': 'Notification from Dashboard!'
            }
        }
    }
    )

    return HttpResponse('Notification Sent')


    

