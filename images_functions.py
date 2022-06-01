import concurrent.futures
import os
import random
import requests
import shutil
from streamlit_functions import create_output_markdown
import subprocess
import string
import sys


def create_and_change_into_random_folder() -> str:
    project_root = os.path.realpath(os.path.join(os.path.dirname(__file__)))
    random_folder = f'{project_root}/{"".join(random.choice(string.ascii_letters) for i in range(10))}'
    if os.path.exists(f'{random_folder}'):
        shutil.rmtree(f'{random_folder}')
    os.makedirs(f'{random_folder}')
    os.chdir(f'{random_folder}')
    return random_folder


def download_image(nr: int) -> str:
    dimension_images = '1920x1080'.split('x')
    file_name = f'image_{str(nr).zfill(3)}.jpg'

    response = requests.get(f'https://picsum.photos/{dimension_images[0]}/{dimension_images[1]}?random')

    file = open(f'{file_name}', 'wb')
    file.write(response.content)
    file.close()

    return f'- Downloaded {file_name}'


def download_images(nr_images: int, threading_enabled: bool) -> None:

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


def delete_random_folder(random_folder: str) -> None:
    project_root = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    os.chdir(f'{project_root}')
    if os.path.exists(f'{random_folder}'):
        shutil.rmtree(f'{random_folder}')
