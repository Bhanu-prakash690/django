from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import JsonResponse
from .models import Crime, PoliceStation
import requests, json
import math
# Create your views here.


def distance(p1, p2):
    d = math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return d

def upload(request):
    return render(request, 'upload.html')


def map(request):
    return render(request, 'index.html')


def update_data_base(request):
    latitude = float(request.POST['latitude'])
    longitude = float(request.POST['longitude'])
    image = None
    video = None
    try:
        image = request.FILES['image']
        video = request.FILES['video']
    except:
        print(' ')

    description = request.POST['description']

    url = 'https://us1.locationiq.com/v1/reverse.php'
    params = {
        'key':'e1647973e5944d',
        'lat':str(latitude),
        'lon':str(longitude),
        'format':'json'
    }

    data = json.loads(requests.get(url, params=params).text)

    crime = Crime(
        latitude=latitude,
        longitude=longitude,
        image=image,
        video=video,
        description=description,
        display_name=data['display_name']
    )
    crime.save()

    police_stations = [(distance((x.latitude, x.longitude), (latitude, longitude)), x.pk) for x in PoliceStation.objects.all()]
    police_stations.sort(key=lambda x: x[0])

    shortest_ = [police_stations[0],]
    print(shortest_)

    url_ = 'https://maker.ifttt.com/trigger/crime_recorded/with/key/kg0M1ubFZhI0o5cJVMXEn_B_-GTxnCQRbcAtm32WfP7'
    msg_ = f'''
    description:{description}
    location:{data['display_name']}
    '''
    map_url = f'https://www.google.com/maps/search/?api=1&query={latitude},{longitude}'


    for station in shortest_:
        i = PoliceStation.objects.get(pk=station[1])
        print(i.phonenumber)
        data = {
            "value1":i.phonenumber,
            "value2":msg_,
            "value3":map_url
        }
        print(requests.post(url_, data=data))


    return HttpResponseRedirect(reverse('upload'))

def detail(request, pk):
    crime = Crime.objects.get(pk=pk)
    context = {
        'crime':crime
    }
    return render(request, 'detail.html', context)

def get_data(request):
    data = Crime.objects.all()
    json_data = []

    for i in data:
        image = None
        video = None
        try:
            image = i.image.url
            video = i.video.url
        except:
            print(' ')
        d = {
            'url':reverse('detail', args=(i.pk,)),
            'latitude':i.latitude,
            'longitude':i.longitude,
            'image':image,
            'video':video,
            'description':i.description,
            'display_name':i.display_name,
        }

        json_data.append(d)

    return JsonResponse({'data':json_data})
