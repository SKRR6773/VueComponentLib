import urllib.request
import urllib.parse



def calc_progress(full=100, curp=0):
    try:
        full / curp


        cur

    except ZeroDivisionError:
        pass

req = urllib.request.Request("http://mrg-web01.mrgshrimp.local/GA_SERVICES/translate/documentation/UNIT-3.pdf", )

reader = urllib.request.urlopen(req)


print(reader.headers.get("Content-Length"))

with open("output.pdf", 'wb')as f:
    while True:
        section = reader.read(1024)

        if not section:
            break

        

        f.write(section)