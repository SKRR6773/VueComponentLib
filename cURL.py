import urllib.request
import urllib.parse



def calc_progress(full=100, curp=0):
    try:
        return f"{100 / (full / curp)}%"

    except ZeroDivisionError:
        return "###############"

req = urllib.request.Request("http://mrg-web01.mrgshrimp.local/GA_SERVICES/translate/documentation/UNIT-3.pdf", )

reader = urllib.request.urlopen(req)


size = reader.headers.get("Content-Length")

with open("output.pdf", 'wb')as f:
    curr = 0

    while True:
        section = reader.read(1024)

        if not section:
            break

        
        print(calc_progress(size, curr))


        f.write(section)
        curr += len(section)