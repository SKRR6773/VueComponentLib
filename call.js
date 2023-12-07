const fetch = require('node-fetch');

fetch("https://clients6.google.com/upload/drive/v3/files?uploadType=multipart&fields=id&key=AIzaSyAHCfkEDYwQD6HuUx2DyX3VylTrKZG7doM", {
  "headers": {
    "authorization": "SAPISIDHASH 1700720763_6027ebf9a6c5686e2b368fcb6461c0ad846c1d3e",
    "content-type": "multipart/mixed; boundary=\"-------314159265358979323846\"",
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version": "\"119.0.6045.160\"",
    "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"119.0.6045.160\", \"Chromium\";v=\"119.0.6045.160\", \"Not?A_Brand\";v=\"24.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-ch-ua-wow64": "?0",
    "x-clientdetails": "appVersion=5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F119.0.0.0%20Safari%2F537.36&platform=Win32&userAgent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F119.0.0.0%20Safari%2F537.36",
    "x-goog-authuser": "0",
    "x-goog-encode-response-if-executable": "base64",
    "x-javascript-user-agent": "google-api-javascript-client/1.1.0",
    "x-requested-with": "XMLHttpRequest",
    "Referer": "https://bard.google.com/",
    "Referrer-Policy": "origin"
  },
  "body": "\r\n---------314159265358979323846\r\nContent-Type: application/json\r\n\r\n{\"mimeType\":\"application/vnd.google-apps.spreadsheet\",\"name\":\"algolia search autocomplete is free?\"}\r\n---------314159265358979323846\r\nContent-Type: text/csv\r\n\r\nวางแผน,บันทึกทั้งหมด,คำขอค้นหา,แนะนำคำขอ,ราคา\nอาคารอัลโกเลีย,1 ล้าน,\"10,000\",\"10,000\",ฟรี\nอัลโกเลีย โกรว์,51 ดอลลาร์,\"10,000\",\"10,000\",ไม่มี\r\n---------314159265358979323846--",
  "method": "POST"
}).then(function(response){
    return response.json();
}).then(function(response){
    console.log(response);
}).catch(function(err){
    console.error(err);
});