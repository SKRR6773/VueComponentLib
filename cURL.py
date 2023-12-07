import urllib.request
import urllib.parse



def calc_progress(full=100, curp=0):
    try:
        return f"{100 / (full / curp)}%"

    except ZeroDivisionError:
        return "###############"

req = urllib.request.Request(r"http://localhost:9000/api/issues/search?componentKeys=VueComponentLib&s=FILE_LINE&resolved=false&ps=100&facets=severities%2Ctypes&additionalFields=_all&timeZone=Asia%2FBangkokmd", headers={
    "Cookie": "XSRF-TOKEN=glk6gobkurnq1n9aqpd8vulul8; JWT-SESSION=eyJhbGciOiJIUzI1NiJ9.eyJsYXN0UmVmcmVzaFRpbWUiOjE3MDE5Mzk5MDU4MzgsInhzcmZUb2tlbiI6ImdsazZnb2JrdXJucTFuOWFxcGQ4dnVsdWw4IiwianRpIjoiQVl4Q2NiSFd2bkZpVC1tV2pLclgiLCJzdWIiOiJBWXdWT3l6b2pXRy1vb2VFdHN3XyIsImlhdCI6MTcwMTkyMTc5NiwiZXhwIjoxNzAyMTk5MTA1fQ.x9GWGDfCc4M6zeMcT7SgTAETxyoR7OqJU80mG7-hl4w"
})

reader = urllib.request.urlopen(req)


# size = int(reader.headers.get("Content-Length"))

with open("output.json", 'wb')as f:
    curr = 0

    while True:
        section = reader.read(1024)

        if not section:
            break

        

        f.write(section)
        # curr += len(section)


        # print(calc_progress(size, curr))