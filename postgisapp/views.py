from django.http import JsonResponse
import random

from .models import Location
from django.contrib.gis.geos import Point
#checking whether the docker container is serving or not
def index(request):
    data = {'message': 'Hello, World!'}
    return JsonResponse(data)

#Adds a Random Location
def addLocation(request):
    try:
        random_latitude = random.uniform(-90, 90)
        random_longitude = random.uniform(-180, 180)
        # Create a new location with the random point
        location = Location(name='Random Location', point=Point(x=random_longitude, y=random_latitude))
        location.save()
        data = {
                'msg':'success',
                'id': location.id,
                'name': location.name,
                'point': {
                    'latitude': location.point.y,
                    'longitude': location.point.x,
                }
            }
        return JsonResponse(data)
    except Exception as e:
        error=str(e)
        return JsonResponse({'error':f"Unexpected Error {error}"},status=404)

def allLocation(request):
    try:
        locations=Location.objects.all().order_by('-id')
                # Create a list to store the data of all locations
        locations_data = []

            # Loop through each location and append its data to the list
        for location in locations:
            location_data = {
                    'id': location.id,
                    'name': location.name,
                    'point': {
                        'latitude': location.point.y,
                        'longitude': location.point.x,
                    }
                }
            locations_data.append(location_data)

            # Create a dictionary to hold the list of all locations
        data = {'locations': locations_data}

            # Return the JsonResponse with the data
        return JsonResponse(data)
    except Exception as e:
        error=str(e)
        return JsonResponse({'error':f"Unexpected Error {error}"},status=404)

#For viewing a specific location
def viewLocation(request,locationId):
    try:
        location=Location.objects.get(id=locationId)
        data = {
                'id': location.id,
                'name': location.name,
                'point': {
                    'latitude': location.point.y,
                    'longitude': location.point.x,
                }
            }
        return JsonResponse(data)
    except Exception as e:
        error=str(e)
        return JsonResponse({'error':f"Unexpected Error {error}"},status=404)
