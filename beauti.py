import sys
import json



load_data = None

with open(sys.argv[1], 'r')as fr:
    with open(sys.argv[1], 'w')as fw:
        json.dump(json.loads(fr.read()), fw, indent=4)