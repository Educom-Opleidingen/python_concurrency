import concurrent.futures
import os
import requests
import shutil
from streamlit_functions import create_output_markdown
import subprocess
import sys


def download_image(nr: int) -> str:
    dimension_images = '1920x1080'.split('x')
    file_name = f'image_{str(nr).zfill(3)}.jpg'

    response = requests.get(f'https://picsum.photos/{dimension_images[0]}/{dimension_images[1]}?random')

    file = open(f'images/{file_name}', 'wb')
    file.write(response.content)
    file.close()

    return f'- Downloaded {file_name}'


def download_images(nr_images: int, threading_enabled: bool) -> None:
    if os.path.exists('images'):
        shutil.rmtree('images')
    os.makedirs('images')

    image_nrs = range(1, nr_images + 1)

    if threading_enabled:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for result in executor.map(download_image, image_nrs):
                create_output_markdown(result)
    else:
        for nr in image_nrs:
            result = download_image(nr)
            create_output_markdown(result)


def process_images(nr_images: int, multi_processing_enabled: bool) -> None:
    pi = subprocess.run([f'{sys.executable}', 'process_images.py', f'{nr_images}', f'{int(multi_processing_enabled)}'],
                        capture_output=True)
    for result in pi.stdout.decode().splitlines():
        create_output_markdown(result)
