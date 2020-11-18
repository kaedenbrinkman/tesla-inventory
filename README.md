# tesla-inventory
Python app for the Tesla Inventory API

The used inventory browser at https://www.tesla.com/inventory/used/ does not show all information about the cars.
I'm working on a python app for tracking price changes in used inventory and showing additional information such as the reason for being in inventory, etc.

Currently, script.py spits out a summary .CSV file of the cars available. You have to manually change the URL for ms, mx, etc. or for a different location.
You can track price changes by running the program once daily.

The other file, photos.py, is intended to find used photos of the car using the API. Tesla used to show these on their website, but they do not do it anymore.
There is also a visualization file for reading the generated .csv files in a path:
![Image of Price History Chart](/assets/example.png)
