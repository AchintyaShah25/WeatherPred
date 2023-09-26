import requests
# MY_LAT = 18.964896
MY_LAT = 36.335880
# MY_LNG = 72.813085
MY_LNG = -92.387500
API_ID = "10725f0a8677064f55b7ae1cf27c900d"
link = f"https://api.openweathermap.org/data/2.8/onecall?lat={MY_LAT}&lon={MY_LNG}&appid={API_ID}"
parameters = {
    "lat": MY_LAT,
    "lon":MY_LNG,
    "appid":API_ID
}
response = requests.get(link)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"]
hourly_id = []
for rn in hourly_data:
    a = rn["weather"]
    b = a[0]
    id_code = b["id"]
    hourly_id.append(id_code)
print(hourly_id)
umbrella = False
for induv in hourly_id:
    if induv < 700:
        umbrella = True
