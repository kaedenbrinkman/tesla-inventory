import requests
import json
from datetime import date

x = requests.get('https://www.tesla.com/inventory/api/v1/inventory-results?query=%7B%22query%22%3A%7B%22model%22%3A%22m3%22%2C%22condition%22%3A%22used%22%2C%22options%22%3A%7B%22TRIM%22%3A%5B%22MRRWD%22%2C%22LRRWD%22%2C%22LRAWD%22%5D%2C%22AUTOPILOT%22%3A%5B%22AUTOPILOT_FULL_SELF_DRIVING%22%5D%7D%2C%22arrangeby%22%3A%22Price%22%2C%22order%22%3A%22asc%22%2C%22market%22%3A%22US%22%2C%22language%22%3A%22en%22%2C%22super_region%22%3A%22north%20america%22%2C%22lng%22%3A-122.1257%2C%22lat%22%3A47.6722%2C%22zip%22%3A%2298052%22%2C%22range%22%3A0%7D%2C%22offset%22%3A0%2C%22count%22%3A50%2C%22outsideOffset%22%3A0%2C%22outsideSearch%22%3Afalse%7D')
y = json.loads(x.content)
today = date.today()
toExport = ('"Found ' + y['total_matches_found'] + ' results."\n')
toExport += ('"Request date: ' + str(today) + '"\n')
toExport += ('"VIN","MODEL","TRIM","MILAGE","AP","PRICE","LOCATION"\n')
for result in y['results']:
    toExport += (result['VIN'] + '","' + result['Model'] + '","' + result['TrimName'] + '","' + str(result['Odometer']) + ' ' + result['OdometerType'] + '","' + result['AUTOPILOT'][0] + '","$' + str(result['Price']) + '","' + result['MetroName'] + '"\n')

file = open(str(today) + ".csv", "w")
file.write(toExport)
file.close()