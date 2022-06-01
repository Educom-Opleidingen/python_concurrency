from datetime import datetime
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
    for nr in image_nrs:
        download_image(nr)


if __name__ == '__main__':

    nr_images = 40

    print(f'Started part 1 at {datetime.now():%d-%m-%Y %H:%M:%S}...')
    t1 = time.perf_counter()

    download_images(nr_images)

    t2 = time.perf_counter()
    print(f'Finished part 1 at {datetime.now():%d-%m-%Y %H:%M:%S}.')

    print(f'Part 1 took {round(t2 - t1, 2)} seconds')
