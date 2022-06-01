import concurrent.futures
from PIL import Image, ImageFilter
import sys


def process_image(nr: int) -> str:
    dimension_images = '1280x1024'.split('x')
    file_name = f'image_{str(nr).zfill(3)}.jpg'
    img = Image.open(f'images/{file_name}')
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail((int(dimension_images[0]), int(dimension_images[1])))
    img.save(f'images/processed_{file_name}')
    return f'- Processed {file_name}'


def process_images(nr_images: int, multi_processing_enabled: bool) -> list:
    results = []
    image_nrs = range(1, nr_images + 1)

    if multi_processing_enabled:
        with concurrent.futures.ProcessPoolExecutor(10) as executor:
            for result in executor.map(process_image, image_nrs):
                results.append(result)
    else:
        for nr in image_nrs:
            result = process_image(nr)
            results.append(result)

    return results


if __name__ == '__main__':
    for r in process_images(int(sys.argv[1]), bool(int(sys.argv[2]))):
        print(r)
