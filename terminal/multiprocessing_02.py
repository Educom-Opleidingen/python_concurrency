import concurrent.futures
from datetime import datetime
import os
from PIL import Image, ImageFilter
import requests
import time


def download_image(nr: int) -> None:
    dimensions = '1920x1080'.split('x')
    file_name = f'image_{str(nr).zfill(3)}.jpg'
    response = requests.get(f'https://picsum.photos/{dimensions[0]}/{dimensions[1]}?random')
    file = open(file_name, 'wb')
    file.write(response.content)
    file.close()
    print(f'- Downloaded {file_name}')


def download_images(nr_images: int):
    image_nrs = range(1, nr_images + 1)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, image_nrs)


def process_image(nr: int) -> None:
    dimension_images = '1280x1024'.split('x')
    file_name = f'image_{str(nr).zfill(3)}.jpg'
    img = Image.open(f'{file_name}')

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail((int(dimension_images[0]), int(dimension_images[1])))
    img.save(f'processed_{file_name}')
    print(f'- Processed {file_name}')


def process_images(nr_images: int):

    image_nrs = range(1, nr_images + 1)

    with concurrent.futures.ProcessPoolExecutor(10) as executor:
        executor.map(process_image, image_nrs)


if __name__ == '__main__':

    nr_images = 40

    print(f'Started part 1 at {datetime.now():%d-%m-%Y %H:%M:%S}...')
    t1 = time.perf_counter()

    download_images(nr_images)

    t2 = time.perf_counter()
    print(f'Finished part 1 at {datetime.now():%d-%m-%Y %H:%M:%S}.')

    print('')

    print(f'Started part 2 at {datetime.now():%d-%m-%Y %H:%M:%S}...')
    t3 = time.perf_counter()

    process_images(nr_images)

    t4 = time.perf_counter()
    print(f'Finished part 2 at {datetime.now():%d-%m-%Y %H:%M:%S}.')

    print(f'Part 1 took {round(t2 - t1, 2)} seconds')
    print(f'Part 2 took {round(t4 - t3, 2)} seconds')

    [os.remove(file) for file in os.listdir(os.getcwd()) if file.endswith('.jpg')]
