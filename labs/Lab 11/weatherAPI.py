import json 
import requests 

print('Widget1 is: ')
widgetOne = input()

print('Widget2 is: ')
widgetTwo = input()

r = requests.get('widgets.json')
data = r.json()
print(data['widget1'][0]['color'], data['widget2'][0]['color'])