import requests

headerdata = {'T1':'First_Header','T2':'Second_Header_Header'}

response = requests.get('https://httpbin.org/get',headers=headerdata,verify=False)
print(response.text)
