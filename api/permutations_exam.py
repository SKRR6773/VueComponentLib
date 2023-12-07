import requests
from itertools import permutations
import json

'''

fetch("http://localhost:7700/chk_options", {
  "headers": {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9,th;q=0.8",
    "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryx0inr5vqTyOtNnAp",
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  },
  "referrer": "http://localhost:5173/",
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": "------WebKitFormBoundaryx0inr5vqTyOtNnAp\r\nContent-Disposition: form-data; name=\"answer\"\r\n\r\n[[\"52*54\",\"1224\"],[\"7/17\",\"0.4117647058823529\"],[\"24x2\",\"48\"],[\"36-84\",\"2\"],[\"24*51\",\"1.9545454545454546\"],[\"43/22\",\"2808\"],[\"24+2*0\",\"24\"],[\"1+1\",\"-48\"]]\r\n------WebKitFormBoundaryx0inr5vqTyOtNnAp--\r\n",
  "method": "POST",
  "mode": "cors",
  "credentials": "omit"
});

'''

res = requests.get("http://localhost:7700/exam_options")
data = res.json()
res.close()


left_data = data['left']
right_data = data['right']


all_right_data = list(permutations(right_data))


for right_row in all_right_data:
    body = {
        "answer": list(zip(left_data, right_row))
    }

    print(body)
    

    res = requests.post("http://localhost:7700/chk_options", data=json.dumps(body), )
    print(res.text)
    res.close()