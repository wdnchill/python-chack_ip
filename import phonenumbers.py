import requests

def track_phone_number(phone_number):
    # Ganti <YOUR_API_KEY> dengan kunci API yang Anda dapatkan dari Numverify
    api_key = "<YOUR_API_KEY>"
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=&format=1"

    try:
        response = requests.get(url)
        data = response.json()

        if data["valid"]:
            print("Informasi Nomor Telepon:")
            print(f"Nomor Telepon: {data['number']}")
            print(f"Negara: {data['country_name']}")
            print(f"Lokasi: {data['location']}")
            print(f"Provider: {data['carrier']}")
        else:
            print("Nomor telepon tidak valid.")

    except requests.exceptions.RequestException as e:
        print("Terjadi kesalahan saat menghubungi API Numverify:", str(e))

phone_number = input("Masukkan nomor telepon: ")
track_phone_number(phone_number)
