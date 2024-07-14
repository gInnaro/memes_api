import io
from minio import Minio
from minio.error import S3Error
import requests
import os

minio_endpoint = "memes_api-minio-1:9000"
minio_key = "YFEYv4VRncc0rPSEvLbo"
minio_secret = "wKXcFRlrxcEwz19x3VTwfAMiUjysThqek23BPYKE"
minio_bucket_name = "memes"

class Minio_Memes:
    def __init__(self):
        self.client = Minio(endpoint=minio_endpoint, access_key=minio_key, secret_key=minio_secret, secure=False)

    def open_memes(self, name):
        image_bytes = self.client.get_object(minio_bucket_name, f'{name}.jpg')
        return io.BytesIO(image_bytes.read())

    def upload_memes(self, url, name):
        r = requests.get(url)
        with open(f'{name}.jpg', 'wb') as f:
            f.write(r.content)
        if r.status_code == 200:
            found = self.client.bucket_exists(minio_bucket_name)
            if not found:
                self.client.make_bucket(minio_bucket_name)
                print("Created bucket", minio_bucket_name)
            else:
                print("Bucket", minio_bucket_name, "already exists")

            self.client.fput_object(minio_bucket_name, f"{name}.jpg", f"{name}.jpg")
            os.remove(f"{name}.jpg")

    def delete_memes(self, name):
        try:
            self.client.stat_object(minio_bucket_name, f"{name}.jpg")
        except S3Error as exc:
            print('Такого файла нету')
        else:
            self.client.remove_object(minio_bucket_name, f"{name}.jpg")

if __name__ == "__main__":
    pass