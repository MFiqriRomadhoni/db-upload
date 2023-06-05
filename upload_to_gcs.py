from flask import Flask, request
from google.cloud import storage

BUCKET_NAME = 'capstone-c23-ps303_uploadimage'

app = Flask(__name__)

@app.route('/upload-image', methods=['POST'])
def upload_image():
    # Memverifikasi dan memvalidasi permintaan
    # (Implementasikan logika otorisasi atau validasi sesuai kebutuhan Anda)

    # Mendapatkan file gambar dari permintaan
    if 'image' not in request.files:
        return 'Tidak ada file gambar yang diunggah', 400
    
    image_file = request.files['image']
    image_name = image_file.filename

    # Menyimpan file gambar di sistem penyimpanan
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(image_name)
    blob.upload_from_file(image_file)

    # Mengirim respons balik ke aplikasi klien
    return 'Gambar berhasil diunggah', 200

if __name__ == '__main__':
    app.run()
