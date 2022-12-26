from pyowm import OWM
import xml.etree.ElementTree as ET

owm = OWM('b25452b3be3de65a6ea6f4408121deab')
place= input("Enter the City: ")
country = input("Enter country: ")
point = place + ', ' + country
mrg = owm.weather_manager();
observer = mrg.weather_at_place(point)
w = observer.weather
status = w.detailed_status
humidity = w.humidity
t = w.temperature('celsius')['temp']


weather = ET.Element('weather')
records = ET.SubElement(weather, 'records')
wp = ET.SubElement(records, 'place')
ws = ET.SubElement(records, 'status')
wt = ET.SubElement(records, 'temperature')
wh = ET.SubElement(records, 'humidity')
wp.text = str(point)
ws.text = str(status)
wt.text = str(t)
wh.text = str(humidity)
my_data = ET.tostring(weather, encoding='unicode')
myfile = open(input("File name: "), 'w')
myfile.write(my_data)


def weather():
    print("in " + str(place) + " now is " + str(status) +
          "\n temperature " + str(round(t)) + " celsius" +
          "\n humidity " + str(humidity) + "%")
#weather()