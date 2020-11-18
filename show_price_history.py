import matplotlib.pyplot as plt
import os, sys

vin = '5YJ3E1EA0HF001099'
path = 'C:/Users/Kaeden/Files/tesla-inventory'

names = []
values = []
paths = os.listdir(path)
for filepath in paths:
	with open(os.path.join(path, filepath)) as f:
		price = 0
		date = ''
		for line in f:
			#print(line)
			if 'Request date:' in line and date == '':
				date = line[15:25]
			if vin in line:
				line2 = line[line.index('$')+1:line.index('$')+7]
				if '"' in line2:
					line2 = line2[0:len(line2) - 1]
				#print(line2)
				price = int(line2)
				print()
				break
		if date != '' and price != 0:
			values.append(price)
			names.append(date)

print(names)
print(values)

plt.figure('Price History')
plt.plot(names, values)
plt.ylabel('Price (USD)')
plt.xlabel('Date')
plt.suptitle('Price History | ' + vin)
plt.show()