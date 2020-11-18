import requests, json, urllib
from datetime import date

vin = '5YJ3E1EA0HF001099'   #example VIN
model = 'm3'  # ms, mx, m3, my
condition = 'used'  # used, new
zipcode = '98052'   #Search within 200 miles of this ZIP code


query = '{"query":{"model":"' + model + '","condition":"' + condition + '","options":{},"arrangeby":"Price","order":"asc","market":"US","language":"en","super_region":"north america","lng":-122.1257,"lat":47.6722,"zip":"' + zipcode + '","range":0},"offset":0,"count":100,"outsideOffset":0,"outsideSearch":false}'
y = json.loads(requests.get(
    'https://www.tesla.com/inventory/api/v1/inventory-results?query=' + urllib.parse.quote(query)).content)
print('Found ' + y['total_matches_found'] + ' vehicles in given area.')
found = False;
for result in y['results']:
    try:
        if (result['VIN'] == vin):
            print('Found VIN: ' + vin)
            for image in result['VehiclePhotos']:
                print(image['imageUrl'])
            found = True;
            break;
    except KeyError:
        if (result['VIN'] == vin):
            print('No Photos')
    except TypeError:
        print('TypeError.')
if (not found):
    print('VIN not found.')