import urllib.request
import urllib.parse



def calc_progress(full=100, curp=0):
    try:
        return f"{100 / (full / curp)}%"

    except ZeroDivisionError:
        return "###############"

req = urllib.request.Request(r"http://localhost:9000/api/issues/search?componentKeys=VueComponentLib&s=FILE_LINE&resolved=false&ps=100&facets=severities%2Ctypes&additionalFields=_all&timeZone=Asia%2FBangkokmd", )

reader = urllib.request.urlopen(req)


size = int(reader.headers.get("Content-Length"))

with open("output.json", 'wb')as f:
    curr = 0

    while True:
        section = reader.read(1024)

        if not section:
            break

        

        f.write(section)
        curr += len(section)


        print(calc_progress(size, curr))