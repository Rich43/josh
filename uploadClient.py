import os

import requests


def upload_file(file_path, file_server_url):
    with open(file_path, 'rb') as f:
        files = {'file': (os.path.basename(file_path), f)}
        response = requests.post(file_server_url, files=files)
        return response.status_code


def upload_folder(upload_folder_path, upload_server_url):
    for root, dirs, files in os.walk(upload_folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            status = upload_file(file_path, upload_server_url)
            if status == 200:
                print(f"Successfully uploaded {file_path}")
            else:
                print(f"Failed to upload {file_path}, status code: {status}")


if __name__ == "__main__":
    folder_path = "C:/Users"
    # noinspection HttpUrlsUsage
    server_url = "http://storage.wardcrew.com/pi/Seagate%20Por/"
    upload_folder(folder_path, server_url)
