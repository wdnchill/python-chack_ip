import socket
import requests

def get_ipv4_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        try:
            sch_id_url = url.replace(".id", ".sch.id",".go.id","org")
            ip_address = socket.gethostbyname(sch_id_url)
            return ip_address
        except socket.gaierror:
            return None

def get_location(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        data = response.json()
        if 'error' in data:
            return None
        country = data.get('country_name')
        region = data.get('region')
        city = data.get('city')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        return f"Location: {city}, {region}, {country}\nCoordinates: {latitude}, {longitude}"
    except requests.exceptions.RequestException:
        return None

url = input("Masukkan alamat URL: ")
ipv4_address = get_ipv4_address(url)

if ipv4_address:
    print(f"IPv4 Address: {ipv4_address}")
    location = get_location(ipv4_address)
    if location:
        print(location)
    else:
        print("Lokasi tidak ditemukan.")
else:
    print("Alamat URL tidak valid.")
