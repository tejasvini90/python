

#Q]to find date and time using datetime libraray
import datetime
d = datetime.datetime.today()
print('Current year: ', d.year)
print('Current month: ', d.month)
print('Current day: ', d.day)

import datetime
d = datetime.datetime.now()
print(d)


#Q]to get file frm s3 into spider and perform add on 177 and store the file on desktop

import requests

url = "https://collabera-aws-training.s3.amazonaws.com/employees01.csv"

headers = {
   'Host': "collabera-aws-training.s3.amazonaws.com",
   'X-Amz-Content-Sha256': "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
   'X-Amz-Date': "20190703T185532Z",
   'Authorization': "AWS4-HMAC-SHA256 Credential=AKIA4SOMN2PT4N3C32NF/20190703/us-east-1/s3/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=403a2fa64de254a467af113a88ef0b52944a43cb2cb4d6c3dde5e28010c19318",
   'User-Agent': "PostmanRuntime/7.15.0",
   'Accept': "*/*",
   'Cache-Control': "no-cache",
   'Postman-Token': "fd78b54b-8833-4c3e-a262-5a5fbcede79d,2fff30ed-43d4-4be6-9787-136c43d8da8a",
   'accept-encoding': "gzip, deflate",
   'Connection': "keep-alive",
   'cache-control': "no-cache" 
   }

response = requests.request("GET", url, headers=headers)

print(response.text)

response.text.split('\n')[-2]
response.text.split('\n')[-2].split(',')[-3]
response.text.split('\n')[-2].split(',')[-3].split(' ')[-3]
int(response.text.split('\n')[-2].split(',')[-3].split(' ')[-3])+2
t=int(response.text.split('\n')[-2].split(',')[-3].split(' ')[-3])+2
f1=open('C:/Users/akshay/Desktop/froms3.txt','w')
f1.write(str(t))
f1.close()

#Q] to get file frm url shared using import requests 
import requests
requests.get('https://raw.githubusercontent.com/becloudready/snowflake-tutorials/master/dataset/employees01.csv')  ###get http get command
r=requests.get('https://raw.githubusercontent.com/becloudready/snowflake-tutorials/master/dataset/employees01.csv')  ###get http get command
r
r.status_code
r.text.split('\n')[-2]
f1=open('C:/Users/akshay/Desktop/request.txt','w')
t=r.text.split('\n')[-2]
f1.write(t)
f1.close()


