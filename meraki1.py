import json
import requests

response=requests.get("http://saral.navgurukul.org/api/courses")
print(response.text)


response=requests.get("http://saral.navgurukul.org/api/courses")
with open("file_json.json","w") as d:
    json.dump((response.json()),d,indent=5)
    print(response)



