import urllib.request
import urllib.parse


req = urllib.request.Request("http://mrg-web01.mrgshrimp.local/GA_SERVICES/translate/documentation/UNIT-3.pdf", )

reader = urllib.request.urlopen(req)


with open("output.pdf", 'wb')as f:
    while True:
        section = 
    f.write(reader.read())