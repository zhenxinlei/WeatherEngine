from xml.dom import  minidom
import csv

xmldoc = minidom.parse('./data/nyc_shoreline.kml')
placemarks = xmldoc.getElementsByTagName('Placemark')

print(len(placemarks))


with open('./data/nyc_shoreline_cor.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ["longitude", "latitdue"], delimiter = ',')
    writer.writeheader()
    for place in placemarks:
        lon = place.getElementsByTagName('longitude')
        lat = place.getElementsByTagName('latitude')

        dic = {"longitude":lon[0].firstChild.nodeValue, "latitdue":lat[0].firstChild.nodeValue}
        writer.writerow(dic)