import concurrent.futures
from datetime import datetime
import os
from PIL import Image, ImageFilter
import random
import requests
import shutil
import string
import time


# CLI VERSION OF THE CONCURRENCY DEMO APP

# FUNCTIONS
def download_image(nr: int) -> None:
    dimension_images = '1920x1080'.split('x')
    file_name = f'image_{str(nr).zfill(3)}.jpg'
    response = requests.get(f'https://picsum.photos/{dimension_images[0]}/{dimension_images[1]}?random')
    file = open(file_name, 'wb')
    file.write(response.content)
    file.close()
    print(f'- Downloaded {file_name}')


def download_images(nr_images: int, threading_enabled: bool):

    image_nrs = range(1, nr_images + 1)

    if threading_enabled:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(download_image, image_nrs)
    else:
        for nr in image_nrs:
            download_image(nr)


def process_image(nr: int) -> None:
    dimension_images = '1280x1024'.split('x')
    file_name = f'image_{str(nr).zfill(3)}.jpg'
    img = Image.open(f'{file_name}')

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail((int(dimension_images[0]), int(dimension_images[1])))
    img.save(f'processed_{file_name}')
    print(f'- Processed {file_name}')


def process_images(nr_images: int, multi_processing_enabled: bool):

    image_nrs = range(1, nr_images + 1)

    if multi_processing_enabled:
        with concurrent.futures.ProcessPoolExecutor(10) as executor:
            executor.map(process_image, image_nrs)
    else:
        for nr in image_nrs:
            process_image(nr)


# CONFIGURING AND RUNNING IT
if __name__ == '__main__':

    # CONFIGURATION
    nr_images = 10
    threading_enabled = False
    multi_processing_enabled = False
    skip_second_part = False

    # THE ACTUAL PROCESS
    print(f'Started part 1 at {datetime.now():%d-%m-%Y %H:%M:%S}...')
    t1 = time.perf_counter()

    download_images(nr_images, threading_enabled)

    t2 = time.perf_counter()
    print(f'Finished part 1 at {datetime.now():%d-%m-%Y %H:%M:%S}.')

    if not skip_second_part:
        print('')
        print(f'Started part 2 at {datetime.now():%d-%m-%Y %H:%M:%S}...')
        t3 = time.perf_counter()

        process_images(nr_images, multi_processing_enabled)

        t4 = time.perf_counter()
        print(f'Finished part 2 at {datetime.now():%d-%m-%Y %H:%M:%S}.')

    print('')
    print(f'Number of images: {nr_images} | Threading: {threading_enabled} | '
          f'Multi processing: {multi_processing_enabled} | Skip second part: {skip_second_part}')
    print(f'Part 1 took {round(t2 - t1, 2)} seconds')
    if not skip_second_part:
        print(f'Part 2 took {round(t4 - t3, 2)} seconds')
