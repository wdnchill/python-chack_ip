# ini termasuk dalam information Gathring atau menggumpulkan informasi target

#import yang terinstall di terminal 
# contoh pip install socket
import socket
import requests
import pprint
# mengisi inputan nama Domain
hostname = input('[+]Masukan nama Domain: ')
ip_address = socket.gethostbyname(hostname)
request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
# membuat hasil inputan lokasi menjadi code
geolocation = response.content.decode() 
# meghilangkan tanda () di hasil inputan agar mudah di baca
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
		pprrint.pprint(str(k) + ':' + str(v))
