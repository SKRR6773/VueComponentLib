import sys
import json



load_data = None

with open(sys.argv[1], 'r')as fr:
    load_data = fr.read()



with open(sys.argv[1], 'w')as fw:
    json.dump(json.loads(load_data), fw, indent=4)