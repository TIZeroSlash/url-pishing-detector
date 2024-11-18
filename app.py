from flask import Flask, render_template, request, redirect, jsonify
import requests
import random
import string
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load konfigurasi dari .env
load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY')
SAFE_BROWSING_URL = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}'

# In-memory dict untuk menyimpan URL shorten
url_map = {}

# Fungsi untuk memeriksa phishing menggunakan Google Safe Browsing
def check_phishing(url):
    payload = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    try:
        response = requests.post(SAFE_BROWSING_URL, json=payload)
        result = response.json()
        if 'matches' in result:
            return True
    except Exception as e:
        print(f"Error checking phishing: {e}")
        return False
    return False

# Fungsi untuk membuat short URL
def generate_short_code(length=6):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

# Halaman utama
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        
        # Cek apakah URL mengandung phishing
        if check_phishing(original_url):
            return render_template('index.html', message="Phishing URL terdeteksi! Mohon masukkan URL yang aman.")
        
        # Generate short code
        short_code = generate_short_code()
        url_map[short_code] = original_url

        # Kirim URL shortened ke user
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

# Redirect dari short URL
@app.route('/<short_code>')
def redirect_url(short_code):
    original_url = url_map.get(short_code)
    if original_url:
        return redirect(original_url)
    return jsonify({"error": "Invalid URL"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
